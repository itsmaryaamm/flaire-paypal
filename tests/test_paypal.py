"""PayPal sandbox rail: the adapter talks to PayPal's Payouts API; here PayPal is mocked."""
import httpx
import pytest

from app.core.config import get_settings
from app.integrations.payments import get_adapter
from app.integrations.payments import paypal as pp
from app.models import Card


class R:
    def __init__(self, code, data):
        self.status_code, self._d, self.text = code, data, str(data)

    def json(self):
        return self._d

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(self.status_code)


@pytest.fixture
def configured(monkeypatch):
    s = get_settings()
    monkeypatch.setattr(s, "paypal_client_id", "cid")
    monkeypatch.setattr(s, "paypal_client_secret", "sec")
    monkeypatch.setattr(s, "paypal_receiver_email", "merchant@sandbox.example")
    pp._token.update({"value": None, "exp": 0})
    return s


def card(balance=100_000):
    return Card(label="AI", provider="paypal", last4="1234", currency="SAR", status="active", credit_limit=balance, available_balance=balance)


def test_converts_sar_to_usd_and_pays_out(configured, monkeypatch):
    seen = {}

    def post(url, **kw):
        if url.endswith("/oauth2/token"):
            return R(200, {"access_token": "tok", "expires_in": 300})
        seen["body"], seen["auth"] = kw["json"], kw["headers"]["Authorization"]
        return R(201, {"batch_header": {"payout_batch_id": "PB123", "batch_status": "PENDING"}})

    monkeypatch.setattr(httpx, "post", post)
    c = card()
    res = get_adapter("paypal").authorize(c, 37_500, "Canva", "FLAIRE*Canva")  # SAR 375.00 -> USD 100.00
    assert res.ok and res.status == "authorized" and res.provider_ref == "paypal_PB123"  # PENDING at PayPal
    assert res.issuer_currency == "USD" and res.issuer_amount == 10_000 and res.fx_rate == 3.75
    item = seen["body"]["items"][0]
    assert item["amount"] == {"value": "100.00", "currency": "USD"} and item["receiver"] == "merchant@sandbox.example"
    assert seen["auth"] == "Bearer tok" and c.available_balance == 100_000 - 37_500


def test_declines_cleanly(configured, monkeypatch):
    def post(url, **kw):
        if url.endswith("/oauth2/token"):
            return R(200, {"access_token": "tok", "expires_in": 300})
        return R(422, {"name": "VALIDATION_ERROR", "message": "Receiver not found"})

    monkeypatch.setattr(httpx, "post", post)
    c = card()
    res = get_adapter("paypal").authorize(c, 1000, "Canva", "x")
    assert not res.ok and "Receiver not found" in res.decline_reason and c.available_balance == 100_000
    assert not get_adapter("paypal").authorize(card(500), 1000, "Canva", "x").ok  # insufficient funds, no PayPal call


def test_unconfigured_declines_without_network(monkeypatch):
    s = get_settings()
    monkeypatch.setattr(s, "paypal_client_id", None)
    monkeypatch.setattr(httpx, "post", lambda *a, **k: (_ for _ in ()).throw(AssertionError("no network")))
    res = get_adapter("paypal").authorize(card(), 1000, "Canva", "x")
    assert not res.ok and "not configured" in res.decline_reason


def test_full_flow_agent_request_to_paypal_payout(monkeypatch):
    """Agent asks, Flaire approves, PayPal sandbox is paid; a denied request never reaches PayPal."""
    import os
    os.environ["AUTH_ENGINE"] = "native"
    from fastapi.testclient import TestClient
    from app.core.db import Base, engine
    from app.main import app

    from app.integrations.shotoku.receipts import reset_spent
    reset_spent()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    s = get_settings()
    monkeypatch.setattr(s, "paypal_client_id", "cid")
    monkeypatch.setattr(s, "paypal_client_secret", "sec")
    monkeypatch.setattr(s, "paypal_receiver_email", "merchant@sandbox.example")
    pp._token.update({"value": None, "exp": 0})
    calls = []

    def post(url, **kw):
        calls.append(url)
        if url.endswith("/oauth2/token"):
            return R(200, {"access_token": "tok", "expires_in": 300})
        return R(201, {"batch_header": {"payout_batch_id": "PB999", "batch_status": "PENDING"}})

    monkeypatch.setattr(httpx, "post", post)
    c = TestClient(app)
    r = c.post("/api/v1/auth/register", json={"company_name": "PPCo", "email": "pp@test.sa", "password": "password123", "full_name": "PP"})
    H = {"Authorization": f"Bearer {r.json()['access_token']}"}
    c.patch("/api/v1/company", json={"trusted_merchants": ["Canva"]}, headers=H)
    dept = c.post("/api/v1/departments", json={"name": "Marketing", "monthly_budget": 500_000}, headers=H).json()
    ag = c.post("/api/v1/agents", json={"name": "AI", "role": "marketing", "department_id": dept["id"], "per_transaction_limit": 100_000, "monthly_limit": 400_000,
                                        "approval_threshold": 100_000, "allowed_categories": ["software"], "blocked_merchants": ["Gift card"], "max_requests_per_hour": 50}, headers=H).json()
    A = {"X-Agent-Key": ag["api_key"]}
    assert ag["agent"]["card"]["provider"] == "paypal"
    pr = c.post("/api/v1/agent/purchase-requests", json={"amount": 37_500, "merchant": "Canva", "category": "software", "description": "Design plan"}, headers=A).json()
    assert pr["status"] == "completed"
    tx = c.get(f"/api/v1/transactions/{pr['transaction_id']}", headers=H).json()
    assert tx["provider"] == "paypal" and tx["provider_ref"] == "paypal_PB999" and tx["issuer_currency"] == "USD" and tx["issuer_amount"] == 10_000
    n = len(calls)
    bad = c.post("/api/v1/agent/purchase-requests", json={"amount": 5_000, "merchant": "Gift card", "category": "software", "description": "x"}, headers=A).json()
    assert bad["status"] == "denied" and len(calls) == n  # blocked by Flaire, PayPal never called


def _boot(monkeypatch, email="life@test.sa"):
    import os
    os.environ["AUTH_ENGINE"] = "native"
    from fastapi.testclient import TestClient
    from app.core.db import Base, engine
    from app.main import app
    from app.integrations.shotoku.receipts import reset_spent
    reset_spent()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    s = get_settings()
    monkeypatch.setattr(s, "paypal_client_id", "cid")
    monkeypatch.setattr(s, "paypal_client_secret", "sec")
    monkeypatch.setattr(s, "paypal_receiver_email", "merchant@sandbox.example")
    pp._token.update({"value": None, "exp": 0})
    state = {"items": "PENDING", "batch": "PENDING"}

    def post(url, **kw):
        if url.endswith("/oauth2/token"):
            return R(200, {"access_token": "tok", "expires_in": 300, "scope": "https://uri.paypal.com/services/payments/payouts"})
        return R(201, {"batch_header": {"payout_batch_id": "PBL1", "batch_status": "PENDING"}})

    def get(url, **kw):
        return R(200, {"batch_header": {"payout_batch_id": "PBL1", "batch_status": state["batch"]}, "items": [{"transaction_status": state["items"]}]})
        
    monkeypatch.setattr(httpx, "post", post)
    monkeypatch.setattr(httpx, "get", get)
    c = TestClient(app)
    r = c.post("/api/v1/auth/register", json={"company_name": "Life", "email": email, "password": "password123", "full_name": "L"})
    H = {"Authorization": f"Bearer {r.json()['access_token']}"}
    c.patch("/api/v1/company", json={"trusted_merchants": ["Canva"]}, headers=H)
    dept = c.post("/api/v1/departments", json={"name": "Marketing", "monthly_budget": 500_000}, headers=H).json()
    ag = c.post("/api/v1/agents", json={"name": "AI", "role": "marketing", "department_id": dept["id"], "per_transaction_limit": 100_000, "monthly_limit": 400_000,
                                        "approval_threshold": 100_000, "allowed_categories": ["software"], "blocked_merchants": [], "max_requests_per_hour": 50}, headers=H).json()
    A = {"X-Agent-Key": ag["api_key"]}
    pr = c.post("/api/v1/agent/purchase-requests", json={"amount": 37_500, "merchant": "Canva", "category": "software", "description": "Plan"}, headers=A).json()
    assert pr["status"] == "completed", pr["decision"]
    return c, H, A, ag, pr, state


def test_payout_pending_then_settles(monkeypatch):
    c, H, A, ag, pr, state = _boot(monkeypatch)
    assert pr["status"] == "completed"
    tx = c.get(f"/api/v1/transactions/{pr['transaction_id']}", headers=H).json()
    assert tx["status"] == "authorized"  # PayPal still PENDING
    state.update(items="SUCCESS", batch="SUCCESS")
    tx = c.get(f"/api/v1/transactions/{pr['transaction_id']}", headers=H).json()
    assert tx["status"] == "settled"


def test_failed_payout_is_reversed_and_budget_returns(monkeypatch):
    c, H, A, ag, pr, state = _boot(monkeypatch, "fail@test.sa")
    assert c.get("/api/v1/cards", headers=H).json()[0]["available_balance"] == 400_000 - 37_500
    state.update(items="FAILED", batch="DENIED")
    txs = c.get("/api/v1/transactions", headers=H).json()
    assert txs[0]["status"] == "reversed"
    assert c.get("/api/v1/cards", headers=H).json()[0]["available_balance"] == 400_000
    assert c.get(f"/api/v1/agents/{ag['agent']['id']}", headers=H).json()["spent_this_period"] == 0


def test_webhook_asks_paypal_and_ignores_forged_claims(monkeypatch):
    c, H, A, ag, pr, state = _boot(monkeypatch, "hook@test.sa")
    forged = {"id": "WH-1", "event_type": "PAYMENT.PAYOUTSBATCH.SUCCESS", "resource": {"batch_header": {"payout_batch_id": "PBL1", "batch_status": "SUCCESS"}}}
    r = c.post("/api/v1/webhooks/paypal", json=forged).json()
    assert r["matched_transaction"] == pr["transaction_id"] and r["status"] == "authorized"  # PayPal itself still says PENDING
    state.update(items="SUCCESS", batch="SUCCESS")
    forged["id"] = "WH-2"
    assert c.post("/api/v1/webhooks/paypal", json=forged).json()["status"] == "settled"
    assert c.post("/api/v1/webhooks/paypal", json=forged).json().get("duplicate") is True


def test_connection_check(monkeypatch):
    c, H, A, ag, pr, state = _boot(monkeypatch, "conn@test.sa")
    r = c.post("/api/v1/paypal/test", headers=H).json()
    assert r["ok"] and r["sandbox"] and r["receiver_set"] and r["payouts_enabled"] is True

# Demo video script (target 2:50, hard limit 3:00)

Rules: under 3 minutes, public on YouTube, shows the project working, no third party logos or copyrighted music. No music is safest. Made-up merchants only (Acme Design, Northwind Software, Blueline Media).

Criteria this hits: Technological Implementation (PayPal Payouts, Orders, webhooks), Design (clean dashboard), Potential Impact (the problem and the money), Innovation (a rule layer for AI spending with a human approving inside PayPal), Presentation (three flows, no dead air).

Prize categories for Devpost: Best Use of Agentic Commerce, Best Use of PayPal + AI, Best Use of Render, Most Impactful, Most Creative, Best Demo Delivery.

## Before you record (30 minutes)

1. Wake the API 2 minutes before: open https://flaire-api-cmrs.onrender.com/api/v1/health.
2. Controls, trusted merchants: add Acme Design, Northwind Software, Blueline Media (so the new-supplier review does not interfere).
3. Check the AI employee's limits (AI workforce, Edit): per purchase at least $267, approval threshold BELOW $200 (new accounts default to $133), monthly $2,667 or more. If your threshold equals the per purchase limit, the $200 request will not wait for approval.
4. Do one full rehearsal with the same three prompts. The recording is take two.
5. Browser 1920x1080, zoom 110 percent, one window per tab, close everything else, hide bookmarks, Do Not Disturb on, phone notifications off.
6. Tabs in order: ChatGPT, Flaire Spending, Flaire Approvals, PayPal sandbox merchant Activity (merchant@flaire.com), and a PRIVATE window for the approver so the PayPal login shows.
7. Prompts in a notes file (paste, do not type):
   - Use Flaire to pay $100 to Acme Design for the completed logo design job.
   - Use Flaire to pay $200 to Northwind Software for the website build milestone.
   - Use Flaire to pay $320 to Blueline Media for an ad package.

## Final script (target 2:45, hard limit 3:00)

Prize targets and where the video earns each: Best Use of Agentic Commerce (the agent pays inside a policy), Best Use of PayPal + AI (Payouts and Orders driven by ChatGPT), Best Demo Delivery (three proofs, measured time, no dead air), Render (named once). Honest framing is on screen at the start and the end.

**0:00 to 0:25 The problem**
[Black screen, white text, one line at a time: "Illustrative team: 100 AI agent payments a month." "5 minutes to check each one." "8 hours 20 minutes of review. Every month." "Or open access, and no control." Small source line at the bottom: "Checkout.com, Agentic Commerce 2026: 400 payments leaders, 12,000+ consumers." Then cut to the Flaire logo.]
"Consider a team whose AI agents request 100 routine payments a month. Five minutes to check each one is over eight hours of human review, and the agent waits on every answer. Or the agent gets open access, and finance loses control. Checkout.com's 2026 report says three in four payments leaders need to revoke an agent's permission instantly. That is the gap."

**0:25 to 0:32 Title**
[Flaire logo with the line: "Agentic commerce with a spending policy. Built on PayPal."]
"This is Flaire. Agentic commerce, with a spending policy, built on PayPal."

**0:32 to 1:02 Proof 1: inside the rules**
[ChatGPT with prompt 1, press send. The answer. Flaire Spending, Acme Design $100, the PayPal panel. A stopwatch overlay: "Request to payout: N seconds" (use your real measured number). PayPal merchant Activity: "$100.00 Completed".]
"My AI employee lives in ChatGPT. A contractor finishes a job, and it pays 100 dollars. Flaire checks the agent's budget, its per payment limit and whether the payee is trusted. All inside the rules, so it pays through the PayPal Payouts API, no human needed. Request to payout, N seconds. And it lands in PayPal."

**1:02 to 1:50 Proof 2: above the limit, a human approves inside PayPal**
[Prompt 2. ChatGPT says it is waiting. Approvals: "$200 Northwind Software, waiting". Overlay: "The AI cannot approve itself". Approve, password. Private window: PayPal login as the approver, checkout $200.00, Pay. Return page. Merchant Activity $200.00.]
"Now 200 dollars, above this agent's limit. Flaire stops. ChatGPT has no approve button. A person approves in Flaire. Then Flaire hands off to PayPal Orders, where that person approves again with their own PayPal login, and PayPal moves the money. Small payments run alone. Big ones need a human. And PayPal is the final authority."

**1:50 to 2:12 Proof 3: stopped**
[Prompt 3. ChatGPT says denied. A red "Blocked" row with its reason. Overlay: "Denied before PayPal was called". Kill switch on (frozen banner), then off.]
"Now 320 dollars, over the limit. Denied before PayPal is ever called, and recorded in an audit log. And one switch freezes every agent."

**2:12 to 2:35 Engineering**
[Connections, "Test PayPal connection", green message. Then 3 seconds of the GitHub README showing "113 tests".]
"Real engineering, not a mockup. PayPal OAuth, Payouts with idempotency keys so a retry never pays twice, Orders for human approval, and webhooks Flaire re-verifies with PayPal. Any ChatGPT or Claude agent connects over MCP, and the API runs on Render. 113 automated tests."

**2:35 to 2:50 Close**
[Overview dashboard, held still. Optional face circle bottom right. End card: logo, flaire-paypal.vercel.app, github.com/itsmaryaamm/flaire-paypal, "PayPal sandbox. No real money moves."]
"Everything you saw runs in the PayPal sandbox, paid to a sandbox merchant. Next: live accounts, and a pilot to measure how much review time teams really save. Flaire. Let AI spend, with a human in charge."

## Recording technique

- Record the voice over separately after the screen, on your phone voice memo 15 cm from your mouth in a small quiet room (wardrobe or car). A clean voice matters more than anything.
- Record each flow as its own clip (OBS or Win+G, 1080p, 30 fps) so you can retake one.
- Edit in Clipchamp or CapCut: cut dead air, speed waiting moments 2x, zoom 120 percent on the amount and the PayPal panel, burned in captions (many judges watch muted).
- Pause half a second after each key number. Do not say "um", "so basically" or "as you can see".
- Export 1080p MP4. YouTube Public, title: "Flaire: the finance department for AI employees, built on PayPal". Put the GitHub and live links in the description.
- Watch it once on your phone with the sound off.

## If you run out of time

Cut "Under the hood" to one sentence. Never cut Flow 2, it is the strongest moment.

## Feature freeze rule

If a feature is not in this script, do not build it before the deadline. Only fixes that keep the three flows working are allowed.

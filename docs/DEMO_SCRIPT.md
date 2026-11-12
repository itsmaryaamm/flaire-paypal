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

## Strategy for the 3 minutes

Judges know PayPal and have seen "an AI agent pays with PayPal" many times. We do not win by showing that an agent can pay. We win by showing the missing layer: who lets an agent spend, how much, who approves, who can stop it. PayPal's own idea list (agents that pay contractors when a job is complete, agents that settle with other agents, agentic checkout) all assume the agent is allowed to move money. Flaire is the permission and control layer that makes those ideas safe for a real finance team, built natively on PayPal Payouts and Orders.

Time budget: 20 seconds thesis (earns the next 2 minutes), 90 seconds of live proof, 25 seconds of engineering credibility, 20 seconds of why it matters.

## Script (about 400 words, target 2:50)

**0:00 to 0:20 Thesis**
[Black screen. One white line at a time, 2 seconds each: "Agents that pay contractors when a job is done." "Agents that settle payments with other agents." "Agents that check out for you." Then: "All of them need one thing first." Then large: "Permission." Cut to ChatGPT with prompt 1 pasted.]
"PayPal's own idea list has AI agents paying contractors, settling with other agents, checking out for you. Not recommending, transacting. But every one of them needs an answer nobody has solved. Who gave the agent permission to spend, how much, and who can stop it?"

**0:20 to 0:28 Title**
[Flaire logo with the line: "The permission layer for AI agents that move money. Built on PayPal."]
"This is Flaire."

**0:28 to 1:00 Proof 1: a job is complete, the agent pays**
[Press send on prompt 1. ChatGPT answers. Spending, the Acme Design $100 row, the PayPal panel. Then PayPal merchant Activity: "$100.00 Completed". Overlay: "Inside the rules: PayPal Payouts, no human needed".]
"A job is marked complete. My AI employee in ChatGPT pays the contractor 100 dollars. Flaire first checks that employee's budget, its per payment limit and whether the payee is trusted. All inside the rules, so Flaire pays through the PayPal Payouts API. And it lands in PayPal."

**1:00 to 1:50 Proof 2: a bigger payment, a human approves inside PayPal**
[Send prompt 2. ChatGPT says it is waiting. Approvals: "$200 Northwind Software, waiting". Overlay: "The AI cannot approve itself". Approve, password. Private window: PayPal login as the approver, checkout $200.00, Pay. Return page. Merchant Activity $200.00.]
"Now 200 dollars. A shared card or an open API key would just send it. Flaire stops, because this employee may not move that much alone. ChatGPT has no approve button. A person approves in Flaire. Then Flaire hands off to PayPal Orders, where that person approves again with their own PayPal login, and PayPal moves the money. Autonomy for small payments, a human for big ones, PayPal as the final authority."

**1:50 to 2:15 Proof 3: an agent that goes too far**
[Send prompt 3. ChatGPT says denied. Spending: red "Blocked" row, open it to show the reason. Overlay: "Denied before PayPal was called". Toggle the kill switch on (frozen banner), then off.]
"Now an agent that goes too far. 320 dollars is over the limit, so it is denied before PayPal is ever called, and the decision is recorded in a tamper evident audit log. If anything looks wrong, one switch freezes every agent."

**2:15 to 2:35 Engineering credibility**
[Connections, "Test PayPal connection", green message. Then 3 seconds of the GitHub README showing "113 tests".]
"This is real engineering, not a mockup. PayPal OAuth, Payouts with idempotency keys so a retry never pays twice, Orders for human approval, and webhooks Flaire always re-verifies with PayPal. If PayPal returns a payout, the budget is restored. 113 automated tests. Any ChatGPT or Claude agent connects over MCP, and the API runs on Render."

**2:35 to 2:55 Why it matters**
[Overview dashboard, held still. Optional face circle bottom right. End card: Flaire logo, flaire-paypal.vercel.app, github.com/itsmaryaamm/flaire-paypal, "PayPal sandbox. No real money moves."]
"Contractor payouts, agent to agent settlement, agentic checkout. They only reach real businesses when a finance team can trust them. Flaire is that trust layer, built on PayPal. Today it runs in the sandbox. Next, live accounts, and a small fee on the volume it governs. Flaire. Let AI spend, with a human in charge."

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

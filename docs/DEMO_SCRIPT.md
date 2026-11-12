# Demo video script (target 2:50, hard limit 3:00)

Rules: under 3 minutes, public on YouTube, shows the project working, no third party logos or copyrighted music. No music is safest. Made-up merchants only (Acme Design, Northwind Software, Blueline Media).

Criteria this hits: Technological Implementation (PayPal Payouts, Orders, webhooks), Design (clean dashboard), Potential Impact (the problem and the money), Innovation (a rule layer for AI spending with a human approving inside PayPal), Presentation (three flows, no dead air).

Prize categories for Devpost: Best Use of Agentic Commerce, Best Use of PayPal + AI, Best Use of Render, Most Impactful, Most Creative, Best Demo Delivery.

## Before you record (30 minutes)

1. Wake the API 2 minutes before: open https://flaire-api-cmrs.onrender.com/api/v1/health.
2. Controls, trusted merchants: add Acme Design, Northwind Software, Blueline Media (so the new-supplier review does not interfere).
3. The ChatGPT employee limits: $267 per purchase, approval from $133, monthly $2,667 (the defaults). Do not change them.
4. Do one full rehearsal with the same three prompts. The recording is take two.
5. Browser 1920x1080, zoom 110 percent, one window per tab, close everything else, hide bookmarks, Do Not Disturb on, phone notifications off.
6. Tabs in order: ChatGPT, Flaire Spending, Flaire Approvals, PayPal sandbox merchant Activity (merchant@flaire.com), and a PRIVATE window for the approver so the PayPal login shows.
7. Prompts in a notes file (paste, do not type):
   - Use Flaire to request a purchase of $100 from Acme Design for a team workspace.
   - Use Flaire to request a purchase of $200 from Northwind Software for a design license.
   - Use Flaire to request a purchase of $320 from Blueline Media for an ad package.

## Script (about 380 words)

**0:00 to 0:12 Hook.** Screen: ChatGPT with the first prompt pasted. Press send as you start.
"AI agents are starting to buy things. Today that means a shared company card and hope. No budget, no approval, no off switch. This is Flaire, the finance department for AI employees, and every payment goes through PayPal."

**0:12 to 0:50 Flow 1, within the rules.** Screen: ChatGPT answers, then Flaire Spending, open the row, show the PayPal panel, then the PayPal merchant Activity (refresh).
"My AI employee lives in ChatGPT. I ask for a 100 dollar workspace. Flaire checks its budget, its per purchase limit and the supplier. All inside the rules, so Flaire pays through the PayPal Payouts API. And here it is in PayPal. 100 dollars, received."

**0:50 to 1:40 Flow 2, a human approves in PayPal.** Screen: ChatGPT with the second prompt, Flaire Approvals, Approve, password, PayPal login in the private window, Pay, return page, merchant Activity.
"Now 200 dollars. On a shared card this just goes through. Here it is above this employee's approval limit, so Flaire stops and asks a person. The AI cannot approve its own spending. I approve in Flaire with my password. Then Flaire sends me to PayPal, where I approve again with my own PayPal login. PayPal Orders moves the money. Two approvals, and the merchant is paid."

**1:40 to 2:05 Flow 3, blocked.** Screen: ChatGPT with the third prompt, the denial, Spending list showing the blocked row, kill switch on then off.
"Now a request that breaks the rules. 320 dollars is over the limit, so it is denied before PayPal is ever called. And one kill switch freezes every AI employee at once."

**2:05 to 2:25 Under the hood.** Screen: Connections, press Test PayPal connection, green message.
"Under the hood: PayPal OAuth, Payouts with idempotency keys so a retry never pays twice, Orders for approval, and webhooks that Flaire never trusts without asking PayPal again. If PayPal returns a payout, the budget is given back. Any ChatGPT or Claude agent connects over MCP, and the API runs on Render."

**2:25 to 2:45 Impact and honesty.** Screen: Flaire Overview.
"Every company that lets agents spend has this problem, and today the answer is a shared card. Flaire earns a small fee on what it governs. Everything here runs in the PayPal sandbox, no real money moves. Next is live PayPal accounts. Flaire: let AI spend, with a human in charge."

End card, 3 seconds, plain text: flaire-paypal.vercel.app

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

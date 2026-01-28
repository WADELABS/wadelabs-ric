# Lead Magnet Flow: The "Integrity Teaser"

## 1. The Hook (Landing Page)
**URL:** `wadelabs.ai/checkup`
**Promise:** "Run a free 60-second integrity check on your Login/Logout flow."
**Input:**
*   URL (e.g., `staging.myapp.com`)
*   Test User Credentials (optional, or generic)

## 2. The Mechanics (Automated)
Upon submission, `wade-ric` triggers a **"Lite" Scan** (RIC-01 Only):
1.  Navigates to URL.
2.  Logs in.
3.  Captures Session Token.
4.  Logs out.
5.  **Replays Session Token** against `/user/settings` or similar.

## 3. The Hook (The Result)
If it FAILS (Token works after logout), user gets an email:

> **Subject:** Integrity Alert: Session Issue on staging.myapp.com
>
> We ran the check.
> **Result:** FAIL.
>
> Your session token remained active for privileged actions after logout.
>
> [**View Proof (Trace)**](#)
>
> This is exactly what RIC prevents weekly.
> **[Enable Weekly Monitoring - $499/mo]**

If it PASSES:
> **Subject:** Integrity Check Passed
>
> Logout logic looks solid.
> What about Double-Charge races or Role Boundaries?
>
> **[Run Full Suite - $499/mo]**

## 4. The Funnel
*   **Top:** Free RIC-01 Scan.
*   **Middle:** PDF Proof ("Case File") delivered.
*   **Bottom:** Stripe Checkout for recurring full suite.

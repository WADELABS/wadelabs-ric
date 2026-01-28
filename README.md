# Wadelabs Release Integrity Check (RIC)

### **Release Integrity Checks That Catch What Scanners Miss.**

**Wadelabs RIC** is an automated regression engine that verifies the **5 mathematical guarantees** that must never break in a SaaS application. It focuses on session integrity, workflow invariants, and authorization boundaries—areas where standard scanners fail.

---

## 🚨 The "Friday Deploy" Problem

Most security tools check for CVEs or misconfigurations. They don't check **logic state**.
When you ship a release, do you know if:
*   Your logout actually invalidates the session on the server?
*   your "Free Tier" users can access "Pro" exports?
*   Clicking "Pay" twice triggers a double charge?

RIC answers these questions with **reproducible evidence** (Playwright traces & HAR logs) every single run.

---

## 🛡️ The 5 Signature Checks

| ID | Check Name | Why It Matters |
| :--- | :--- | :--- |
| **RIC-01** | **Logout Reality** | A valid token after logout is a permanent backdoor. |
| **RIC-02** | **Multi-Tab Double-Action** | Race conditions in billing cost real money. |
| **RIC-03** | **Role Boundary** | Admin features must be mathematically unreachable by users. |
| **RIC-04** | **Data Export Leak** | Predictable IDs (IDOR) on exports cause massive leaks. |
| **RIC-05** | **Sensitive Step-Up** | Critical actions (Pass Change) must require re-auth. |

*(Plus **RIC-06 Integrity Drift**: Alerts you when a new regression is introduced vs previous run.)*

---

## 📦 Usage (CLI)

RIC is designed to run in your CI/CD pipeline or as a pre-release gate.

### Installation
```bash
pip install wadelabs-ric
```

### Run a Standard Check
```bash
wade-ric --target staging --policy commercial_audit
```

### Detect Drift (Regression Check)
Compare the current run against a previous baseline to see *exactly* what broke this release.
```bash
wade-ric --target staging --baseline last_run.json > current_run.json
```

---

## 📄 The Output: Integrity Snapshot

The CLI produces a JSON report and (optionally) a Human-Readable Snapshot.

**Sample Output:**
```json
{
  "check_id": "RIC-01",
  "status": "FAIL",
  "summary": "Token reusable 45s after logout.",
  "evidence": ["trace_logout.zip"],
  "control_map": {"OWASP_ASVS": ["V3.4.1"]}
}
```

---

## 💼 Commercial & Support

**Wadelabs RIC** is maintained by **Integrity Engineering**.
We offer:
*   **Managed Weekly Monitoring**: We run the checks, analyze the traces, and send you the **Integrity Snapshot**.
*   **Pressure Suite™**: Advanced testing under network latency, retry storms, and outage simulation.

[**Run Your First Integrity Check**](https://wadelabs.ai/checkup)

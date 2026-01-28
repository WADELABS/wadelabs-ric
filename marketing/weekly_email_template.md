Subject: Wadelabs Integrity Snapshot: {{ target }} ({{ timestamp }})

**Integrity Score:** {{ passed_count }}/{{ total_count }} Passed
**Regression Status:** {{ regression_status }}

---

### 🚨 Critical Findings (Action Required)

{% if failing_checks %}
The following invariants FAILED in this release:

{% for f in failing_checks %}
**❌ {{ f.check_name }}**
*   **Impact:** {{ f.description }}
*   **Evidence:** attached `{{ f.evidence[0].filename }}`
*   **Fix Priority:** P0 (Critical)
{% endfor %}

{% else %}
✅ All systems nominal. No logic regressions detected.
{% endif %}

---

### 📉 Drift Radar
*Compared to run {{ base_run_id }}*

*   **New Regressions:** {{ regressions_count }}
*   **Fixes Verified:** {{ fixes_count }}

---

**Next Steps:**
1.  Review attached Playwright traces for failed checks.
2.  Patch logic gaps (see standard `OWASP ASVS` mappings in report).
3.  Reply to schedule a re-test.

*Confident execution.*
**Wadelabs Integrity Engineering**

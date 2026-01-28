from __future__ import annotations
import uuid
import yaml
from datetime import datetime, timezone
from pathlib import Path
import sys
import json
import argparse

# Use relative imports since this is now inside the package
from .models import IntegrityReport, Finding
from .drift import compare_runs

def load_policy(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Policy not found: {path}")
    return yaml.safe_load(p.read_text(encoding="utf-8"))

def run_signature_checks(policy: dict, target: str) -> IntegrityReport:
    run_id = str(uuid.uuid4())
    timestamp_utc = datetime.now(timezone.utc).isoformat()

    findings: list[Finding] = []
    for check in policy.get("signature_checks", []):
        findings.append(
            Finding(
                check_id=check["id"],
                check_name=check["name"],
                status="PENDING",
                severity=check.get("severity_default", "medium"),
                summary=f"{check['name']} not executed (runner v0).",
                details="This is a placeholder until Playwright/API harness is wired in.",
                evidence=[],
                control_map=check.get("control_mapping", {}),
            )
        )

    return IntegrityReport(
        target=target,
        run_id=run_id,
        timestamp_utc=timestamp_utc,
        findings=findings,
        gaps={},
    )

def main() -> None:
    parser = argparse.ArgumentParser(description="Wadelabs RIC integrity runner (v1.2)")
    # Policy is now expected to be in the package: wadelabs_ric/policy/qa_integrity_policy.yaml
    default_policy = Path(__file__).parent / "policy" / "qa_integrity_policy.yaml"
    
    parser.add_argument("--policy", default=str(default_policy))
    parser.add_argument("--target", default="local-sandbox")
    parser.add_argument("--baseline", help="Path to previous run JSON for drift analysis", default=None)
    
    args = parser.parse_args()

    try:
        policy = load_policy(args.policy)
    except FileNotFoundError:
        print(f"Error: Policy file not found at {args.policy}", file=sys.stderr)
        sys.exit(1)

    report = run_signature_checks(policy, args.target)

    # Drift Analysis
    if args.baseline:
        try:
            with open(args.baseline, 'r') as f:
                base_data = json.load(f)
            
            # Reconstruct Finding objects for baseline
            base_findings = [Finding(**f) for f in base_data.get('findings', [])]
            base_report = IntegrityReport(
                target=base_data.get('target', 'unknown'),
                run_id=base_data.get('run_id', 'unknown'),
                timestamp_utc=base_data.get('timestamp_utc', ''),
                findings=base_findings
            )
            
            drift = compare_runs(base_report, report)
            
            # Inject RIC-06 Result
            for f in report.findings:
                if f.check_id == "RIC-06":
                    if drift.regressions_count > 0:
                        f.status = "FAIL"
                        f.summary = f"CRITICAL: {drift.regressions_count} Regression(s) Detected."
                    else:
                        f.status = "PASS"
                        f.summary = "No regressions detected."
                    f.details = f"Fixes: {drift.fixes_count}. New: {len([d for d in drift.deltas if d.change_type=='NEW'])}."
                    break

        except Exception as e:
            print(f"Drift Analysis Failed: {e}", file=sys.stderr)

    print(json.dumps(report, default=lambda o: o.__dict__, indent=2))

if __name__ == "__main__":
    main()

import sys
from pathlib import Path
# Add project root to sys.path
sys.path.append(str(Path(__file__).parent.parent))

from wadelabs_ric.integrity_runner import load_policy, run_signature_checks

def test_runner_emits_pending_findings():
    policy_path = Path(__file__).parent.parent / "policy" / "qa_integrity_policy.yaml"
    policy = load_policy(str(policy_path))
    report = run_signature_checks(policy, target="demo")
    assert len(report.findings) == 5
    assert all(f.status == "PENDING" for f in report.findings)

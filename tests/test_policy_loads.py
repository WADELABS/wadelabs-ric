import sys
from pathlib import Path
# Add project root to sys.path
sys.path.append(str(Path(__file__).parent.parent))

from wadelabs_ric.integrity_runner import load_policy

def test_policy_loads():
    policy_path = Path(__file__).parent.parent / "policy" / "qa_integrity_policy.yaml"
    policy = load_policy(str(policy_path))
    assert policy["product"].startswith("Wadelabs")
    assert len(policy["signature_checks"]) == 5

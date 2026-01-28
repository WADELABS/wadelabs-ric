from __future__ import annotations
from pathlib import Path
from typing import Iterable

REQUIRED_EVIDENCE_KINDS = {
    "playwright_trace",
    "network_log",
    "assertion_log",
    "request_response_samples",
    "artifact_hashes",
}

def ensure_paths_exist(paths: Iterable[str]) -> None:
    missing = [p for p in paths if p and not Path(p).exists()]
    if missing:
        raise FileNotFoundError(f"Missing evidence files: {missing}")

def evidence_is_sufficient(required_kinds: list[str], provided_kinds: list[str]) -> bool:
    # All required must be present
    return all(k in provided_kinds for k in required_kinds)

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal, Optional, Dict, List

Severity = Literal["info", "low", "medium", "high", "critical"]
Status = Literal["PASS", "FAIL", "PENDING", "UNKNOWN", "ERROR"]
GapType = Literal["telemetry_gap", "observability_gap", "process_integrity_gap"]

@dataclass
class Evidence:
    kind: str
    path: str
    note: Optional[str] = None

@dataclass
class Finding:
    check_id: str
    check_name: str
    status: Status
    severity: Severity
    summary: str
    details: str = ""
    evidence: List[Evidence] = field(default_factory=list)
    control_map: Dict[str, List[str]] = field(default_factory=dict)  # e.g., {"OWASP_ASVS": ["V3.2.1"]}

@dataclass
class IntegrityReport:
    target: str
    run_id: str
    timestamp_utc: str
    findings: List[Finding]
    gaps: Dict[GapType, List[str]] = field(default_factory=dict)

@dataclass
class FindingDelta:
    check_id: str
    check_name: str
    previous_status: Optional[Status]
    current_status: Status
    change_type: Literal["REGRESSION", "FIX", "STABLE", "NEW", "REMOVED"]

@dataclass
class DriftReport:
    base_run_id: str
    current_run_id: str
    deltas: List[FindingDelta]
    regressions_count: int
    fixes_count: int

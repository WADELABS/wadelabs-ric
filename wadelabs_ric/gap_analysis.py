from __future__ import annotations
from typing import Dict, List, Any
from .models import GapType

def analyze_system_integrity_gaps(
    telemetry: Dict[str, Any],
    expectations: Dict[str, Any],
) -> Dict[GapType, List[str]]:
    """
    telemetry: what we observed (logs, traces, events, scans)
    expectations: what we expect to exist (controls, logging, process)
    """
    gaps: Dict[GapType, List[str]] = {
        "telemetry_gap": [],
        "observability_gap": [],
        "process_integrity_gap": [],
    }

    # Telemetry gaps: expected signals are missing
    required_signals = expectations.get("required_signals", [])
    observed_signals = set(telemetry.get("signals_present", []))
    for s in required_signals:
        if s not in observed_signals:
            gaps["telemetry_gap"].append(f"Missing required signal: {s}")

    # Observability gaps: failures cannot be traced to root cause
    if expectations.get("require_trace_artifacts", True) and not telemetry.get("has_trace", False):
        gaps["observability_gap"].append("No trace artifacts available for replayable debugging.")

    # Process integrity gaps: changes lack approvals/audit trail
    if expectations.get("require_change_ticket", False) and not telemetry.get("has_change_ticket", False):
        gaps["process_integrity_gap"].append("No change ticket associated with the tested release.")

    return gaps

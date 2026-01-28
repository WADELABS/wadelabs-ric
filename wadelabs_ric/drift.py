from __future__ import annotations
from typing import List, Dict, Optional
from .models import IntegrityReport, DriftReport, FindingDelta, Finding

def compare_runs(baseline: IntegrityReport, current: IntegrityReport) -> DriftReport:
    """
    Compares two integrity reports to generate a DriftReport.
    """
    base_map: Dict[str, Finding] = {f.check_id: f for f in baseline.findings}
    curr_map: Dict[str, Finding] = {f.check_id: f for f in current.findings}
    
    deltas: List[FindingDelta] = []
    
    all_ids = set(base_map.keys()) | set(curr_map.keys())
    
    regressions = 0
    fixes = 0
    
    for check_id in all_ids:
        base_f = base_map.get(check_id)
        curr_f = curr_map.get(check_id)
        
        # Determine Statuses
        prev_status = base_f.status if base_f else None
        curr_status = curr_f.status if curr_f else None
        
        name = curr_f.check_name if curr_f else base_f.check_name
        
        # Determine Change Type
        if not base_f and curr_f:
            c_type = "NEW"
        elif base_f and not curr_f:
            c_type = "REMOVED"
            curr_status = "UNKNOWN" # Or handled differently
        elif prev_status == "PASS" and curr_status == "FAIL":
            c_type = "REGRESSION"
            regressions += 1
        elif prev_status == "FAIL" and curr_status == "PASS":
            c_type = "FIX"
            fixes += 1
        elif prev_status != curr_status:
             c_type = "STABLE" # Changed but not Regression/Fix
             pass
        else:
            c_type = "STABLE"

        deltas.append(FindingDelta(
            check_id=check_id,
            check_name=name,
            previous_status=prev_status,
            current_status=curr_status,
            change_type=c_type
        ))
        
    return DriftReport(
        base_run_id=baseline.run_id,
        current_run_id=current.run_id,
        deltas=deltas,
        regressions_count=regressions,
        fixes_count=fixes
    )

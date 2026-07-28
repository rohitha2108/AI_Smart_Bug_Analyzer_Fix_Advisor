import json
import os
from triage_agent import triage_bug
from log_analysis_agent import analyze_log
from root_cause_agent import find_root_cause
from duplicate_detection_agent import detect_duplicates
from remediation_agent import recommend_fix
import json
import os

def run_analysis(description, error_log):

    triage_result = triage_bug(description)

    log_result = analyze_log(error_log)
    root_cause_result = find_root_cause(description)
    duplicate_result = detect_duplicates(description)
    remediation_result = recommend_fix(root_cause_result)

    combined_result = {
    "Triage Agent": triage_result,
    "Log Analysis Agent": log_result,
    "Root Cause Agent": root_cause_result,
    "Duplicate Detection Agent": duplicate_result,
    "Remediation Agent": remediation_result
}
    # Create outputs folder if it doesn't exist
    os.makedirs("outputs", exist_ok=True)

    # Save JSON file
    with open("outputs/result.json", "w") as f:
        json.dump(combined_result, f, indent=4)

    return combined_result
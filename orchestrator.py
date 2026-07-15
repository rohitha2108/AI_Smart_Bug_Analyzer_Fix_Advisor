import json
import os
from triage_agent import triage_bug
from log_analysis_agent import analyze_log
import json
import os

def run_analysis(description, error_log):

    triage_result = triage_bug(description)

    log_result = analyze_log(error_log)

    combined_result = {
        "Triage Agent": triage_result,
        "Log Analysis Agent": log_result
    }

    # Create outputs folder if it doesn't exist
    os.makedirs("outputs", exist_ok=True)

    # Save JSON file
    with open("outputs/result.json", "w") as f:
        json.dump(combined_result, f, indent=4)

    return combined_result
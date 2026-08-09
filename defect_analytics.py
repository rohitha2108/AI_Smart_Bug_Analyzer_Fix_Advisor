import json
import os
from collections import Counter

HISTORY_FILE = "outputs/bug_history.json"


def load_bug_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as f:
        return json.load(f)


def analyze_defect_patterns():

    bugs = load_bug_history()

    if not bugs:
        return {
            "total_bugs": 0,
            "severity_patterns": {},
            "component_patterns": {},
            "exception_patterns": {},
            "root_cause_patterns": {}
        }

    severity = Counter()
    components = Counter()
    exceptions = Counter()
    root_causes = Counter()

    for bug in bugs:

        severity[bug.get("Severity", "Unknown")] += 1
        components[bug.get("Component", "Unknown")] += 1
        exceptions[bug.get("Exception", "Unknown")] += 1
        root_causes[bug.get("Root Cause", "Unknown")] += 1

    return {
        "total_bugs": len(bugs),
        "severity_patterns": dict(severity),
        "component_patterns": dict(components),
        "exception_patterns": dict(exceptions),
        "root_cause_patterns": dict(root_causes)
    }
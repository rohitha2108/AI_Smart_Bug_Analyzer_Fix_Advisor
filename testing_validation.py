import json
import os


def validate_bug_history():

    history_file = "outputs/bug_history.json"

    result = {
        "total_bugs": 0,
        "minimum_five_bugs": False,
        "bugs": [],
        "all_fields_valid": False
    }

    # Check file exists
    if not os.path.exists(history_file):
        return result

    # Read bug history
    try:
        with open(history_file, "r") as f:
            bugs = json.load(f)
    except Exception:
        return result

    result["total_bugs"] = len(bugs)

    # Milestone requirement
    result["minimum_five_bugs"] = len(bugs) >= 5

    required_fields = [
        "Title",
        "Description",
        "Severity",
        "Priority",
        "Component",
        "Exception",
        "Failure Point",
        "Root Cause"
    ]

    all_valid = True

    for i, bug in enumerate(bugs):

        missing_fields = []

        for field in required_fields:

            if field not in bug:
                missing_fields.append(field)

        bug_result = {
            "Bug Number": i + 1,
            "Title": bug.get("Title", "Unknown"),
            "Status": "PASS" if not missing_fields else "FAIL",
            "Missing Fields": missing_fields
        }

        result["bugs"].append(bug_result)

        if missing_fields:
            all_valid = False

    result["all_fields_valid"] = all_valid

    return result
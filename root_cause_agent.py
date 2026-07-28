from search_bug import search_similar_bugs


def find_root_cause(bug_description):
    """
    Finds the probable root cause using similar historical bugs.
    """

    similar_bugs = search_similar_bugs(bug_description)

    evidence = similar_bugs[0] if len(similar_bugs) > 0 else "No historical evidence found."

    bug = bug_description.lower()

    if "nullpointerexception" in bug or "null pointer" in bug:
        root_cause = "Object was not initialized before use."
        confidence = 95

    elif "sql" in bug or "database" in bug:
        root_cause = "Database connection or query execution failure."
        confidence = 92

    elif "timeout" in bug:
        root_cause = "Server response timeout."
        confidence = 90

    elif "file" in bug:
        root_cause = "File path missing or file not found."
        confidence = 88

    elif "memory" in bug:
        root_cause = "Insufficient memory or memory leak."
        confidence = 87

    else:
        root_cause = "Possible application logic or configuration issue."
        confidence = 75

    return {
        "Root Cause": root_cause,
        "Confidence": confidence,
        "Evidence": evidence
    }
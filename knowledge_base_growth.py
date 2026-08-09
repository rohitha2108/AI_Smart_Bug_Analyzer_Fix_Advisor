import json
import os


KB_FILE = "outputs/resolved_bugs.json"


def add_resolved_bug(bug_data):
    """
    Add a bug with a confirmed fix to the knowledge base.
    """

    os.makedirs("outputs", exist_ok=True)

    # Load existing resolved bugs
    if os.path.exists(KB_FILE):
        try:
            with open(KB_FILE, "r", encoding="utf-8") as f:
                resolved_bugs = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            resolved_bugs = []
    else:
        resolved_bugs = []

    # Add new resolved bug
    resolved_bugs.append(bug_data)

    # Save updated knowledge base
    with open(KB_FILE, "w", encoding="utf-8") as f:
        json.dump(resolved_bugs, f, indent=4)

    return True


def get_resolved_bugs():
    """
    Retrieve all resolved bugs from the knowledge base.
    """

    if not os.path.exists(KB_FILE):
        return []

    try:
        with open(KB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
def triage_bug(description):

    description = description.lower()

    severity = "Low"
    priority = "Low"
    component = "General"

    if "crash" in description or "exception" in description:
        severity = "Critical"
        priority = "High"
        component = "Backend"

    elif "login" in description:
        severity = "High"
        priority = "High"
        component = "Authentication"

    elif "database" in description:
        severity = "High"
        priority = "Medium"
        component = "Database"

    elif "timeout" in description:
        severity = "Medium"
        priority = "Medium"
        component = "Network"

    elif "ui" in description or "button" in description:
        severity = "Low"
        priority = "Low"
        component = "Frontend"

    confidence = 90

    reasoning = f"Detected keywords related to {component}"

    return {
        "Severity": severity,
        "Priority": priority,
        "Component": component,
        "Confidence": confidence,
        "Reasoning": reasoning
    }
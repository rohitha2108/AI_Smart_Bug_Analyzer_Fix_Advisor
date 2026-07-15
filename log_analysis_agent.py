import re

def analyze_log(error_log):

    exception = "Unknown"
    failure_point = "Unknown"
    affected_code_path = "Unknown"

    # Detect Exception
    match = re.search(r'(\w+Exception)', error_log)

    if match:
        exception = match.group(1)

    # Detect File and Line Number
    file_match = re.search(r'at\s+([\w\.]+):(\d+)', error_log)

    if file_match:
        affected_code_path = file_match.group(1)
        failure_point = f"{file_match.group(1)}:{file_match.group(2)}"

    return {
        "Exception": exception,
        "Failure Point": failure_point,
        "Affected Code Path": affected_code_path
    }
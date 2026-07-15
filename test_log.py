from log_analysis_agent import analyze_log

log = """
java.lang.NullPointerException
at LoginService.java:45
"""

result = analyze_log(log)

print(result)
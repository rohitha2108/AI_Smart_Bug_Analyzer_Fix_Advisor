from orchestrator import run_analysis

description = "Application crashes during login"

error_log = """
java.lang.NullPointerException
at LoginService.java:45
"""

result = run_analysis(description, error_log)

print(result)
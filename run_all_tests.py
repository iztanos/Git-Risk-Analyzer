import os
from analyzer.risk_scoring import score_diff
from analyzer.output_renderer import render_report

def run_test(test_name, content):
    print(f"--- Running Test: {test_name} ---")
    report = score_diff(content)
    render_report(report)
    print("\\n" + "="*40 + "\\n")

if __name__ == "__main__":
    # Scenario 1: Low risk
    run_test("Low Risk Commit", "diff --git a/low_risk.py b/low_risk.py\\n--- a/low_risk.py\\n+++ b/low_risk.py\\n@@ -0,0 +1 @@\\n+print('Hello world')")

    # Scenario 2: Medium risk
    medium_risk_content = "diff --git a/medium_risk.py b/medium_risk.py\\n--- a/medium_risk.py\\n+++ b/medium_risk.py\\n@@ -0,0 +1,600 @@\\n"
    medium_risk_content += "\\n".join([f"+print('line {i}')" for i in range(600)])
    run_test("Medium Risk Commit", medium_risk_content)

    # Scenario 3: High risk
    run_test("High Risk Commit with Secret", "diff --git a/high_risk.py b/high_risk.py\\n--- a/high_risk.py\\n+++ b/high_risk.py\\n@@ -0,0 +1 @@\\n+api_key = 'FAKE_SECRET_456'")

    # Scenario 4: Critical risk
    run_test("Critical Risk Commit on .env file", "diff --git a/.env b/.env\\n--- a/.env\\n+++ b/.env\\n@@ -0,0 +1 @@\\n+SECRET_KEY=supersecret")

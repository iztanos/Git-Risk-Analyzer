import os
import subprocess
from dotenv import load_dotenv

def run_command(command, check=True):
    try:
        result = subprocess.run(
            command,
            check=check,
            text=True,
            capture_output=True,
            encoding='utf-8'
        )
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(e.stdout)
        print(e.stderr)
        return None

def create_and_analyze(filename, content, commit_message, branch_name):
    # Create a new branch
    run_command(["git", "checkout", "-b", branch_name])

    # Create the .env file
    with open('.env', 'w', encoding='utf-8') as f:
        f.write('OPENAI_API_KEY=dummy_key_for_testing\n')
    
    # Load the .env file
    load_dotenv()

    # Create the test file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Add and commit the test file
    run_command(["git", "add", filename])
    run_command(["git", "commit", "-m", commit_message])

    # Run the analysis
    print(f"--- Analyzing: {commit_message} ---")
    result = run_command(["python", "main.py", "HEAD"])
    if result:
        print(result.stdout)

    # Clean up the branch
    run_command(["git", "checkout", "main"])
    run_command(["git", "branch", "-D", branch_name])


if __name__ == "__main__":
    # Scenario 1: Low risk
    create_and_analyze("low_risk.py", "print('Hello world')", "Scenario 1: Low risk commit", "test-low-risk")

    # Scenario 2: Medium risk
    medium_risk_content = "\\n".join([f"print('line {i}')" for i in range(600)])
    create_and_analyze("medium_risk.py", medium_risk_content, "Scenario 2: Medium risk commit", "test-medium-risk")

    # Scenario 3: High risk
    create_and_analyze("high_risk.py", "api_key = 'FAKE_SECRET_456'", "Scenario 3: High risk commit with secret", "test-high-risk")

    # Scenario 4: Critical risk
    create_and_analyze("critical_risk.txt", "SECRET_KEY=supersecret", "Scenario 4: Critical risk commit on .env file", "test-critical-risk")

# Git Risk Analyzer

A Python tool that analyzes Git commits for security risks and potential issues using both rule-based analysis and AI-powered insights.

## Features

- **Git Diff Analysis**: Extracts and analyzes changes from specific commits
- **Risk Scoring**: Identifies potential security issues like exposed API keys, secrets, and large changes
- **AI-Powered Analysis**: Uses OpenAI for detailed security risk explanations
- **Rich Output**: Console output with color-coded risk levels




https://github.com/user-attachments/assets/c35d7ff5-d9b4-440a-aea6-91df3d755bcc

Example - Changes in the `.env` file

<img width="2032" height="212" alt="CritExmaple" src="https://github.com/user-attachments/assets/a202f9c9-ad7b-429d-a284-094a65a641ef" />











## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd git-risk-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key (optional, for AI analysis):
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

To analyze a specific commit, run:
```bash
python main.py <commit-hash>
```

To run the test suite, which simulates various risk scenarios, execute:
```bash
python run_all_tests.py
```
This will provide a summary of how the tool evaluates low, medium, and high risk commits.

## Risk Levels

- **Low**: No significant issues detected
- **Medium**: Large changes or moderate concerns
- **High**: Sensitive information detected (API keys, secrets, etc.)

## Testing

This project includes a set of tests to ensure the risk analysis is working correctly. To run the tests, simply execute:
```bash
python run_all_tests.py
```
The test runner will simulate different types of commits (low, medium, and high risk) and display the analysis for each.

## Configuration

The tool looks for the following environment variables in `.env`:
- `OPENAI_API_KEY`: Your OpenAI API key for AI-powered analysis (optional)



## License

This project is open source and available under the MIT License.

# Git Risk Analyzer

A Python tool that analyzes Git commits for security risks and potential issues using both rule-based analysis and AI-powered insights.

## Features

- **Git Diff Analysis**: Extracts and analyzes changes from specific commits
- **Risk Scoring**: Identifies potential security issues like exposed API keys, secrets, and large changes
- **AI-Powered Analysis**: Uses OpenAI GPT-3.5-turbo for detailed security risk explanations
- **Rich Output**: Beautiful console output with color-coded risk levels

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

Analyze a specific commit:
```bash
python main.py <commit-hash>
```

Example:
```bash
python main.py HEAD
python main.py abc123f
```

## Risk Levels

- **Low**: No significant issues detected
- **Medium**: Large changes or moderate concerns
- **High**: Sensitive information detected (API keys, secrets, etc.)

## Configuration

The tool looks for the following environment variables in `.env`:
- `OPENAI_API_KEY`: Your OpenAI API key for AI-powered analysis (optional)

## Project Structure

```
├── main.py                 # Entry point
├── analyzer/
│   ├── cli.py             # Command-line interface
│   ├── diff_extractor.py  # Git diff extraction
│   ├── risk_scoring.py    # Risk analysis logic
│   ├── output_renderer.py # Console output formatting
│   ├── ai_model.py        # OpenAI integration
│   ├── tokenizer.py       # Text tokenization
│   └── utils.py           # Utility functions
├── requirements.txt       # Python dependencies
└── .env                  # Environment variables
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

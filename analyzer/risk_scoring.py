import re
from analyzer.tokenizer import tokenize

def score_diff(diff: str):
    #print("\n[DEBUG] Diff content received for scoring:\n", diff, "\n")  # Add this debug line

    score = {"risk_level": "Low", "issues": []}

    if re.search(r"(api_key|secret|password|token)", diff, re.IGNORECASE):
        score["risk_level"] = "High"
        score["issues"].append("Sensitive information detected")

    tokens = tokenize(diff)
    if len(tokens) > 1000:
        if score["risk_level"] != "High":
            score["risk_level"] = "Medium"
        score["issues"].append("Large diff detected")

    return score


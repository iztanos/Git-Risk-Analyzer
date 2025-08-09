import re
from analyzer.tokenizer import tokenize

import re
from analyzer.tokenizer import tokenize
from analyzer.ai_model import explain_diff

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

    # Call AI model for additional explanation only if not already explained
    if not any("AI explanation" in issue for issue in score["issues"]):
        ai_explanation = explain_diff(diff)
        if ai_explanation:
            score["issues"].append(ai_explanation)

    return score

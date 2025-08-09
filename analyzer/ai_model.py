import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # load OPENAI_API_KEY from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_diff(diff: str) -> str:
    """
    Send the git diff to OpenAI GPT-4 model for security risk explanation.
    """
    if not os.getenv("OPENAI_API_KEY"):
        return "OpenAI API key not set. Skipping AI explanation."

    prompt = (
        "You are a security-aware code reviewer. "
        "Analyze this git diff and describe any security or risk issues in detail:\n\n"
        f"{diff}\n\n"
        "Explain the risks clearly and concisely."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in secure code reviews."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=500,
            temperature=0.2,
        )
        explanation = response.choices[0].message.content.strip()
        return explanation
    except Exception as e:
        error_message = str(e)
        if "insufficient_quota" in error_message:
            return "AI explanation error: Quota exceeded. Please check your plan and billing details."
        return f"AI explanation error: {e}"

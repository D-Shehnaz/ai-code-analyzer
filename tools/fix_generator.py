import json
from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def safe_extract(text):
    if not text:
        return "No output"

    try:
        text = str(text)
        text = text.replace("```python", "").replace("```", "").strip()

        # return raw code safely
        return text

    except Exception:
        return "Error parsing response"


def generate_fix(code, language, bugs):

    prompt = f"""
You are a senior software engineer.

Fix the code if needed.

RULES:
- Return ONLY corrected code
- No explanation
- No markdown

Language: {language}
Bugs: {bugs}

Code:
{code}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You return only fixed code. No explanation."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return safe_extract(response.choices[0].message.content)

    except Exception as e:
        return f"# Error generating fix: {str(e)}"
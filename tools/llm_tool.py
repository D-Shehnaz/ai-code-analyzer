import json
import re
from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


# -------------------------
# FALLBACK
# -------------------------
def fallback(msg="error"):
    return {
        "summary": "Analysis failed",
        "bugs_explained": msg,
        "severity_analysis": "Unknown",
        "suggestions": ["Unable to analyze properly"],
        "fix_explanation": "",
        "fixed_code": ""
    }


# -------------------------
# SAFE PARSER
# -------------------------
def safe_parse(text):

    try:
        if not text:
            return fallback("Empty response")

        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            return fallback("No JSON found")

        data = json.loads(match.group())

        fixed_code = data.get("fixed_code", "")

        # prevent garbage fixes
        if not isinstance(fixed_code, str):
            fixed_code = ""

        if len(fixed_code.strip()) < 3:
            fixed_code = ""

        return {
            "summary": data.get("summary", "No summary provided"),
            "bugs_explained": data.get("bugs_explained", ""),
            "severity_analysis": data.get("severity_analysis", ""),
            "suggestions": data.get("suggestions", []),
            "fix_explanation": data.get("fix_explanation", ""),
            "findings": data.get("findings", []),
            "fixed_code": fixed_code
        }

    except Exception as e:
        return fallback(str(e))


# -------------------------
# LLM TOOL
# -------------------------
class LLMTool:

    def explain(self, code, language, bugs, complexity, ast):

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """
You are an expert AI Code Reviewer.

You MUST ALWAYS:

1. summary → explain what the code does clearly
2. bugs_explained → explain issues OR say "No issues found"
3. severity_analysis → risk explanation
4. suggestions → ALWAYS give at least 1 improvement suggestion
5. fix_explanation → explain whether code is correct or not
6. fixed_code → ONLY improved code if needed, otherwise ""

RULES:
- If code is correct, say "Code is correct and safe"
- NEVER return empty summary
- NEVER skip explanation
- ALWAYS provide at least 1 suggestion
"""
                },
                {
                    "role": "user",
                    "content": f"""
Analyze this code:

CODE:
{code}

LANGUAGE:
{language}

BUGS:
{bugs}

COMPLEXITY:
{complexity}

AST:
{ast}

Return STRICT JSON ONLY.
Even if code is correct, explain it properly and give suggestions.
"""
                }
            ],
            temperature=0.2
        )

        return safe_parse(response.choices[0].message.content)
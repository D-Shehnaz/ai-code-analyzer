import json
import ast
from groq import Groq
from config import GROQ_API_KEY
from prompts.prompts import build_analysis_prompt

client = Groq(api_key=GROQ_API_KEY)


# -------------------------
# FALLBACK RESPONSE
# -------------------------
def fallback(reason="Unknown error"):
    return {
        "summary": "AI analysis failed",
        "bugs_explained": reason,
        "severity_analysis": "Unknown",
        "best_practices": [],
        "fixed_code": ""
    }


# -------------------------
# SAFE PARSER (FIXED)
# -------------------------
def safe_parse(text):

    if isinstance(text, dict):
        return text

    if text is None:
        return fallback("Empty response")

    try:
        text = str(text).strip()

        # remove markdown
        text = text.replace("```json", "").replace("```", "")

        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:
            return fallback("No JSON found")

        json_str = text[start:end + 1]

        # STEP 1: try JSON first
        try:
            return json.loads(json_str)
        except:
            pass

        # STEP 2: fallback for python dict format
        try:
            return ast.literal_eval(json_str)
        except:
            return fallback("Invalid JSON / dict format")

    except Exception as e:
        return fallback(f"Parse error: {str(e)}")


# -------------------------
# LLM TOOL
# -------------------------
class LLMTool:

    def explain(self, code, language, bugs, complexity, stats):

        prompt = build_analysis_prompt(
            code,
            language,
            bugs,
            complexity,
            stats
        )

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a strict JSON generator. "
                            "Return ONLY valid JSON. No text."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.1
            )

            text = response.choices[0].message.content

            return safe_parse(text)

        except Exception as e:
            return fallback(f"LLM error: {str(e)}")
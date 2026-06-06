def build_analysis_prompt(code, language, bugs, complexity, ast):
    return f"""
You are a senior code reviewer.

Return ONLY valid JSON.

Focus ONLY on explanation and improvements.

DO NOT repeat AST or complexity as raw data.

Instead, describe them in human language.

FORMAT:

{{
  "summary": "...",
  "bugs_explained": "...",
  "suggestions": "...",
  "fix_explanation": "...",
  "fixed_code": "..."
}}

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
"""
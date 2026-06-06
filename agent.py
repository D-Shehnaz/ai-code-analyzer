from tools.llm_tool import LLMTool
from tools.ast_parser import parse_code_basic
from tools.language_detector import detect_language
from tools.static_analyzer import analyze_complexity, detect_bugs


class Agent:

    def __init__(self):
        self.llm = LLMTool()

    def run(self, code):

        # 1. STATIC ANALYSIS (FACTS)
        ast = parse_code_basic(code)
        language = detect_language(code)
        complexity = analyze_complexity(code)
        bugs = detect_bugs(code, ast)

        # severity split
        critical = [b for b in bugs if b.get("severity") == "Critical"]
        warnings = [b for b in bugs if b.get("severity") != "Critical"]

        # 2. AI REVIEW (EXPLANATION ONLY)
        ai = self.llm.explain(
            code,
            language,
            bugs,
            complexity,
            ast
        )

        # 3. SIMPLE SEVERITY SCORE (HYBRID)
        severity_score = (
            len(critical) * 40 +
            len(warnings) * 10 +
            complexity.get("score", 0)
        )

        # 4. FINAL RESPONSE
        return {
            "static": {
                "language": language,
                "ast": ast,
                "complexity": complexity,
                "critical_bugs": critical,
                "warnings": warnings
            },

            "ai_review": ai,

            "severity_score": min(severity_score, 100),

            "final_fixed_code": ai.get("fixed_code", "")
        }
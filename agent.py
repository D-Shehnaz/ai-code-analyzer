from tools.language_detector import detect_language
from tools.ast_parser import parse_code_basic
from tools.complexity_tool import analyze_complexity
from tools.bug_detector import detect_bugs
from tools.llm_tool import LLMTool


class Agent:

    def __init__(self):
        self.llm = LLMTool()

    def run(self, code):

        ast = parse_code_basic(code)
        language = detect_language(code)
        complexity = analyze_complexity(code)
        bugs = detect_bugs(code, ast)

        ai = self.llm.explain(
            code,
            language,
            bugs,
            complexity,
            ast
        )

        return {
            "static": {
                "language": language,
                "ast": ast,
                "complexity": complexity
            },

            "critical_bugs": [b for b in bugs if b["severity"] == "Critical"],
            "warnings": [b for b in bugs if b["severity"] != "Critical"],

            "severity_score": min(
                100,
                len(bugs) * 15 + complexity.get("score", 0) * 5
            ),

            "ai_review": ai,

            "fixed_code": ai.get("fixed_code", "")
        }
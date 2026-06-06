def analyze_complexity(code: str):
    return {
        "functions": code.count("def ") + code.count("function"),
        "loops": code.count("for ") + code.count("while "),
        "conditions": code.count("if "),
        "try_blocks": code.count("try"),
        "score": len(code.splitlines())
    }


def detect_bugs(code: str, ast=None):
    """
    ONLY REAL, SAFE DETECTION SIGNALS
    NO fake "deep nesting", no guessing bugs
    """

    bugs = []

    # REAL unsafe pattern (Python)
    if "eval(" in code:
        bugs.append({
            "bug": "Use of eval() is unsafe",
            "severity": "Critical",
            "type": "security"
        })

    # REAL JS issue pattern
    if "console.log" in code and "try" in code:
        bugs.append({
            "bug": "Logging inside try block may leak errors",
            "severity": "Low",
            "type": "design"
        })

    return bugs
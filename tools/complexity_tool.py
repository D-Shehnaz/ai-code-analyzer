def analyze_complexity(code):

    lines = len(code.split("\n"))

    return {
        "functions": code.count("def "),
        "loops": code.count("for ") + code.count("while "),
        "conditions": code.count("if ") + code.count("elif "),
        "lines": lines,
        "score": min(
            10,
            code.count("for ")
            + code.count("while ")
            + code.count("if ")
            + (lines // 20)
        )
    }
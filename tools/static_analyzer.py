def analyze_complexity(code):

    score = 1

    score += code.count("for ")
    score += code.count("while ")
    score += code.count("if ")
    score += code.count("elif ")
    score += code.count("try")

    return {
        "functions": code.count("def "),
        "loops": code.count("for ") + code.count("while "),
        "conditions": code.count("if ") + code.count("elif "),
        "try_blocks": code.count("try"),
        "score": min(score, 10)
    }
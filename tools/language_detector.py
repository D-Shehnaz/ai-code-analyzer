def detect_language(code: str):
    code = code.lower()

    if "console.log" in code or "function" in code or "const " in code:
        return "javascript"

    if "def " in code or "import " in code or "print(" in code:
        return "python"

    if "#include" in code:
        return "c/c++"

    return "unknown"
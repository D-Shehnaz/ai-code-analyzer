def detect_bugs(code, ast):

    bugs = []
    c = code.lower()

    # -------------------------
    # SQL INJECTION
    # -------------------------
    if "select" in c and ("+" in c or "f\"" in c or "f'" in c):
        bugs.append({
            "type": "sql_injection",
            "severity": "Critical",
            "message": "Unsafe SQL query construction detected"
        })

    # -------------------------
    # COMMAND INJECTION
    # -------------------------
    if "os.system" in c or "subprocess" in c:
        bugs.append({
            "type": "command_injection",
            "severity": "Critical",
            "message": "System command execution detected"
        })

    # -------------------------
    # HARD CODED SECRET
    # -------------------------
    if "password" in c or "api_key" in c:
        bugs.append({
            "type": "hardcoded_secret",
            "severity": "Warning",
            "message": "Hardcoded credentials detected"
        })

    # -------------------------
    # DESIGN ISSUE (FIXED LOGIC)
    # -------------------------
    if ast and not ast.get("has_function"):

        if ast.get("has_loop") or ast.get("has_condition"):
            bugs.append({
                "type": "design_issue",
                "severity": "Warning",
                "message": "Complex logic without function structure"
            })

    return bugs
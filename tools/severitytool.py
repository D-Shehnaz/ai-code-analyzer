WEIGHTS = {
    "sql_injection": 50,
    "command_injection": 50,
    "hardcoded_secret": 30,
    "design_issue": 10
}

def calculate_severity(bugs):

    score = 0
    breakdown = {"critical": 0, "warning": 0}

    for b in bugs:
        score += WEIGHTS.get(b["type"], 10)

        if b["severity"].lower() == "critical":
            breakdown["critical"] += 1
        else:
            breakdown["warning"] += 1

    return {
        "score": min(score, 100),
        "breakdown": breakdown
    }
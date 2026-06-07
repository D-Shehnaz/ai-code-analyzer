def generate_fix(bug_type):

    fixes = {
        "sql_injection": "Use parameterized queries instead of string concatenation.",
        "command_injection": "Use subprocess.run([...]) instead of os.system.",
        "hardcoded_secret": "Move secrets to environment variables.",
        "design_issue": "Wrap logic inside functions for better structure."
    }

    return fixes.get(bug_type, "Manual review required.")
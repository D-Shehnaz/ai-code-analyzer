import ast

def check_syntax(code: str):

    try:
        ast.parse(code)
        return {
            "valid": True,
            "error": None
        }
    except Exception as e:
        return {
            "valid": False,
            "error": str(e)
        }
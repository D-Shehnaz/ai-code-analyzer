from tree_sitter import Language, Parser

# NOTE: For production you would build grammars.
# For your assignment we use lightweight fallback AST-like parsing.

def parse_code_basic(code: str):
    """
    Lightweight AST-like structure (safe for student projects)
    """

    return {
        "has_function": "def " in code or "function" in code,
        "has_loop": "for " in code or "while " in code,
        "has_condition": "if " in code,
        "language_hints": {
            "python": "def " in code,
            "javascript": "console.log" in code or "function" in code
        }
    }
import ast

def parse_code_basic(code):

    try:
        tree = ast.parse(code)

        return {
            "has_function": any(isinstance(n, ast.FunctionDef) for n in ast.walk(tree)),
            "has_loop": any(isinstance(n, (ast.For, ast.While)) for n in ast.walk(tree)),
            "has_condition": any(isinstance(n, ast.If) for n in ast.walk(tree)),
            "has_expression": any(isinstance(n, ast.Expr) for n in ast.walk(tree))
        }

    except:
        return {
            "has_function": False,
            "has_loop": False,
            "has_condition": False,
            "has_expression": False
        }
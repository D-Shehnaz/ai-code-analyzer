import ast


class ComplexityTool:

    def execute(self, code):

        result = {
            "functions": 0,
            "loops": 0,
            "conditions": 0,
            "try_blocks": 0,
            "score": 0
        }

        try:

            tree = ast.parse(code)

        except:

            return result

        for node in ast.walk(tree):

            if isinstance(
                node,
                ast.FunctionDef
            ):
                result["functions"] += 1

            elif isinstance(
                node,
                (ast.For, ast.While)
            ):
                result["loops"] += 1

            elif isinstance(
                node,
                ast.If
            ):
                result["conditions"] += 1

            elif isinstance(
                node,
                ast.Try
            ):
                result["try_blocks"] += 1

        result["score"] = (
            result["functions"]
            + result["loops"] * 2
            + result["conditions"] * 2
            + result["try_blocks"]
        )

        return result
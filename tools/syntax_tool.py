import ast


class SyntaxTool:

    def execute(self, code, language):

        if language != "Python":

            return {
                "valid": True,
                "message": "Syntax check only enabled for Python"
            }

        try:

            ast.parse(code)

            return {
                "valid": True,
                "message": "No Syntax Errors"
            }

        except Exception as e:

            return {
                "valid": False,
                "message": str(e)
            }
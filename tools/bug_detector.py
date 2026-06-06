import ast


class BugDetector:

    def execute(self, code):

        bugs = []

        try:

            tree = ast.parse(code)

        except Exception:

            return bugs

        # -------------------------
        # Division by constant zero
        # -------------------------

        for node in ast.walk(tree):

            if isinstance(node, ast.BinOp):

                if isinstance(node.op, ast.Div):

                    if (
                        isinstance(node.right, ast.Constant)
                        and node.right.value == 0
                    ):

                        bugs.append(
                            {
                                "bug":
                                "Division By Zero",

                                "severity":
                                "High"
                            }
                        )

        # -------------------------
        # Infinite loops
        # -------------------------

        for node in ast.walk(tree):

            if isinstance(node, ast.While):

                if (
                    isinstance(node.test, ast.Constant)
                    and node.test.value is True
                ):

                    has_break = False

                    for child in ast.walk(node):

                        if isinstance(
                            child,
                            ast.Break
                        ):
                            has_break = True

                    if not has_break:

                        bugs.append(
                            {
                                "bug":
                                "Potential Infinite Loop",

                                "severity":
                                "High"
                            }
                        )

        # -------------------------
        # Dangerous eval()
        # -------------------------

        for node in ast.walk(tree):

            if isinstance(node, ast.Call):

                if (
                    isinstance(node.func, ast.Name)
                    and node.func.id == "eval"
                ):

                    bugs.append(
                        {
                            "bug":
                            "Unsafe eval() Usage",

                            "severity":
                            "High"
                        }
                    )

        # -------------------------
        # Generic Exception
        # -------------------------

        for node in ast.walk(tree):

            if isinstance(node, ast.ExceptHandler):

                if node.type is None:

                    bugs.append(
                        {
                            "bug":
                            "Generic Exception Handler",

                            "severity":
                            "Medium"
                        }
                    )

        # -------------------------
        # Empty exception block
        # -------------------------

        for node in ast.walk(tree):

            if isinstance(node, ast.Try):

                for handler in node.handlers:

                    if len(handler.body) == 1:

                        stmt = handler.body[0]

                        if isinstance(
                            stmt,
                            ast.Pass
                        ):

                            bugs.append(
                                {
                                    "bug":
                                    "Silent Exception Handling",

                                    "severity":
                                    "Medium"
                                }
                            )

        # -------------------------
        # Hardcoded passwords
        # -------------------------

        password_keywords = [
            "password",
            "passwd",
            "secret",
            "apikey",
            "token"
        ]

        for node in ast.walk(tree):

            if isinstance(node, ast.Assign):

                for target in node.targets:

                    if isinstance(
                        target,
                        ast.Name
                    ):

                        name = target.id.lower()

                        if any(
                            keyword in name
                            for keyword
                            in password_keywords
                        ):

                            bugs.append(
                                {
                                    "bug":
                                    "Hardcoded Credential",

                                    "severity":
                                    "Critical"
                                }
                            )

        # -------------------------
        # Deep nesting
        # -------------------------

        max_depth = self.get_depth(tree)

        if max_depth >= 5:

            bugs.append(
                {
                    "bug":
                    "Deep Nesting",

                    "severity":
                    "Low"
                }
            )

        # -------------------------
        # Large function
        # -------------------------

        for node in ast.walk(tree):

            if isinstance(
                node,
                ast.FunctionDef
            ):

                line_count = len(node.body)

                if line_count > 30:

                    bugs.append(
                        {
                            "bug":
                            f"Large Function ({node.name})",

                            "severity":
                            "Low"
                        }
                    )

        return bugs

    def get_depth(
        self,
        node,
        depth=0
    ):

        children = list(
            ast.iter_child_nodes(node)
        )

        if not children:

            return depth

        return max(
            self.get_depth(
                child,
                depth + 1
            )
            for child in children
        )
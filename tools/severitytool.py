class SeverityTool:

    def execute(self, bugs):

        score = 0

        for bug in bugs:

            level = bug["severity"]

            if level == "Critical":
                score += 10

            elif level == "High":
                score += 7

            elif level == "Medium":
                score += 4

            elif level == "Low":
                score += 1

        return score
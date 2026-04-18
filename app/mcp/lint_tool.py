import subprocess

class LintTool:
    def run_flake8(self, path: str) -> str:
        result = subprocess.run(
            ["flake8", path],
            capture_output=True,
            text=True,
        )

        return result.stdout
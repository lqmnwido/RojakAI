import subprocess

class SearchTool:
    def search(self, query: str, root: str) -> str:
        result = subprocess.run(
            ["rg", query, root],
            capture_output=True,
            text=True,
        )

        return result.stdout
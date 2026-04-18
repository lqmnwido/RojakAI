import subprocess

class TerminalTool:
    def run(self, command: str) -> dict:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )

        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode,
        }
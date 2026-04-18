from pathlib import Path

class FileTool:
    def read(self, path: str) -> str:
        return Path(path).read_text(encoding="utf-8", errors="ignore")
from pathlib import Path

class Chunker:
    def chunk_file(self, file_path: str, chunk_size: int = 1500) -> list[str]:
        text = Path(file_path).read_text(encoding="utf-8", errors="ignore")

        chunks: list[str] = []

        for index in range(0, len(text), chunk_size):
            chunks.append(text[index:index + chunk_size])

        return chunks
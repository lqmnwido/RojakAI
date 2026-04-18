from pathlib import Path

from app.llm.ollama_client import OllamaClient
from app.rag.chunker import Chunker
from app.rag.vector_store import VectorStore


class Indexer:
    def __init__(self) -> None:
        self.chunker = Chunker()
        self.vector_store = VectorStore()
        self.ollama = OllamaClient()

    def index_project(self, root_path: str) -> None:
        point_id = 1

        allowed_extensions = {
            ".py",
            ".js",
            ".ts",
            ".tsx",
            ".vue",
            ".php",
            ".md",
            ".json",
            ".yaml",
            ".yml",
        }

        for file_path in Path(root_path).rglob("*"):
            if not file_path.is_file():
                continue

            if file_path.suffix.lower() not in allowed_extensions:
                continue

            chunks = self.chunker.chunk_file(str(file_path))

            for chunk in chunks:
                embedding = self.ollama.embed(chunk)

                self.vector_store.insert(
                    point_id=point_id,
                    embedding=embedding,
                    payload={
                        "file": str(file_path),
                        "content": chunk,
                    },
                )

                point_id += 1
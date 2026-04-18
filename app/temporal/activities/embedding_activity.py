from app.rag.indexer import Indexer

class EmbeddingActivity:
    async def run(self, path: str) -> str:
        Indexer().index_project(path)
        return "done"
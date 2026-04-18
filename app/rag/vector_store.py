from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from app.config.settings import settings

class VectorStore:
    def __init__(self) -> None:
        self.client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT,
        )

        self.collection = settings.QDRANT_COLLECTION
        self._create_collection()

    def _create_collection(self) -> None:
        existing = [
            item.name
            for item in self.client.get_collections().collections
        ]

        if self.collection not in existing:
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(
                    size=768,
                    distance=Distance.COSINE,
                ),
            )

    def insert(self, point_id: int, embedding: list[float], payload: dict) -> None:
        self.client.upsert(
            collection_name=self.collection,
            points=[
                PointStruct(
                    id=point_id,
                    vector=embedding,
                    payload=payload,
                )
            ],
        )

    def search(self, embedding: list[float], limit: int = 5):
        response = self.client.query_points(
            collection_name=self.collection,
            query=embedding,
            limit=limit,
        )

        return response.points
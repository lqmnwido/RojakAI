from minio import Minio

from app.config.settings import settings

class MinioStorage:
    def __init__(self) -> None:
        self.client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=False,
        )

        if not self.client.bucket_exists(settings.MINIO_BUCKET):
            self.client.make_bucket(settings.MINIO_BUCKET)

    def upload_file(self, object_name: str, file_path: str) -> None:
        self.client.fput_object(
            settings.MINIO_BUCKET,
            object_name,
            file_path,
        )
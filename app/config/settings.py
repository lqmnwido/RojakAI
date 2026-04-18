from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OLLAMA_URL: str
    OLLAMA_MODEL: str
    OLLAMA_EMBED_MODEL: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    REDIS_HOST: str
    REDIS_PORT: int

    QDRANT_HOST: str
    QDRANT_PORT: int
    QDRANT_COLLECTION: str

    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_BUCKET: str

    TEMPORAL_HOST: str
    TEMPORAL_NAMESPACE: str

    PROJECT_ROOT: str
    LOG_PATH: str
    CACHE_PATH: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
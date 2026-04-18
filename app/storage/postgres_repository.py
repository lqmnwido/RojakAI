from sqlalchemy import create_engine, text
import urllib.parse
from app.config.settings import settings

class PostgresRepository:
    def __init__(self) -> None:
        encoded_password = urllib.parse.quote_plus(settings.POSTGRES_PASSWORD)
        self.engine = create_engine(
            (
                f"postgresql+psycopg2://"
                f"{settings.POSTGRES_USER}:"
                f"{encoded_password}@"
                f"{settings.POSTGRES_HOST}:"
                f"{settings.POSTGRES_PORT}/"
                f"{settings.POSTGRES_DB}"
            )
        )

    def create_tables(self) -> None:
        with self.engine.begin() as connection:
            connection.execute(
                text(
                    """
                    CREATE TABLE IF NOT EXISTS messages (
                        id SERIAL PRIMARY KEY,
                        question TEXT NOT NULL,
                        answer TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT NOW()
                    )
                    """
                )
            )

    def save_message(self, question: str, answer: str) -> None:
        with self.engine.begin() as connection:
            connection.execute(
                text(
                    """
                    INSERT INTO messages (question, answer)
                    VALUES (:question, :answer)
                    """
                ),
                {
                    "question": question,
                    "answer": answer,
                },
            )
from dotenv import load_dotenv

class EnvLoader:
    @staticmethod
    def load() -> None:
        load_dotenv()
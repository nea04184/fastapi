from pydantic import BaseSettings


class Settings(BaseSettings):
    mongo_db_url: str = "mongodb://localhost:27017"
    mongo_db_name: str = "FAST"

    class Config:
        env_file = ".env"


def get_settings() -> BaseSettings:
    return Settings()

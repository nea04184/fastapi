from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_db_url: str = "mongodb://localhost:27017"

    class Config:
        env_file = ".env"

def get_settings() -> BaseSettings:
    return Settings()

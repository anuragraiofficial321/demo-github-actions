from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Production App"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "your-secret-key"
    ALLOWED_ORIGINS: List[str] = ["*"]
    OPENAI_API_KEY: str = "your-openai-api-key"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str  # ✅ Match the environment variable name exactly

    class Config:
        env_file = ".env"

settings = Settings()
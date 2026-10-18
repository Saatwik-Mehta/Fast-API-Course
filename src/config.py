from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE_PATH = BASE_DIR / ".env"

class Settings(BaseSettings):
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, extra="ignore")


Config = Settings()
print("ENGINE IS USING URL:", repr(Config.DATABASE_URL))

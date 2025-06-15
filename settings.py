from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv('.env.local')
load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    class Config:
        case_sensitive = True


settings = Settings()

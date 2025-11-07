from pydantic_settings import BaseSettings
from datetime import timedelta
import os 
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    secrect_key: str
    algorithm: str
    token_expire_minutes: int | None = None


    # Database config

    database_username: str
    database_name:str
    database_password: str
    database_host: str
    database_port: str

    class Config:
        env_file = ".env"

settings = Settings()

POSTGRESQL_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"
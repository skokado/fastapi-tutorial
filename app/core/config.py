import os
from pathlib import Path
import secrets
from typing import Dict, List, Union, Optional, Any

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator

BASE_DIR = Path(__file__).parent.parent.parent
env_path = BASE_DIR / '.env'
if not env_path.exists():
    raise OSError('.env file not exists.')

load_dotenv(env_path)


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    SERVER_NAME: str = 'Full Stack Tutorial'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEBUG: bool = bool(os.getenv('DEBUG', False))
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(
        cls, v: Union[str, List[str]]
    ) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = 'full-stack'

    PGUSER = os.getenv('PGUSER', '')
    PGPASSWORD = os.getenv('PGPASSWORD', '')
    PGHOST = os.getenv('PGHOST', '127.0.0.1')
    PGPORT = os.getenv('PGPORT', 5432)
    PGDATABASE = os.getenv('PGDATABASE', '')
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + \
        f'{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}'

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str],
                               values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True


settings = Settings()

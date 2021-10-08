import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.main import app
from app.dependencies import get_db

test_db_host = os.getenv('TEST_PGHOST', '127.0.0.1')
test_db_port = os.getenv('TEST_PGPORT', '5433')

settings.SQLALCHEMY_DATABASE_URI = f"postgresql://app:secret@{test_db_host}:{test_db_port}/app"
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI, connect_args={"sslmode": 'disable'}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

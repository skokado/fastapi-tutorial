from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.main import app
from app.dependencies import get_db

settings.SQLALCHEMY_DATABASE_URI = "postgresql://app:secret@127.0.0.1:5433/app"
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

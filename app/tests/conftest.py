from typing import Generator
import pytest
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database

from app.core.config import settings
from app.database import Base
from app.tests.utils.overrides import TestingSessionLocal, engine


@pytest.fixture(scope="function")
def db() -> Generator[Session, None, None]:
    if not database_exists(settings.SQLALCHEMY_DATABASE_URI):
        create_database(settings.SQLALCHEMY_DATABASE_URI)

    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

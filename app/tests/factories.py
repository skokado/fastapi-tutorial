from factory.alchemy import SQLAlchemyModelFactory

import app.models.user as models
from app.tests.utils.overrides import TestingSessionLocal


class UserFactory(SQLAlchemyModelFactory):
    name = 'skokado'
    email = 'skokado@example.com'
    password = 'MyPassw0rd!'

    class Meta:
        model = models.User
        sqlalchemy_session = TestingSessionLocal()

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
import app.crud.users as users_crud
from app.tests import factories

client = TestClient(app)


class TestAuthRouter:

    def test_ログイン成功(self, db: Session):
        user_in = factories.UserFactory()
        users_crud.create(user_in, db)
        response = client.post(
            '/api/login',
            data={
                'grant_type': 'password',
                'username': user_in.name,
                'password': user_in.password
            }
        )
        assert response.status_code == 200

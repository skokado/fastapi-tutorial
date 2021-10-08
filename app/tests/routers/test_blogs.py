from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
import app.crud.users as users_crud
from app.core.security import create_access_token
from app.tests import factories

client = TestClient(app)
client.headers.update({
    'Authorization': 'Bearer {}'.format(create_access_token)
})


class TestBlogRouter:
    def test_list_empty_blogs(self, db: Session):
        user_in = factories.UserFactory()
        users_crud.create(user_in, db)
        # ログインを実行
        response = client.post(
            '/api/login',
            data={
                'grant_type': 'password',
                'username': user_in.name,
                'password': user_in.password
            }
        )
        jwt = response.json()
        headers = {
            'Authorization': f'{jwt["token_type"].capitalize()} {jwt["access_token"]}'
        }

        # アクセストークンを使用してAPIリクエスト
        response = client.get('/api/blog/', headers=headers)
        assert response.status_code == 200
        assert response.json() == []

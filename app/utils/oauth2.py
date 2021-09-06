from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.models.user import User
from app.dependencies import get_db
from app.utils.token import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")


def get_current_user(db: Session = Depends(get_db),
                     token: str = Depends(oauth2_scheme)):
    username = verify_token(token)
    user = db.query(User).filter(User.name == username).first()
    return user

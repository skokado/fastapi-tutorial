from fastapi import HTTPException, status
import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import schemas
from app.models.user import User
from app.core.security import get_password_hash


def show(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User id {id} not found.'
        )
    return user


def create(request: schemas.User, db: Session):
    hashed_password = get_password_hash(request.password)
    new_user = User(
        name=request.name,
        email=request.email,
        password=hashed_password
    )
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except sa.exc.IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.args[0]
        )
    return new_user

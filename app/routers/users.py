from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import schemas
from app.dependencies import get_db
import app.crud.users as crud
from app.utils.oauth2 import get_current_user

router = APIRouter(
    prefix='/user',
    tags=['Users'],
)


@router.get('/me', response_model=schemas.ShowUser)
def me(current_user: schemas.ShowUser = Depends(get_current_user)):
    return current_user


@router.get('/{id}', response_model=schemas.ShowUser)
def show(id: int, db: Session = Depends(get_db)):
    return crud.show(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED,
             response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(get_db)):
    return crud.create(request, db)

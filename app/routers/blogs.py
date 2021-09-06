from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import schemas
from app.dependencies import get_db
import app.crud.blogs as crud
from app.utils.oauth2 import get_current_user

router = APIRouter(
    prefix='/blog',
    tags=['Blogs'],
    dependencies=[Depends(get_current_user)],
)


@router.get('/', response_model=List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db)):
    return crud.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK,
            response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return crud.show(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.BlogBase, db: Session = Depends(get_db)):
    return crud.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return crud.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.BlogBase,
           db: Session = Depends(get_db)):
    return crud.update(id, request, db)

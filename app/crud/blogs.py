from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app import schemas
from app.models.blog import Blog


def get_all(db: Session):
    blogs = db.query(Blog).all()
    return blogs


def show(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog id {id} not found'
        )
    return blog


def create(request: schemas.Blog, db: Session):
    new_blog = Blog(title=request.title, content=request.content, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog id {id} not found'
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.BlogBase, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog id {id} not found'
        )
    if request.title:
        blog.update({'title': request.title})
    if request.content:
        blog.update({'content': request.content})
    db.commit()
    return 'done'

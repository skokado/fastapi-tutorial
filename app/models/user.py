import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String, unique=True)
    email = sa.Column(sa.String, unique=True)
    password = sa.Column(sa.String)

    blogs = relationship('Blog', back_populates='creator')

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.database import Base


class Blog(Base):
    __tablename__ = 'blogs'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    title = sa.Column(sa.String)
    content = sa.Column(sa.String)

    creator = relationship('User', back_populates='blogs')
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

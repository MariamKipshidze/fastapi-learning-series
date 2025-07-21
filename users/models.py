from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from blog.models import post_likes
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    posts = relationship(argument="BlogPost", back_populates="author")
    liked_posts = relationship(argument="BlogPost", secondary=post_likes, back_populates="likes")
    comments = relationship(argument="Comment", back_populates="author")

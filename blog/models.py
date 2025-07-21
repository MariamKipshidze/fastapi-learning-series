from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from database import Base

post_likes = Table(
    'post_likes',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True)
)


class BlogPost(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)

    author = relationship("User", back_populates="posts")
    likes = relationship("User", secondary=post_likes, back_populates="liked_posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")

    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))

    @hybrid_property
    def like_count(self):
        return len(self.likes)

    @hybrid_property
    def comment_count(self):
        return len(self.comments)


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'))
    author_id = Column(Integer, ForeignKey('users.id'))

    post = relationship("BlogPost", back_populates="comments")
    author = relationship("User", back_populates="comments")

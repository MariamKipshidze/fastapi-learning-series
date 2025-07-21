from pydantic import BaseModel, Field
from typing import List, Optional


# ------------------ User Schema (minimal, for reference only) ------------------ #
class UserBase(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


# ------------------ Comment Schemas ------------------ #
class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    post_id: int
    author_id: int


class CommentUpdate(BaseModel):
    content: Optional[str] = None


class CommentOut(CommentBase):
    id: int
    author: UserBase

    class Config:
        orm_mode = True


# ------------------ BlogPost Schemas ------------------ #
class BlogPostBase(BaseModel):
    title: str = Field(..., example="My First Blog Post", min_length=3, max_length=100)
    content: str = Field(..., example="This is the content of the blog post.", min_length=10)
    like_count: int
    comment_count: int

    class Config:
        orm_mode = True


class BlogPostCreate(BlogPostBase):
    author_id: int


class BlogPostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class BlogPostOut(BlogPostBase):
    id: int
    author: UserBase
    likes: List[UserBase] = []
    comments: List[CommentOut] = []

    class Config:
        orm_mode = True

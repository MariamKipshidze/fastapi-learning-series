from pydantic import BaseModel
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
    title: str
    content: str


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

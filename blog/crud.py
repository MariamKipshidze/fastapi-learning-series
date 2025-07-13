from sqlalchemy.orm import Session
from blog.models import BlogPost
from blog.schemas import BlogPostCreate, BlogPostUpdate


def create_post(post: BlogPostCreate, db: Session):
    db_post = BlogPost(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(post_id: int, db: Session):
    return db.query(BlogPost).filter(BlogPost.id == post_id).first()


def get_all_posts(db: Session):
    return db.query(BlogPost).all()


def update_post(post_id: int, update_data: BlogPostUpdate, db: Session):
    post = get_post(post_id, db)
    if not post:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(post, key, value)
    db.commit()
    db.refresh(post)
    return post


def delete_post(post_id: int, db: Session):
    post = get_post(post_id, db)
    if not post:
        return None
    db.delete(post)
    db.commit()
    return post

from sqlalchemy.orm import Session
from users import models, schemas


def create_user(user: schemas.UserCreate, db: Session):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(models.User).all()

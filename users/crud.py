from users import models, schemas
from database import SessionLocal

db = SessionLocal()

def create_user(user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users():
    return db.query(models.User).all()

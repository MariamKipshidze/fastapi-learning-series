from blog import crud, schemas
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.BlogPostOut])
def list_posts(db: Session = Depends(get_db)):
    return crud.get_all_posts(db)


@router.get("/{post_id}", response_model=schemas.BlogPostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(post_id, db)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("/", response_model=schemas.BlogPostOut)
def create_post(post: schemas.BlogPostCreate, db: Session = Depends(get_db)):
    return crud.create_post(post, db)


@router.put("/{post_id}", response_model=schemas.BlogPostOut)
def update_post(post_id: int, post_data: schemas.BlogPostUpdate, db: Session = Depends(get_db)):
    post = crud.update_post(post_id, post_data, db)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.delete_post(post_id, db)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted"}

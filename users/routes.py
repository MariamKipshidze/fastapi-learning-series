from fastapi import APIRouter
from typing import List

from users.schemas import UserCreate, UserOut
from users.crud import create_user, get_users

router = APIRouter()


@router.post("/", response_model=UserOut)
def create_user_route(user: UserCreate):
    return create_user(user)


@router.get("/", response_model=List[UserOut])
def get_users_route():
    return get_users()

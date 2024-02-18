from schmas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_users

router = APIRouter(
    prefix='/user',
    tags=['user']
)

# CREATE USER
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_users.create_user(db, request)
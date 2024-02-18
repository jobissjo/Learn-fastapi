from db.hash import Hash
from sqlalchemy.orm.session import Session
from schmas import UserBase, UserDisplay
from db.models import DbUser


def create_user(db:Session, request:UserBase)-> UserDisplay:
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
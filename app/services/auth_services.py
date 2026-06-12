from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

def register_user(db: Session, user):
    
    existing = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing:
        return None

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(db: Session, user):
    
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        return None

    if not verify_password(
        user.password,
        db_user.password
    ):
        return None

    token = create_access_token(
        {
            "sub": db_user.email,
            "role": db_user.role
        }
    )

    return token
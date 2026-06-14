from app.database import SessionLocal
from app.model.user import User


def save_user(user: User):

    db = SessionLocal()

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_email(email: str):

    db = SessionLocal()

    user = db.query(User).filter(
        User.email == email
    ).first()

    return user


def get_user_by_id(user_id: int):

    db = SessionLocal()

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    return user
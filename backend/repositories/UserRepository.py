from sqlalchemy.orm import Session

from .DataBaseRepository import User


def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def user_helper(user):
    return {
        "id": str(user.id),
        "username":  user.username,
        "email": user.email,
        "password": user.password
    }


async def listar_users(db):
    return db.query(User).all()


async def buscar_user_por_email(db, email: str) -> dict:
    user = db.query(User).filter_by(email=email).first()
    if user:
        return user_helper(user)


async def atualizar_user(db, id: int, dados_user: dict):
    user = db.query(User).filter(User.id == id).first()
    if user:
        for key, value in dados_user.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user


async def deletar_user(db, id: int):
    user = db.query(User).filter(User.id == id).first()
    if user:
        db.delete(user)
        db.commit()
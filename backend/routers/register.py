import re
from sqlite3 import IntegrityError
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from repositories.DataBaseRepository import User, get_db
from models.UserModel import UserCreation
from utils.AuthUtil import gerar_password_cripty


router = APIRouter()


@router.post("/register")
async def register(user_data: UserCreation, db: Session = Depends(get_db)):
    
    # Validação de e-mail
    regex = r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$"
    if not re.fullmatch(regex, user_data.email):
        raise HTTPException(
            status_code=400,
            detail="O e-mail fornecido não é válido.",
        )
    
    if not user_data.email:
        raise HTTPException(
            status_code=400,
            detail="O e-mail não pode ser vazio.",
        )

    # Validação de senha e confirmação de senha
    if user_data.password != user_data.confirm_password:
        raise HTTPException(
            status_code=422,
            detail="A senha e a confirmação de senha não coincidem.",
        )

    # Criar novo usuário
    hashed_password = gerar_password_cripty(user_data.password)
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password=hashed_password
    )
    
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "Usuário registrado com sucesso!"}
    
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="E-mail ou nome de usuário já cadastrado")


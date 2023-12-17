from datetime import timedelta
from fastapi import APIRouter, Body, Depends, HTTPException
from requests import Session

from models.UserModel import UserLoginModel
from services.AuthService import login_service, create_jwt_token
from repositories.DataBaseRepository import get_db


router = APIRouter()


@router.post("/login")
async def login(user: UserLoginModel = Body(...), db: Session = Depends(get_db)):
    resultado = await login_service(user, db)

    if not resultado["status"] == 200:
        raise HTTPException(status_code = resultado['status'], detail = resultado['mensagem'])
    
    del resultado["dados"]["password"]

    token = create_jwt_token({"id": resultado["dados"]["id"]}, timedelta(minutes=600))

    resultado["token"] = token
    
    return resultado
from passlib.context import CryptContext
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from requests import Session
from datetime import datetime, timedelta

from models.UserModel import UserLoginModel
from repositories.UserRepository import buscar_user_por_email
from utils.AuthUtil import verificar_password
from services.LogoutService import AuthService


SECRET_KEY = "chavesecretaParaO_ProjetoCarros_123567"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_jwt_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def login_service(user: UserLoginModel, db: Session):
    user_encontrado = await buscar_user_por_email(db, user.email)

    if not user_encontrado:
        return {
            "mensagem": "E-mail ou Senha incorretos.",
            "dados": "",
            "status": 401
        }
    else:
        if await verificar_password(user.password, user_encontrado["password"]):
            return {
                "mensagem": "Login efetuado com sucesso!",
                "dados": user_encontrado,
                "status": 200
            }
        else:
            return {
            "mensagem": "E-mail ou Senha incorretos.",
            "dados": "",
            "status": 401
        }


async def logout(token: str):
        if token in AuthService.valid_tokens:
            AuthService.valid_tokens.remove(token)


async def is_token_valid(token: str):
        return token in AuthService.valid_tokens

from fastapi import APIRouter, Depends
import services.AuthService
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    services.AuthService.logout(token)
    return {"status": True, "msg": "Deslogado com sucesso"}
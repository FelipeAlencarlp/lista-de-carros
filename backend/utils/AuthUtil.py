from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def gerar_password_cripty(password):
    return pwd_context.hash(password)


async def verificar_password(password: str, password_criptografada: str):
    return pwd_context.verify(password, password_criptografada)
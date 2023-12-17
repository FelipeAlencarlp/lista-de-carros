from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from repositories.DataBaseRepository import User, get_db

from utils.AuthUtil import gerar_password_cripty
from repositories.DataBaseRepository import create_tables, SessionLocal
from routers.AutenticacaoRoute import router as LoginRoute
from routers.register import router as RegistrarRoute
from routers.cars import router as CarroRoute
from routers.imagens import router as UploadFotoRoute
from routers.logout import router as LogoutRoute


app = FastAPI()


# Configurar middleware CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Criação das tabelas no banco de dados
create_tables()


# Função para criar usuário administrador
def create_admin_user(db: Session = Depends(get_db)):
    admin_user = db.query(User).filter_by(username="admin").first()
    if not admin_user:
        hashed_password = gerar_password_cripty("secret123")  # Substitua pela senha desejada
        admin_user = User(
            username="admin",
            email="admin@carros.com",
            password=hashed_password,
            is_admin=True
        )
        db.add(admin_user)
        db.commit()

# Inicializar usuário administrador
db = SessionLocal()
create_admin_user(db)


# Rotas
app.include_router(RegistrarRoute, tags=["Registrar"], prefix="/api")
app.include_router(CarroRoute, tags=["Carros"], prefix="/api")
app.include_router(LoginRoute, tags=["Autenticacao"], prefix="/api/auth")
app.include_router(UploadFotoRoute, tags=["Foto"], prefix="")
app.include_router(LogoutRoute, tags=["Logout"], prefix="")


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

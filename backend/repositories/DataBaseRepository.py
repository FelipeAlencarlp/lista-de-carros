from sqlalchemy import Float, create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "sqlite:///./carros.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)


    # Relacionamento um para muitos com Carro
    # carros = relationship("Car", back_populates="proprietario")

    class Car(Base):
        __tablename__ = "cars"
        id = Column(Integer, primary_key=True, index=True)
        nome = Column(String, index=True)
        marca = Column(String, index=True)
        modelo = Column(String, index=True)
        valor = Column(Float)
        foto = Column(String)
        ano = Column(String)
        km = Column(String)
        cidade = Column(String)
        
        # Chave estrangeira para a tabela users
        # proprietario_id = Column(Integer, ForeignKey("users.id"))
        
        # Relacionamento muitos para um com Usuario
        # proprietario = relationship("User", back_populates="cars")


def create_tables():
    # Base = declarative_base()
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
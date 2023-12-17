from sqlalchemy.orm import Session
from sqlalchemy import Float, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "sqlite:///./carros.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


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


def get_cars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Car).order_by(Car.valor).offset(skip).limit(limit).all()


def get_car_by_id(db: Session, car_id: int):
    return db.query(Car).filter(Car.id == car_id).first()


def create_car(db: Session, car: Car):
    db_car = Car(**car.model_dump())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


def update_car(db: Session, car_id: int, updated_car: Car):
    # Lógica para atualizar o carro no banco de dados
    db_car = db.query(Car).get(car_id)
    if db_car:
        for key, value in updated_car.model_dump().items():
            setattr(db_car, key, value)
        db.commit()
        db.refresh(db_car)
        
        return db_car
    return None


def delete_car(db: Session, car_id: int):
    # Lógica para deletar o carro do banco de dados
    db_car = db.query(Car).get(car_id)
    if db_car:
        db.delete(db_car)
        db.commit()
        return db_car
    return None

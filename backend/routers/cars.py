from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt

from repositories.CarRepository import (
    get_cars,
    get_car_by_id,
    create_car,
    update_car,
    delete_car
)
from repositories.DataBaseRepository import get_db
from services.AuthService import oauth2_scheme, SECRET_KEY, ALGORITHM
from models.CarModel import Car, CarCreation


router = APIRouter()


@router.get("/cars")
async def read_cars(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    # Lógica para obter os carros do banco de dados ordenados por valor
    cars = get_cars(db, skip=skip, limit=limit)
    return cars


@router.post("/cars/add")
async def add_car(carData: CarCreation, db: Session = Depends(get_db)):
    # Lógica para criar um novo carro no banco de dados
    db_car = create_car(db, carData)
    return {"message": db_car}


@router.get("/cars/{car_id}")
async def read_car(car_id: int, db: Session = Depends(get_db)):
    car = get_car_by_id(db, car_id)
    if car:
        return car
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carro não encontrado!")


@router.put("/cars/{car_id}")
async def update_car_route(
    car_id: int,
    updated_car: Car,
    db: Session = Depends(get_db),
    # tokenUser: str = Depends(oauth2_scheme)
):
    # payload = jwt.decode(tokenUser, SECRET_KEY, algorithms=[ALGORITHM])
    atualize_car = update_car(db, car_id, updated_car)
    if atualize_car:
        return updated_car
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carro não encontrado!")


@router.delete("/cars/{car_id}")
async def delete_car_route(
    car_id: int,
    db: Session = Depends(get_db),
    # tokenUser: str = Depends(oauth2_scheme)
):
    # payload = jwt.decode(tokenUser, SECRET_KEY, algorithms=[ALGORITHM])
    deleted_car = delete_car(db, car_id)
    if deleted_car:
        return deleted_car
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carro não encontrado!")

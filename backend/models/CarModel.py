from typing import Optional
from pydantic import BaseModel, Field


class Car(BaseModel):
    nome: str = Field(...)
    marca: str = Field(...)
    modelo: str = Field(...)
    foto: str
    valor: Optional[float]
    ano: str 
    km: Optional[str] 
    cidade: str


class CarCreation(BaseModel):
    nome: str
    marca: str
    modelo: str
    foto: str
    valor: float
    ano: str
    km: int
    cidade: str
    
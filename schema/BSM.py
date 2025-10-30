from pydantic import BaseModel
import psycopg2
from typing import Optional
from datetime import date

# Generamos el modelo de datos que debe seguir cada una de las tablas de nuestra base de datos 
# los id son y la fecha son generados automaticamente en Postgresql asi que son opcionales y fecha es tipo date igual colocada automaticamente por postgre


class Venta(BaseModel):
    id_venta: int | None = None 
    id_cliente: int | None = None 
    fecha: date | None = None 
    id_producto: int | None = None 

class Cliente(BaseModel):
    id_cliente:int | None = None
    nombre: str 
    correo: str 
    telefono: str 

class Producto(BaseModel):
    id_producto: int | None = None    
    nombre: str 
    precio: float 



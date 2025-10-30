from pydantic import BaseModel
import psycopg2
from typing import Optional
from datetime import date

# Generamos el modelo de datos que debe seguir cada una de las tablas de nuestra base de datos 
# los id son y la fecha son generados automaticamente en Postgresql asi que son opcionales y fecha es tipo date igual colocada automaticamente por postgre
# Entre parentesis tenemos los tipos y tambien la cantidas de caracteres maximos que acepta cada atributo

class Venta(BaseModel):
    id_venta: Optional[int] 
    id_cliente: Optional[int]
    fecha: Optional [date]
    id_producto: Optional[int]

class Cliente(BaseModel):
    id_cliente:Optional[int]
    nombre: str [100]
    correo: str [100]
    telefono: str [15]

class Producto(BaseModel):
    id_producto: Optional[int]    
    nombre: str [100]
    precio: float [10, 2]



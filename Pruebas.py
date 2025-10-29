from fastapi import FastAPI
from pydantic import BaseModel

# Modelo de datos de pydantic, name tipo string, description tipo string pero es opcional, precio tipo float y tax tipo float e igual opcional.
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

#Parametro de ruta y consulta en el mismo endpoint que el parametro de consulta es opcional 
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# parametros de consulta predefinidos skip y limit al pegarle a los valores enteros predefinidos de los parametros nos muestra nuestra "Base de datos completa"
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# Cuerpo de solicitud volviendo a nuestro item creado de tipo Item de la clase de pydantic definida arriba 
@app.post("/items/")
async def create_item(item: Item):
    return item
from fastapi import FastAPI
from model.Conexion import UserConnection
from schema.BSM import Cliente, Producto


app = FastAPI()
conn = UserConnection()

@app.get("/")
def root():
    conn
    return "Hola, Soy FastAPI"

@app.post("/api/insert")
def insert (cliente:Cliente, producto:Producto):
    data = cliente.model_dump()
    data.pop("id_cliente")
    conn.write(data)
    data1 = producto.model_dump()
    data.pop("id_producto")
    conn.write(data1)



from fastapi import FastAPI
from model.Conexion import UserConnection
from schema.BSM import Cliente, Producto, Venta


app = FastAPI()
conn = UserConnection()

@app.get("/cliente")
def root():
    keys = ["id", "nombre", "correo", "telefono"]
    items = []
    for data2 in conn.read_cl():
        items.append(dict(zip(keys, data2)))
    return items 

@app.get("/venta")
def root2():
    keys = ["id_venta", "id_cliente", "fecha", "id_producto"]
    items = []
    for data3 in conn.read_vt():
        items.append(dict(zip(keys, data3)))
    return items 

@app.get("/producto")
def root3():
    keys = ["id", "nombre", "precio"]
    items = []
    for data4 in conn.read_pr():
        items.append(dict(zip(keys, data4)))
    return items 

@app.post("/clientes/insert")
def insert1 (cliente:Cliente):
    data = cliente.model_dump()
    data.pop("id_cliente")
    conn.write_cl(data)

@app.post("/ventas/insert")
def insert2 (ventas:Venta):
    data = ventas.model_dump()
    data.pop("id_venta")  # si el ID es autogenerado
    id_producto = data["id_producto"]
    id_cliente = data["id_cliente"]
    conn.write_vt(id_producto, id_cliente)

@app.post("/productos/insert")
def insert3 (producto:Producto):
    data = producto.model_dump()
    data.pop("id_producto")
    conn.write_pr(data)


@app.delete("/clientes/borrar/{id_cliente}")
def delete1(id_cliente:str):
    conn.delete_cl(id_cliente)

@app.delete("/ventas/borrar/{id_venta}")
def delete1(id_venta:str):
    conn.delete_vt(id_venta)

@app.delete("/productos/borrar/{id_producto}")
def delete1(id_producto:str):
    conn.delete_pr(id_producto)


 

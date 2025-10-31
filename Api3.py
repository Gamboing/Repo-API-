from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

app = FastAPI()
Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:Hadali2203@localhost:5432/guru99")
Session = sessionmaker(bind=engine)

class ClienteDB(Base):
    __tablename__ = "clientes"
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    correo = Column(String)
    telefono = Column(String)
    ventas = relationship("VentaDB", back_populates="cliente")

class ProductoDB(Base):
    __tablename__ = "productos"
    id_producto = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    precio = Column(Float)
    ventas = relationship("VentaDB", back_populates="producto")

class VentaDB(Base):
    __tablename__ = "ventas"
    id_venta = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"))
    id_producto = Column(Integer, ForeignKey("productos.id_producto"))
    fecha = Column(Date, default=date.today)
    cliente = relationship("ClienteDB", back_populates="ventas")
    producto = relationship("ProductoDB", back_populates="ventas")

Base.metadata.create_all(engine)

class UserConnection:
    def __init__(self):
        self.session = Session()

    def read_cl(self):
        return self.session.query(ClienteDB).all()

    def read_vt(self):
        return self.session.query(VentaDB).all()

    def read_pr(self):
        return self.session.query(ProductoDB).all()

    def write_cl(self, cliente):
        c = ClienteDB(nombre=cliente.nombre, correo=cliente.correo, telefono=cliente.telefono)
        self.session.add(c)
        self.session.commit()

    def write_vt(self, venta):
        v = VentaDB(id_cliente=venta.id_cliente, id_producto=venta.id_producto)
        self.session.add(v)
        self.session.commit()

    def write_pr(self, producto):
        p = ProductoDB(nombre=producto.nombre, precio=producto.precio)
        self.session.add(p)
        self.session.commit()

    def delete_cl(self, id_cliente):
        self.session.query(ClienteDB).filter(ClienteDB.id_cliente == id_cliente).delete()
        self.session.commit()

    def delete_vt(self, id_venta):
        self.session.query(VentaDB).filter(VentaDB.id_venta == id_venta).delete()
        self.session.commit()

    def delete_pr(self, id_producto):
        self.session.query(ProductoDB).filter(ProductoDB.id_producto == id_producto).delete()
        self.session.commit()

    def update_cl(self, id_cliente, cliente):
        c = self.session.query(ClienteDB).filter(ClienteDB.id_cliente == id_cliente).first()
        if c:
            c.nombre = cliente.nombre
            c.correo = cliente.correo
            c.telefono = cliente.telefono
            self.session.commit()

    def update_pr(self, id_producto, producto):
        p = self.session.query(ProductoDB).filter(ProductoDB.id_producto == id_producto).first()
        if p:
            p.nombre = producto.nombre
            p.precio = producto.precio
            self.session.commit()

    def update_vt(self, id_venta, venta):
        v = self.session.query(VentaDB).filter(VentaDB.id_venta == id_venta).first()
        if v:
            v.id_cliente = venta.id_cliente
            v.id_producto = venta.id_producto
            self.session.commit()

    def __del__(self):
        self.session.close()

class Venta(BaseModel):
    id_venta: Optional[int] = None
    id_cliente: Optional[int] = None
    fecha: Optional[date] = None
    id_producto: Optional[int] = None

class Cliente(BaseModel):
    id_cliente: Optional[int] = None
    nombre: str
    correo: str
    telefono: str

class Producto(BaseModel):
    id_producto: Optional[int] = None
    nombre: str
    precio: float

conn = UserConnection()

@app.get("/cliente")
def root():
    return conn.read_cl()

@app.get("/venta")
def root2():
    return conn.read_vt()

@app.get("/producto")
def root3():
    return conn.read_pr()

@app.post("/clientes/insert")
def insert1(cliente: Cliente):
    conn.write_cl(cliente)

@app.post("/ventas/insert")
def insert2(ventas: Venta):
    conn.write_vt(ventas)

@app.post("/productos/insert")
def insert3(producto: Producto):
    conn.write_pr(producto)

@app.delete("/clientes/borrar/{id_cliente}")
def delete1(id_cliente: int):
    conn.delete_cl(id_cliente)

@app.delete("/ventas/borrar/{id_venta}")
def delete2(id_venta: int):
    conn.delete_vt(id_venta)

@app.delete("/productos/borrar/{id_producto}")
def delete3(id_producto: int):
    conn.delete_pr(id_producto)

@app.put("/clientes/actualizar/{id_cliente}")
def update1(id_cliente: int, cliente: Cliente):
    conn.update_cl(id_cliente, cliente)

@app.put("/productos/actualizar/{id_producto}")
def update2(id_producto: int, producto: Producto):
    conn.update_pr(id_producto, producto)

@app.put("/ventas/actualizar/{id_venta}")
def update3(id_venta: int, venta: Venta):
    conn.update_vt(id_venta, venta)


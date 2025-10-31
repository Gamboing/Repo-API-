from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

app = FastAPI()
Base = declarative_base() # Definición de la base declarativa
engine = create_engine("postgresql+psycopg2://postgres:Hadali2203@localhost:5432/guru99") # Reemplaza con tu cadena de conexión
Session = sessionmaker(bind=engine) # Crear una clase de sesión

class ClienteDB(Base): # Modelo de cliente para la base de datos
    __tablename__ = "clientes"
    id_cliente = Column(Integer, primary_key=True, autoincrement=True) # Llave primaria
    nombre = Column(String) # Nombre del cliente
    correo = Column(String) # Correo del cliente
    telefono = Column(String) # Teléfono del cliente
    ventas = relationship("VentaDB", back_populates="cliente") # Relación con ventas

class ProductoDB(Base): # Modelo de producto para la base de datos
    __tablename__ = "productos" # Nombre de la tabla
    id_producto = Column(Integer, primary_key=True, autoincrement=True) # Llave primaria
    nombre = Column(String)
    precio = Column(Float)
    ventas = relationship("VentaDB", back_populates="producto")# Relación con ventas

class VentaDB(Base): # Modelo de venta para la base de datos
    __tablename__ = "ventas"
    id_venta = Column(Integer, primary_key=True, autoincrement=True) # Llave primaria
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente")) # Llave foránea al cliente
    id_producto = Column(Integer, ForeignKey("productos.id_producto")) # Llave foránea al producto
    fecha = Column(Date, default=date.today) # Fecha de la venta
    cliente = relationship("ClienteDB", back_populates="ventas") # Relación con cliente 
    producto = relationship("ProductoDB", back_populates="ventas") # Relación con producto el back_populates significa que es bidireccional


Base.metadata.create_all(engine)# Crear las tablas en la base de datos

class UserConnection: # Clase para manejar las operaciones de la base de datos
    def __init__(self):
        self.session = Session()

    def read_cl(self): # Leer todos los clientes
        return self.session.query(ClienteDB).all() # Obtener todos los clientes

    def read_vt(self): # Leer todas las ventas
        return self.session.query(VentaDB).all()   # Obtener todas las ventas

    def read_pr(self): # Leer todos los productos
        return self.session.query(ProductoDB).all()# Obtener todos los productos

    def write_cl(self, cliente): # Escribir un nuevo cliente
        c = ClienteDB(nombre=cliente.nombre, correo=cliente.correo, telefono=cliente.telefono) # Crear un nuevo cliente comparando con el modelo de la base de datos para asignar los valores
        self.session.add(c) # Agregar el cliente a la sesión
        self.session.commit() # Confirmar los cambios

    def write_vt(self, venta):
        v = VentaDB(id_cliente=venta.id_cliente, id_producto=venta.id_producto) # Crear una nueva venta comparando con el modelo de la base de datos para asignar los valores de id_cliente e id_producto
        self.session.add(v)
        self.session.commit()

    def write_pr(self, producto):
        p = ProductoDB(nombre=producto.nombre, precio=producto.precio) # Crear un nuevo producto comparando con el modelo de la base de datos para asignar los valores
        self.session.add(p)
        self.session.commit()

    def delete_cl(self, id_cliente): # Eliminar un cliente por id
        self.session.query(ClienteDB).filter(ClienteDB.id_cliente == id_cliente).delete() # Filtrar por id_cliente y eliminar
        self.session.commit()

    def delete_vt(self, id_venta):
        self.session.query(VentaDB).filter(VentaDB.id_venta == id_venta).delete()
        self.session.commit()

    def delete_pr(self, id_producto):
        self.session.query(ProductoDB).filter(ProductoDB.id_producto == id_producto).delete()
        self.session.commit()

    def update_cl(self, id_cliente, cliente): # Actualizar un cliente por id 
        c = self.session.query(ClienteDB).filter(ClienteDB.id_cliente == id_cliente).first() # Filtrar por id_cliente y obtener el primer resultado para comparar que el cliente exista
        if c: # Si el cliente existe, actualizar los valores
            c.nombre = cliente.nombre # Actualizar 
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

    def __del__(self): # Destructor para cerrar la sesión
        self.session.close() # Cerrar la sesión al eliminar la instancia




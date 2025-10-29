# Importar la librerias necesarias
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class EstadoEnum(str, Enum):
    pendiente = "Pendiente"
    en_progreso = "En Progreso"
    completada = "Completada"

                          # Definir el modelo de datos para los endpoints
class Task(BaseModel):    # Clase llamada tarea que validara los datos ingresados
    id: int               # Identificador unico de la tarea tipo entero          
    titulo: str           # Titulo de la tarea tipo cadena de texto     
    descripcion: Optional[str] = None # Descripcion de la tarea tipo cadena de texto
    estado: EstadoEnum = EstadoEnum.pendiente  # Estado de la tarea tipo cadena de texto con valores por defecto
    fecha_creacion: datetime = Field(default_factory=datetime.now)  # Fecha de creacion de la tarea tipo datetime con valor por defecto    
    

app = FastAPI()           # Crear una instancia de la aplicacion FastAPI
tareas = {}               # Diccionario para almacenar las tareas
 
# Endpoint POST para crear una nueva tarea
@app.post("/tareas/")    # Decorador para definir el endpoint POST en la ruta /tareas/
def crear_tarea(tarea: Task):  # Funcion para crear una nueva tarea
    tareas[tarea.id] = tarea    # Agregar la tarea al diccionario de tareas
    return tarea                 # Retornar la tarea creada

# Endpoint GET que devuelve la lista de tareas completa
@app.get("/tareas/")  # Decorador para definir el endpoint GET en la ruta /tareas/
def obtener_tareas():  # Funcion para obtener la lista de tareas
    return list(tareas.values())  # Retornar la lista de tareas


# Endpoint GET para obtener una tarea por su ID 
@app.get("/tareas/{tarea_id}")  # Decorador para definir el endpoint GET en la ruta /tareas/{tarea_id}
def obtener_tarea(tarea_id: int):  # Funcion para obtener una tarea por su ID
    tarea = tareas.get(tarea_id)   # Obtener la tarea del diccionario de tareas
    if tarea:                       # Si la tarea existe
        return tarea                # Retornar la tarea
    return {"error": "Tarea no encontrada"}  # Retornar un error si la tarea no existe

# Endpoint PUT para actualizar una tarea existente
@app.put("/tareas/{tarea_id}")  # Decorador para definir el endpoint PUT
def actualizar_tarea(tarea_id: int, tarea_actualizada: Task):  # Funcion para actualizar una tarea existente
    if tarea_id in tareas:  # Si la tarea existe en el diccionario de tareas
        tareas[tarea_id] = tarea_actualizada  # Actualizar la tarea
        return tarea_actualizada               # Retornar la tarea actualizada
    return {"error": "Tarea no encontrada"}   # Retornar un error si la tarea no existe

# Endpoint DELETE para eliminar una tarea por su ID
@app.delete("/tareas/{tarea_id}")  # Decorador para definir el endpoint DELETE  
def eliminar_tarea(tarea_id: int):  # Funcion para eliminar una tarea por su ID
    if tarea_id in tareas:  # Si la tarea existe en el diccionario de tareas
        del tareas[tarea_id]  # Eliminar la tarea
        return {"mensaje": "Tarea eliminada"}  # Retornar un mensaje de confirmacion
    return {"error": "Tarea no encontrada"}    # Retornar un error si la tarea no existe

# Importor la libreria FastAPI desde fastapi
from fastapi import FastAPI
# Crear una instancia de la aplicación FastAPI
app = FastAPI()

@app.get("/")                            # Definir un endpoint GET en la ruta raíz "/" la ruta esta en el string y devuelve un json 
def root():                              # Definir la función que maneja las solicitudes a este endpoint
    return {"message": "Hello World"}    # Devolver un diccionario que se convierte automáticamente en JSON tambien es el mensaje de respuesta


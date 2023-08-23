from fastapi import FastAPI
from models import Item

# Crear una instancia de FastAPI
app = FastAPI()

# Definir una ruta para la raíz del sitio
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Ruta para recibir y imprimir un JSON mediante POST
@app.post("/items/")
def process_json(item: Item):
    print("JSON recibido:")
    print(item.json())
    return {"message": "JSON recibido y procesado"}
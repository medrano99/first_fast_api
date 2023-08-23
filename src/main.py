from fastapi import FastAPI
from models import Item

# Create an instance of FastAPI
app = FastAPI()

# Define a path for the site root
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Path to receive and print a JSON via POST
@app.post("/items/")
def process_json(item: Item):
    print("JSON recibido:")
    print(item.json())
    return {"message": "JSON recibido y procesado"}
from pydantic import BaseModel

# Pydantic model for the data in the body of the POST request
class Item(BaseModel):
    name: str
    description: str = None
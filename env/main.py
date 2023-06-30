from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Dish(BaseModel):
    index: int
    name: str
    price: float

menu = []

@app.get("/customers")
def get_customer():
    return menu

@app.post("/customers")
def add_customer(dish: Dish):
    menu.append(dish)
    return {"message": "Danie zostało dodane do menu"}

@app.delete("/customers/{dish_index}")
def remove_customer(dish_index: int):
    if dish_index >= 0 and dish_index < len(menu):
        removed_dish = menu.pop(dish_index)
        return {"message": f"Danie '{removed_dish.name}' zostało usunięte z menu"}
    else:
        return {"error": "Spróbuj ponownie"}
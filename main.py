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

@app.delete("/customers/{customer_id}")
def remove_customer(customer_id: int):
    if customer_id >= 0 and customer_id < len(menu):
        removed_dish = menu.pop(customer_id)
        return {"message": f"Danie '{removed_dish.name}' zostało usunięte z menu"}
    else:
        return {"error": "Spróbuj ponownie"}
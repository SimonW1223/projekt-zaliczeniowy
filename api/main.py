from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Przykładowa baza danych klientów
customers = [
    {
        'id': 1,
        'name': 'John Doe',
        'email': 'john@example.com'
    },
    {
        'id': 2,
        'name': 'Jane Smith',
        'email': 'jane@example.com'
    }
]

# Model danych klienta
class Customer(BaseModel):
    id: int
    name: str
    email: str

# Endpoint do dodawania klientów
@app.get('/customers')
def add_customer(customer: Customer):
    customers.append(customer.dict())
    return {'message': 'Klient dodany pomyślnie.'}

# Endpoint do edytowania klientów
@app.put('/customers/{customer_id}')
def edit_customer(customer_id: int, customer: Customer):
    for idx, cust in enumerate(customers):
        if cust['id'] == customer_id:
            customers[idx] = customer.dict()
            return {'message': 'Klient zaktualizowany pomyślnie.'}
    return {'message': 'Nie znaleziono klienta o podanym ID.'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
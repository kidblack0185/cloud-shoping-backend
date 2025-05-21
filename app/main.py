from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users, products, orders

app = FastAPI(title="Nuvem Shop UDI - Backend")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)


from .db import models, database
from lib2to3.pytree import Base
from fastapi import FastAPI, HTTPException, status


stores = database.generate_store_db()
products = database.generate_product_db()
inventory = database.generate_inventory_db()

app = FastAPI()

@app.get("/stores")
def get_stores():
    return stores

@app.get("/stores/{store}")
def get_store(store: str):
    return

@app.post("/stores")
def add_store(store: models.Store):
    return

@app.delete("/stores/{store}")
def delete_store(store: str):
    return

@app.get("/products")
def get_products():
    return products

@app.get("/products/{product}")
def get_products(product: str):
    return

@app.get("/products")
def get_products(product: str):
    return
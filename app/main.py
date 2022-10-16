from lib2to3.pytree import Base
from fastapi import FastAPI, HTTPException, status

from .db import models
from .api import api

app = FastAPI()

@app.get("/stores")
def get_stores():
    return api.all_stores()

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
    return api.all_products()

@app.get("/products/{product}")
def get_products(product: str):
    return

@app.get("/products")
def get_products(product: str):
    return
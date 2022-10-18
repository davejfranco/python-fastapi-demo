#from lib2to3.pytree import Base
from curses.ascii import HT
from fastapi import FastAPI, HTTPException

from .db import models
from .api import api

app = FastAPI()

#Stores
@app.get("/stores")
def get_stores():
    return api.all_stores()

@app.get("/stores/{id}")
def get_store(id: int):
    req = api.store_by_id(id)
    if req != {}:
        return req
    raise HTTPException(status_code=404, detail="Store not found")

@app.post("/stores", status_code=201)
def add_store(store: models.Store):
    try:
        api.add_new_store(store)
    except Exception as err:
        raise HTTPException(status_code=422, detail=err)


@app.delete("/stores/{id}", status_code=201)
def delete_store(id: int):
    try:
        api.delete_store(id)
    except IndexError:
        raise HTTPException(status_code=404, detail="store not found")
    except Exception as err:
        raise HTTPException(status_code=422, detail=err)
  

@app.get("/products")
def get_products():
    return api.all_products()

@app.get("/products/{product}")
def get_products(product: str):
    return

@app.get("/products")
def get_products(product: str):
    return
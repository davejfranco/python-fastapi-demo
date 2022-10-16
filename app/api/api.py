from app.db import database

stores = database.generate_store_db()
products = database.generate_product_db()
inventory = database.generate_inventory_db()

def all_stores():
    return stores

def all_products():
    return products

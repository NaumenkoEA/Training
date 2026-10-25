from typing import Callable, TypedDict


class Product(TypedDict):
    name : str 
    price : float 
    in_stock : bool


product = {
    "name": "Laptop",
    "price": 1200,
    "in_stock": True
}

def get_product_name(product: Product) -> str:
    return product["name"]

def get_expensive_products(products: list[Product]) -> list[Product]:
    return [product for product in products if product["price"] >= 1000]


def get_most_expensive(products: list[Product]) -> Product | None:
    if not products:
        return None
    return max(products , key= lambda product : product["price"])

def get_available_products(products: list[Product]) -> list[Product]:
    return [product for product in products if product["in_stock"]]

def get_available_expensive_products(products: list[Product]) -> list[Product]:
    return [product for product in products if product["in_stock"] and product["price"] >= 1000]

def apply_discount(product: Product, discount: float) -> Product:
    product["price"] = product["price"] * (1-discount)
    return product

def apply_discount_copy(product: Product, discount: float) -> Product:
    product_copy = product.copy()
    product_copy["price"] = product_copy["price"] * (1-discount)
    return product_copy
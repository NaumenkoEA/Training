from typing import Callable, TypedDict


class Product(TypedDict):
    name : str 
    price : float 
    in_stock : bool

def is_expensive(product: Product) -> bool:
    return product["price"] >= 1000


def filter_products(
    products: list[Product],
    condition: Callable[[Product], bool]
) -> list[Product]:
    return [product for product in products if condition(product)]

def is_available(product: Product) -> bool:
    return product["in_stock"]

def is_good_product(product: Product) -> bool:
    return product["in_stock"] and product["price"] < 2000 and product["price"] >500


def get_products(
        products : list[Product],
        condition : Callable[[Product], bool]
) -> list[Product]:
    return [product for product in products if condition(product)]
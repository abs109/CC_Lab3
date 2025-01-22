import json

import products
from cart import dao
from products import Product


class Cart:
    def _init_(self, cart_id: int, user_name: str, cart_contents: list[Product], total_cost: float):
        self.cart_id = cart_id
        self.user_name = user_name
        self.cart_contents = cart_contents
        self.total_cost = total_cost

    @staticmethod
    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(user_name: str) -> list:
    cart_records = dao.get_cart(user_name)
    if not cart_records:
        return []
    
    items = []
    for record in cart_records:
        contents = record.get('contents', '[]')
        items.extend(json.loads(contents))

    products_list = []
    for item_id in items:
        product = products.get_product(item_id)
        products_list.append(product)
    return products_list


def add_to_cart(user_name: str, product_id: int):
    dao.add_to_cart(user_name, product_id)


def remove_from_cart(user_name: str, product_id: int):
    dao.remove_from_cart(user_name, product_id)


def delete_cart(user_name: str):
    dao.delete_cart(user_name)

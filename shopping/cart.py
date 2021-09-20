from shopping import item
from shopping.item import Item


class Cart:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.items = []

    def add(self, one_item: item.Item):
        self.items.append(one_item)

    def __add__(self, item_name, item_price, item_quantity):
        one_item = Item(item_name, item_price, item_quantity)
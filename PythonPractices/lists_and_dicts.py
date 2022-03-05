new_items = {"new": 2, "old": 1}
print(new_items)

stuff = {"my_world": "GOD", "my_name": "Martha"}
new_items.update(stuff)
print(new_items)
new_items.update(food="money")
print(new_items)

new_items.pop("food")
print(new_items)

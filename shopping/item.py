class Item:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def calculate_total(self):
        return self.__price * self.__quantity

    def __str__(self):
        return str(self.__name) + "\t\t\t" + str(self.__price) + "\t\t\t" + str(self.__quantity)
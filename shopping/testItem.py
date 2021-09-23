from unittest import TestCase
from shopping.item import Item


class TestItem(TestCase):
    def test_calculate_total(self):
        item = Item("Puff puff", 5, 2)
        self.assertEqual(10, item.calculate_total(), "Not true")

    def test_to_string(self):
        item = Item("Puff puff", 5, 2)
        self.assertEqual("Puff puff			5			2", item.__str__(), "Not true")


        # %-3s
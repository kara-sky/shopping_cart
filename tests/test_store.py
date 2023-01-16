import unittest

from product import Product
from store import Store


class TestStore(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Test Product 1", "Test Description 1", 20, "test1.jpg")
        self.product2 = Product("Test Product 2", "Test Description 2", 25, "test2.jpg")
        self.store = Store()

    def test_add_product(self):
        self.store.add_product(self.product1)
        self.assertEqual(self.store.products, [self.product1])
        self.store.add_product(self.product2)
        self.assertEqual(self.store.products, [self.product1, self.product2])

    def test_list_products(self):
        self.store.add_product(self.product1)
        self.store.add_product(self.product2)
        self.assertEqual(self.store.list_products(), [self.product1, self.product2])

    def test_get_product(self):
        self.store.add_product(self.product1)
        self.store.add_product(self.product2)
        self.assertEqual(self.store.get_product("Test Product 1"), self.product1)
        self.assertIsNone(self.store.get_product("Non Existing Product"))

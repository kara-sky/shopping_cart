import unittest

from models.customer import Customer
from models.discount import Discount
from models.order import Order
from models.product import Product


class TestDiscount(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Test Product 1", "Test Description 1", 20, "test1.jpg")
        self.product2 = Product("Test Product 2", "Test Description 2", 25, "test2.jpg")
        self.customer = Customer("John Doe", "john.doe@example.com")
        self.items = [self.product1, self.product2]
        self.total_price = 45
        self.order = Order(self.customer, self.items, self.total_price)
        self.discount = Discount("WELCOME10", 10)

    def test_apply_discount(self):
        self.discount.apply_discount(self.order)
        self.assertEqual(self.order.total_price, 40.5)

    def test_discount_code(self):
        self.assertEqual(self.discount.code, "WELCOME10")

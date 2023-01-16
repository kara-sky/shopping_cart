import datetime
import unittest

from customer import Customer
from order import Order
from product import Product


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Test Product 1", "Test Description 1", 20, "test1.jpg")
        self.product2 = Product("Test Product 2", "Test Description 2", 25, "test2.jpg")
        self.customer = Customer("John Doe", "john.doe@example.com")
        self.items = [self.product1, self.product2]
        self.total_price = 45
        self.order = Order(self.customer, self.items, self.total_price)

    def test_order_attributes(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.items, self.items)
        self.assertEqual(self.order.total_price, self.total_price)
        self.assertIsNotNone(self.order.order_number)
        self.assertIsInstance(self.order.date, datetime.datetime)

    def test_string_representation(self):
        expected_string = f"Order number: {self.order.order_number}\nCustomer: {self.customer.name}\nTotal price: {self.total_price}\nItems: {self.items}"
        self.assertEqual(str(self.order), expected_string)

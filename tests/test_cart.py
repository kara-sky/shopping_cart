import unittest

from models.cart import Cart
from models.customer import Customer
from models.order import Order
from models.product import Product


class TestCart(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Test Product 1", "Test Description 1", 20, "test1.jpg")
        self.product2 = Product("Test Product 2", "Test Description 2", 25, "test2.jpg")
        self.customer = Customer("John Doe", "john.doe@example.com")
        self.payment_info = {'card_number': '4111111111111111', 'expiry_date': '12/25', 'cvv': '123'}
        self.cart = Cart()

    def test_add_item(self):
        self.cart.add_item(self.product1)
        self.assertEqual(self.cart.items, [self.product1])
        self.cart.add_item(self.product2)
        self.assertEqual(self.cart.items, [self.product1, self.product2])

    def test_remove_item(self):
        self.cart.add_item(self.product1)
        self.cart.add_item(self.product2)
        self.cart.remove_item(self.product1)
        self.assertEqual(self.cart.items, [self.product2])

    def test_checkout(self):
        self.cart.add_item(self.product1)
        self.cart.add_item(self.product2)
        order = self.cart.checkout(self.customer, self.payment_info)
        self.assertIsInstance(order, Order)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.items, [self.product1, self.product2])
        self.assertEqual(order.total_price, 45)

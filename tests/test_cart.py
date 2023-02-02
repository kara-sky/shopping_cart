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
        self.cart = Cart(self.customer)

    def test_add_item(self):
        self.cart.add_item(self.product1)
        self.assertEqual(self.cart.items, [self.product1])
        self.assertEqual(self.cart.total_price, self.product1.price)

        self.cart.add_item(self.product2)
        self.assertEqual(self.cart.items, [self.product1, self.product2])
        self.assertEqual(self.cart.total_price, self.product1.price + self.product2.price)

    def test_remove_item(self):
        self.cart.add_item(self.product1)
        self.cart.add_item(self.product2)
        self.cart.remove_item(self.product1)
        self.assertEqual(self.cart.items, [self.product2])
        self.assertEqual(self.cart.total_price, self.product2.price)

    def test_find_item_by_name(self):
        cart = Cart("Test Customer")
        product1 = Product("Test Product 1", "Test Description 1", 20, "test1.jpg")
        product2 = Product("Test Product 2", "Test Description 2", 25, "test2.jpg")
        cart.add_item(product1)
        cart.add_item(product2)

        # Test finding an existing item
        found_item = cart.find_item_by_name("Test Product 1")
        self.assertIsNotNone(found_item)
        self.assertEqual(found_item.price, 20)

        # Test finding a non-existing item
        found_item = cart.find_item_by_name("Item 3")
        self.assertIsNone(found_item)

    def test_checkout(self):
        self.cart.add_item(self.product1)
        self.cart.add_item(self.product2)
        order = self.cart.checkout(self.payment_info)
        self.assertIsInstance(order, Order)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.items, [self.product1, self.product2])
        self.assertEqual(order.total_price, 45)

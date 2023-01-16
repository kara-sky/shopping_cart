import unittest

from models.product import Product


class TestProduct(unittest.TestCase):
    def test_product_attributes(self):
        product = Product("Test Product", "Test Description", 20, "test.jpg")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Test Description")
        self.assertEqual(product.price, 20)
        self.assertEqual(product.image, "test.jpg")

    def test_update_price(self):
        product = Product("Test Product", "Test Description", 20, "test.jpg")
        product.update_price(25)
        self.assertEqual(product.price, 25)

    def test_string_representation(self):
        product = Product("Test Product", "Test Description", 20, "test.jpg")
        self.assertEqual(str(product), "Test Product - Test Description - 20")

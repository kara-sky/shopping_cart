import unittest

from models.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John Doe", "john.doe@example.com")

    def test_customer_attributes(self):
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.email, "john.doe@example.com")

    def test_string_representation(self):
        self.assertEqual(str(self.customer), "John Doe - john.doe@example.com")

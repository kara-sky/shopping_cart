import datetime
import uuid


class Order:
    def __init__(self, customer, items, total_price):
        self.customer = customer
        self.items = items
        self.total_price = total_price
        self.order_number = self._generate_order_number()
        self.date = datetime.datetime.now()

    def _generate_order_number(self):
        # generate a unique order number
        return str(uuid.uuid4())

    def __str__(self):
        return f"Order number: {self.order_number}\nCustomer: {self.customer.name}\nTotal price: {self.total_price}\nItems: {self.items}"

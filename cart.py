from order import Order
from payment import Payment


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def checkout(self, customer, payment_info):
        total_price = sum(item.price for item in self.items)
        order = Order(customer, self.items, total_price)
        payment = Payment()
        payment.process_payment(order, payment_info)
        return order

from models.order import Order
from models.payment import Payment
from models.store import Store


class Cart:
    def __init__(self, customer):
        self.items = []
        self.customer = customer
        self.total_price = 0
        self.store = Store()

    def add_item(self, item):
        self.items.append(item)
        self.total_price += item.price

    def remove_item(self, item):
        self.items.remove(item)
        self.total_price -= item.price

    def find_item_by_name(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def checkout(self, payment_info):
        order = Order(self.customer, self.items, self.total_price)
        payment = Payment()
        payment.process_payment(order, payment_info)
        return order

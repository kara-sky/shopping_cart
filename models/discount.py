class Discount:
    def __init__(self, code, percentage):
        self.code = code
        self.percentage = percentage

    def apply_discount(self, order):
        order.total_price = order.total_price - (order.total_price * self.percentage / 100)

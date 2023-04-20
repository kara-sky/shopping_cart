class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def __str__(self):
        return f"{self.name} - {self.email}"

    def add_order(self, order):
        # This method adds an order to the customer's list of orders
        self.orders.append(order)
        print(f"Order {order.id} placed successfully!")

    def view_order_history(self):
        # This method displays the customer's order history
        print(f"Order history for {self.name}:")
        for order in self.orders:
            print(f"  Order {order.id}: {order.status}")

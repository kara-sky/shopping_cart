class Product:
    def __init__(self, name, description, price, image):
        self.name = name
        self.description = description
        self.price = price
        self.image = image

    def __str__(self):
        return f"{self.name} - {self.description} - {self.price}"

    def update_price(self, price):
        self.price = price

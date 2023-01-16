class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        return self.products

    def get_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return True
        return False

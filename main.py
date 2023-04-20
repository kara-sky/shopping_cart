from cart import Cart
from customer import Customer
from discount import Discount
from order import Order
from payment import Payment
from product import Product
from store import Store

if __name__ == "__main__":
    # Create some products
    product1 = Product("Test Product 1", "Test Description 1", 20, "test1.jpg")
    product2 = Product("Test Product 2", "Test Description 2", 25, "test2.jpg")
    product3 = Product("Test Product 3", "Test Description 3", 30, "test3.jpg")

    # Create a customer
    customer = Customer("John Doe", "john.doe@example.com")

    # Create a store
    store = Store()
    store.add_product(product1)
    store.add_product(product2)
    store.add_product(product3)

    # Create a cart
    cart = Cart(customer)
    cart.add_item(product1)
    cart.add_item(product2)
    cart.add_item(product3)

    # Create discount
    discount = Discount("WELCOME10", 10)
    discount.apply_discount(cart)

    # Create an order
    order = Order(customer, cart.items, cart.total_price)

    # Process payment
    payment = Payment()
    payment_info = {'card_number': '4111111111111111', 'expiry_date': '12/25', 'cvv': '123'}
    payment.process_payment(order, payment_info)

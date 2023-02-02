from behave import *

from models.cart import Cart
from models.customer import Customer
from models.product import Product
from models.store import Store

@given("the store \"FinOps Store\" exists")
def step_impl(context):
    context.store = Store()

@given("a customer exists as a member of this store")
def step_impl(context):
    context.customer = Customer("John Doe", "john.doe@example.com")

@step("the customer has an empty cart")
def step_impl(context):
    context.cart = Cart(context.customer)

@given('a product with name "{name}" exists')
def step_impl(context, name):
    product = Product(name, "Test Description", 20, "test.jpg")
    context.store.add_product(product)

@when('the customer clicks on the "Add to Cart" button for "{name}"')
def step_impl(context, name):
    product = context.store.get_product(name)
    context.cart.add_item(product)

@then('the product "{name}" should be added to the customer\'s shopping cart')
def step_impl(context, name):
    product = context.cart.find_item_by_name(name)
    assert product is not None
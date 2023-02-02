Feature: Shopping Cart Product Management

Story:
  As a customer
  I want to be able to add products into shopping cart
  So that I can checkout the products I want

Background:
  Given the store "FinOps Store" exists
  Given a customer exists as a member of this store
  Given a product with name "Product 1" exists
  And a product with name "Product 2" exists
  And a product with name "Product 3" exists

Scenario: Add product to cart
  Given the customer has an empty cart
  When the customer clicks on the "Add to Cart" button for "Product 1"
  Then the product "Product 1" should be added to the customer's shopping cart
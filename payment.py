class Payment:
    def process_payment(self, order, payment_info):
        card_number = payment_info['card_number']
        expiry_date = payment_info['expiry_date']
        cvv = payment_info['cvv']

        # Perform validation and processing of payment
        # This is where you would call an external service to process the payment
        # or implement your own payment processing logic
        # For this example, I will just simulate a successful payment
        success = True

        if success:
            print("Payment successful!")
            order.status = "PAID"
            return True
        else:
            print("Payment failed!")
            order.status = "FAILED"
            return False

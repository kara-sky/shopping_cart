import asyncio
import aiohttp


class Payment:

    def __init__(self, store, config):
        self.store = store
        self.payment_gateway_url = config.get("payment_gateway_url", "https://payment-gateway/charge")
        self.retry_attempts = config.get("retry_attempts", 3)
        self.retry_interval = config.get("retry_interval", 5)

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

    async def place_order(self, order, payment_info):
        for attempt in range(self.retry_attempts):
            async with aiohttp.ClientSession() as session:
                try:
                    response = await asyncio.wait_for(session.post(self.payment_gateway_url, json=payment_info), self.retry_interval)
                    if response.status == 200:
                        order.status = 'PAID'
                        self.store.orders.append(order)
                        break
                except asyncio.TimeoutError:
                    # retry
                    pass
        else:
            raise Exception("Failed to place order after max number of retries")

# This is "Task B" - an urgent, unrelated bug fix.

class PaymentGateway:
    def __init__(self, api_key: str):
        self.api_key = api_key
        if not api_key:
            raise ValueError("API Key is required")

    def process_payment(self, amount: float, card_token: str):
        print(f"Processing payment of ${amount} for {card_token}...")

        # BUG: This should be amount > 0
        if amount <= 0:
            print("Invalid amount.")
            return False

        # The presenter will open this file and add a
        # BREAKPOINT on the line below while Task B is active.

        print(f"Connecting to payment gateway with key {self.api_key}...")

        # ... complex payment logic ...

        print("Payment successful.")
        return True


if __name__ == "__main__":
    gw = PaymentGateway("key_live_12345")
    gw.process_payment(100.0, "tok_visa")
    gw.process_payment(-50.0, "tok_mastercard")  # This should fail
# This file handles payment processing.

import logging
from ..models.user import User

logger = logging.getLogger(__name__)

# TODO: Integrate with a real payment gateway like Stripe or PayPal
# This entire file is a simulation.
API_ENDPOINT = "https://api.fake-payment-gateway.com/v1/charge"


class PaymentError(Exception):
    """Custom exception for payment failures."""
    pass


def process_payment(user: User, amount: float):
    """
    Simulates processing a payment via an external API.
    """

    # FIXME: No validation is done on the 'amount'
    # This check is good, but what about a max amount?
    if amount <= 0:
        logger.warning(f"Payment failed for {user.username}: Amount must be positive.")
        return False

    if amount > 10000:
        # TODO: Add a manual review process for large transactions
        logger.warning(f"Payment for {user.username} of ${amount} requires manual review.")
        # For now, we'll let it pass...

    logger.info(f"Processing payment of ${amount} for {user.username}...")

    # --- Simulate API Call ---
    # The presenter will add the custom REVIEW comment on this line:
    # REVIEW: Should we add fraud detection logic here?

    try:
        # Pretend to make an HTTP request
        print(f"POST {API_ENDPOINT} with amount {amount}")

        # Simulate a potential failure
        if user.username == "fraud_user":
            raise PaymentError("User is flagged for fraud.")

        print("... API call successful.")

    except PaymentError as e:
        logger.error(f"Payment failed for {user.username}: {e}")
        return False
    except Exception as e:
        # FIXME: This is too broad. We should catch specific
        # network errors (e.g., requests.exceptions.Timeout)
        logger.error(f"A network error occurred during payment: {e}")
        return False
    # --- End Simulate API Call ---

    logger.info(f"Payment of ${amount} for {user.username} successful.")

    # TODO: Log this transaction to a separate 'transactions' database table

    return True


def issue_refund(user: User, transaction_id: str, amount: float):
    """
    Simulates processing a refund for a user.
    """
    # TODO: Implement the refund logic
    # - Check if transaction_id is valid
    # - Check if amount <= original transaction
    # - Call the gateway's refund API
    logger.info(f"REFUND: Issuing ${amount} to {user.username} for tx_id={transaction_id}...")

    # FIXME: This is not implemented at all!
    pass
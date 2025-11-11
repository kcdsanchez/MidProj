# This is the main entry point for our "large" project.

import sys
import logging

from .models.user import User
from .models.product import Product
from .api.payment import process_payment
from .utils.caching import get_from_cache

# --- Setup Logging ---
# In a real app, this would be more complex
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# TODO: Load configuration from a .env file or config.ini instead of hardcoding
CONFIG = {
    'db_host': 'localhost',
    'db_port': 5432,
    'api_key': '12345-ABCDE'
}


class Application:
    """
    Main application class to encapsulate the app logic.
    """

    def __init__(self, config):
        self.config = config
        self.users = {}
        self.products = {}
        logger.info("Application initialized.")

        # TODO: Implement a proper database connection pool
        # For now, we just simulate a connection
        self.db_connection = f"connected_to_{config['db_host']}"

    def load_initial_data(self):
        """
        Loads initial data into the application.
        In a real app, this would query a database.
        """
        logger.info("Loading initial data...")

        u1 = User("test_user", "password123", "test@example.com")
        p1 = Product("Laptop", 1200.00, "SKU-LT-001", 50)
        p2 = Product("Mouse", 45.00, "SKU-MS-002", 200)

        self.users[u1.username] = u1
        self.products[p1.sku] = p1
        self.products[p2.sku] = p2

        logger.info(f"Loaded {len(self.users)} users and {len(self.products)} products.")

    def run_purchase_flow(self, username, product_sku, quantity):
        """
        Simulates a full user purchase flow.
        """
        logger.info(f"Starting purchase flow for user '{username}'...")

        user = self.users.get(username)
        product = self.products.get(product_sku)

        if not user:
            logger.error(f"User '{username}' not found.")
            return

        if not product:
            logger.error(f"Product '{product_sku}' not found.")
            return

        # Check cache first
        # TODO: This caching logic is too simple, needs proper invalidation
        cached_price = get_from_cache(f"price_{product_sku}")

        if cached_price:
            price = cached_price
            logger.info("Loaded price from cache.")
        else:
            price = product.price

        if not product.is_in_stock(quantity):
            logger.warning(f"Not enough stock for {product.name}.")
            return

        # FIXME: This is a terrible way to calculate total.
        # This should be handled by an Order or Cart class.
        total_amount = price * quantity

        # Process the payment
        success = process_payment(user, total_amount)

        if success:
            product.update_stock(quantity * -1)  # Reduce stock
            logger.info(f"Purchase successful for {user.username}!")
        else:
            logger.error(f"Purchase failed for {user.username}.")


def main():
    """Main function to run the application."""
    try:
        app = Application(CONFIG)
        app.load_initial_data()
        app.run_purchase_flow("test_user", "SKU-LT-001", 1)
        app.run_purchase_flow("test_user", "SKU-MS-002", 500)  # This one should fail
    except Exception as e:
        logger.critical(f"A critical error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
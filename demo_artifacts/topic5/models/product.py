# This file defines the Product model.

import datetime


class Product:
    """
    Represents a Product in the system's inventory.
    """

    def __init__(self, name, price, sku, inventory_count):
        self.name = name

        # FIXME: 'price' should be stored as an integer (cents)
        # to avoid floating-point arithmetic errors.
        self.price = price
        self.sku = sku
        self.inventory_count = inventory_count
        self.created_at = datetime.datetime.now()
        self.is_archived = False

    def get_details(self):
        """
        Returns a dictionary of the product's public details.
        """
        # TODO: Add product description, images, and categories
        return {
            'name': self.name,
            'price': self.price,
            'sku': self.sku,
            'stock': self.inventory_count
        }

    def update_stock(self, quantity_change: int):
        """
        Updates the inventory count for this product.
        'quantity_change' can be positive (stocking) or negative (selling).
        """
        # TODO: Add validation to ensure stock doesn't go below zero
        # if quantity_change < 0 and (self.inventory_count + quantity_change) < 0:
        #    raise ValueError("Not enough stock.")

        print(f"Updating stock for {self.sku} by {quantity_change}...")
        self.inventory_count += quantity_change

        # REVIEW: Should this method return the new stock count?
        # Or just return True/False?

        return self.inventory_count

    def is_in_stock(self, quantity_needed=1):
        """
        Checks if a given quantity of the product is in stock.
        """
        return self.inventory_count >= quantity_needed

    def archive(self):
        """
        Archives a product, making it unavailable for sale.
        """
        # FIXME: Archiving should probably also set inventory_count to 0
        self.is_archived = True
        print(f"Product '{self.name}' has been archived.")

    def __repr__(self):
        return f"<Product {self.name} ({self.sku})>"
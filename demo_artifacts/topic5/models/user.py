# This file defines the User model.

import datetime
import hashlib


class User:
    """
    Represents a User in the system.
    This would typically map to a 'users' table in a database.
    """

    def __init__(self, username, password, email):
        # FIXME: BIG SECURITY RISK! Passwords should never be stored in plain text.
        # We must hash this password before storing it.
        # This is a critical vulnerability.
        self.username = username
        self.password = self.hash_password(password)  # Let's pretend to fix it
        self.email = email
        self.created_at = datetime.datetime.now()
        self.is_active = True

        print(f"User '{username}' created.")

    def hash_password(self, password):
        """
        Hashes a password for secure storage.
        """
        # In a real app, use a proper library like passlib with salt
        # TODO: Implement proper salting per-user. This is still not secure.
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password_to_check):
        """
        Checks if a given password matches the stored hash.
        """
        return self.hash_password(password_to_check) == self.password

    def get_profile(self):
        """
        Returns a dictionary of the user's public profile.
        """
        # TODO: Add user profile fields (e.g., first_name, last_name, bio)
        return {
            'username': self.username,
            'email': self.email,
            'member_since': self.created_at.isoformat()
        }

    def deactivate_account(self):
        """
        Flags a user account as inactive.
        """
        # FIXME: This is not enough. We also need to log them out,
        # invalidate their sessions/tokens, and possibly anonymize data.
        self.is_active = False
        print(f"User '{self.username}' has been deactivated.")

    def get_order_history(self):
        """
        Fetches the user's order history from the database.
        """
        # TODO: Implement database query to fetch orders
        # This requires connecting to the Order model/service.
        print(f"Simulating DB query for {self.username}'s orders...")

        # The presenter will add the custom REVIEW comment on this line:

        return []  # Return empty list for now

    def __repr__(self):
        return f"<User {self.username} ({self.email})>"
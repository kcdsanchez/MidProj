# This is "Task C" - a different, less urgent task.
# e.g., A teammate asked you to review their code.

class UserLogin:
    def __init__(self, db_connection):
        self.db = db_connection

    def login(self, username, password):
        print(f"Attempting login for {username}...")

        # The presenter will just open this file to create
        # a simple context for "Task C".

        user_record = self.db.find(username)
        if user_record and user_record.password == password:
            print(f"Login successful for {username}.")
            return True
        else:
            print("Login failed.")
            return False

# ... other code ...
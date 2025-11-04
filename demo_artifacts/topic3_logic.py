# This is the artifact for Topic 3: Integrated Testing (Code to be tested)

class Calculator:
    """A simple calculator class to be tested."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            return None
        return a / b
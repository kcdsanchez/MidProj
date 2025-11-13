# This is the artifact for Topic 1: Advanced Code Generation & Formatting

class Customer:
    # STEP 5: Demo reformatting here
    def __init__(self, name: str, level: str):
        self.name = name;
        self.level = level;
        k = 20;i = 21;r = 22;k = 23 #Bad Formatting

def get_customer_from_db(customer_id: int, include_history: bool):
    pass


def main_app():
    print("Welcome to the E-commerce System v1.0")  # <-- Topic 5 will change this

    # STEP 1: Demo object completion below this line
    c1 = Customer("Aaron", "Platinum")
    c2 = Customer("Mj", "Diamond")
    c3 = Customer("Kirk", "Bronze")




if __name__ == "__main__":
    main_app()




# This is the main artifact for the Topic 5 TODO demo

def calculate_payment(amount, user_level):
    # FIXME: This is broken for 'guest' users
    if user_level == 'guest':
        # This logic is wrong
        return amount * 0.9

    # The presenter will add the REVIEW comment here during the demo
    return amount * (1.0 - get_discount(user_level))


def get_discount(level):
    if level == 'gold':
        return 0.2
    return 0.1


print("Running main.py")

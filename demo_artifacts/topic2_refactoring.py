# This is a simpler artifact for Topic 2: Code Refactoring & Analysis

def calculate_total_bill(q, p, user_status):

    subtotal = q * p
    discount_rate = 0.0
    if user_status == 'GOLD':
        discount_rate = 0.15
    elif user_status == 'SILVER':
        discount_rate = 0.05

    discount_amount = subtotal * discount_rate
    discounted_total = subtotal - discount_amount


    if user_status == 'GOLD':
        shipping = 0.0
    elif user_status == 'SILVER':
        shipping = 2.50
    elif user_status == 'BRONZE':
        shipping = 5.00
    else:
        shipping = 5.00

    final_bill = discounted_total + shipping

    return final_bill


# This is a simpler artifact for Topic 2: Code Refactoring & Analysis

# STEP 2: Rename 'q' to 'quantity'
# STEP 3: Rename 'p' to 'price'
def calculate_total_bill(q, p, user_status):

    subtotal = q * p
    discount_rate = 0.0
    if user_status == 'GOLD':
        discount_rate = 0.15
    elif user_status == 'SILVER':
        discount_rate = 0.05

    discount_amount = subtotal * discount_rate
    discounted_total = subtotal - discount_amount


    # STEP 4: Select this entire block to Extract Method
    if user_status == 'GOLD':
        shipping = 0.0
    elif user_status == 'SILVER':
        shipping = 2.50
    # STEP 1: Show Code Inspection warning on the line below
    elif user_status == 'BRONZE':
        shipping = 5.00
    else:
        shipping = 5.00
    # --- End of selection ---

    final_bill = discounted_total + shipping

    return final_bill


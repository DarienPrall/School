"""
This program calculates the total price based on quantity purchased and unit proce.
The program will calculate the total price for you after we calculate discount, taxes, and shipping cost.
Discount is 3% if the gross cost is less than $100
Discount is 5% if the gross cost is $100 or higher
Shipping cost is 2% of the gross amount after the discount
"""


# FUNCTION 1: TO RUN THE MAIN PROGRAM (CALLS ON ALL 7 OF THE FUNCTIONS)
def main_function():
    tax_rate = 0.06
    unit_price, quantity = prompt_user()
    gross_cost = calculate_gross_cost(unit_price, quantity)
    discount_amount = calculate_discount(gross_cost)
    price_after_discount = gross_cost - calculate_discount(gross_cost)
    tax_amount = calculate_tax(price_after_discount, tax_rate)
    shipping_amount = calculate_shipping(price_after_discount)
    price = calculate_price(gross_cost, discount_amount, tax_amount, shipping_amount)
    print_results(gross_cost, discount_amount, shipping_amount, tax_amount, price)

# FUNCTION 2: FOR PROMPTING THE USER FOR THE UNIT PRICE AND QUANTITY
def prompt_user():
    unit_price = float(input("How much did the item cost?: $"))
    quantity = int(input("How many did you buy?: "))
    return unit_price, quantity

# FUNCTION 3: TO CALCULATE THE GROSS COST
def calculate_gross_cost(unit_price, quantity):
    gross_cost = unit_price * quantity
    return gross_cost

# FUNCTION 4: TO CALCULATE THE DISCOUNT AMOUNT
def calculate_discount(gross_cost):
    if gross_cost >= 100:
        discount_amount = gross_cost * 0.05
    else:
        discount_amount = gross_cost * 0.03
    return discount_amount

# FUNCTION 5: TO CALCUALTE THE TAX AFTER DISCOUNTS ARE APPLIED
def calculate_tax(price_after_discount, tax_rate):
    tax_amount = price_after_discount * tax_rate
    return tax_amount

# FUNCTION 6: TO CALCULATE SHIPPING AFTER DISCOUNTS ARE APPLIED
def calculate_shipping(price_after_discount):
    shipping_amount = price_after_discount * 0.02
    return shipping_amount

# FUNCTION 7: TO CACLCULATE THE TOTAL COST OF THE TRANSACTION
def calculate_price(gross_cost, discount_amount, tax_amount, shipping_amount):
    price = (gross_cost - discount_amount) + tax_amount + shipping_amount
    return price

# FUNCTION 8: TO DISPLAY THE RESULTS TO THE USER
def print_results(gross_cost, discount_amount, shipping_amount, tax_amount, price):
    print(f"Original Price: ${gross_cost:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Total cost after discount: ${gross_cost - discount_amount:.2f}")
    print(f"Tax Amount: ${tax_amount:.2f}")
    print(f"Cost Including Taxes: ${gross_cost - discount_amount + tax_amount:.2f}")
    print(f"Shipping Amount: ${shipping_amount:.2f}")
    print(f"Total Cost: ${(gross_cost - discount_amount) + tax_amount + shipping_amount:.2f}")
    print(f"Program Ended, have a good day from Darien Prall")

main_function()

    


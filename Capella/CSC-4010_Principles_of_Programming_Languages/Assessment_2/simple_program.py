# For this program, I wanted to include input checking to ensure that the user is entering the correct information
# It starts with an infinite loop while True: which will continuosly ask the user of the unit price or quantity untill they enter a positive integer greater than 0. 
# The user will likely enter a price that is a float (e.g., 2.99)
# Loop 1 start
while True: 
    # Prompts the user for the cost
    unit_price = input("How much did the item cost?: $")
    # Begins the input validation
    # The user can enter a float and it will remove the decimal. By removing the decimal, it now becomes and int
    # For example: 12.99 is a float and becomes 1299 and int.
    # The .isdigit checks if the 1299 is a digit and if the float of unit price (12.99) is greater than 0/
    if unit_price.replace('.', '', 1).isdigit() and float(unit_price) > 0:
        # If it meets the if conditions, it stores the unit_price as a float rather than a string (what the user entered)
        unit_price = float(unit_price)
        # This allows the infinite loop to stop
        break
    else:
        # If the user does not meet the conditions, it will throw an error for the user to correct.
        print("Invalid unit price. Please enter a positive integer greater than 0.")


# The same logic is applied to the following while loop
while True:
    quantity = input("How many did you purchase?: ")
    if quantity.isdigit() and int(quantity) > 0:
        quantity = int(quantity)
        break
    else:
        print("Invalid quantity. Please enter a positive integer greater than 0.")

# Now that we have the unit price and quantity, we can do simple math
total_cost = unit_price * quantity

# We can set the discount rate based on the defined variables using an if statement
if total_cost >= 100:
    discount_rate = 0.05
else:
    discount_rate = 0.03

# Complete some basic mathematical calculations
discount_total = total_cost * discount_rate
amount_due = total_cost - discount_total

# Output the results in a readable format. This output allows for variables to be printed to the console using f.
print(f"You purchased {quantity} items at ${unit_price}.\nYour total comes to ${total_cost:.2f}\nYour discount rate is {discount_rate * 100}%\nYou saved ${discount_total:.2f}\nYour total amount due today is ${amount_due:.2f}")

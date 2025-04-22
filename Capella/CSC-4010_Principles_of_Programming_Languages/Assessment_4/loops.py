def calculate_mortgage():
    print("*** Mortgage Calculation Program by Darien Prall ***\n")
    print("This program is going to calculate the mortgage payment\n")
    print("It will ask you to enter mortgage amount")   

    mortgage_amount = get_positive_number("Enter the Mortgage amount ")
    number_of_years = get_positive_number("Enter the number of years ")
    interest_rate = get_positive_number("Enter the rate as % ")

    interest_rate_decimal = interest_rate / 100
    years_to_months = number_of_years * 12

    yearly_payment = mortgage_amount * (interest_rate_decimal * (1 + interest_rate_decimal) ** number_of_years) / ((1 + interest_rate_decimal) ** number_of_years - 1)
    total_interest = (yearly_payment * number_of_years) - mortgage_amount
    sum_of_years_digits = sum(range(1, number_of_years + 1))

    print(f"Yearly pay ${yearly_payment:.2f}")
    print(f"Total Interest ${total_interest:.2f}")
    print(f"Sum of years digits {sum_of_years_digits}\n")
    print(f"{'Year':<5} {'Starting Balance':<20} {'Year Interest':<15} {'Principle Paid':<15} {'Ending Balance':<20}")

    starting_balance = mortgage_amount
    total_principle_paid = 0

    for year in range(1, number_of_years + 1):
        interest_paid = starting_balance * interest_rate_decimal
        principle_paid = yearly_payment - interest_paid
        ending_balance = starting_balance - principle_paid

        print(f"{year:5} {starting_balance:15,.2f} {interest_paid:15,.2f} {principle_paid:15,.2f} {ending_balance:15,.2f}")

        starting_balance = ending_balance
        total_principle_paid += principle_paid

    print(f"Ending Balance: ${starting_balance:,.2f}\nTotal interest paid: ${total_interest:,.2f}\nTotal principle paid: ${total_principle_paid:,.2f}\n>>>")

def get_positive_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        else:
            print("Invalid input. Please enter a positive number greater than 0.")

calculate_mortgage()


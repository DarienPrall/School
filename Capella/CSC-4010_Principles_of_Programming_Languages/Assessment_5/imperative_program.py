"""
Program Week 5
Menu Driven Program for basic operations
Darien Prall
"""
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by 0."
    return x / y

def remainder(x, y):
    return x % y

operations = {
    "1": add,
    "2": subtract,
    "3": multiply,
    "4": divide,
    "5": remainder
}

def menu():
    exitflag = "N"
    print ("\n**** Welcome to the basic calculator program by Darien Prall ****")
    print ("program to perform the operations of Add, Subtract, Multiple, divide and remainder")
    while exitflag == "N":
        print
        print("Select Operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Remainder")

        choice = input("\nEnter Choice ")
        if choice in operations:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))

            result = operations[choice](num1, num2)
            print(f"The result is {result}")
            exitflag = input("Do you wish to exit Y or N ")
        else:
            print("Invalid Input ")
    print("Program ended, have a good day")

menu()

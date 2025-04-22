"""
INTRODUCTION TO THE PROGRAM
In this program, the user will be presented with a menu offering three choices

1. Calculate the factorial of a number
- If the user chooses the factorial option, the user will have to enter a non-negative integer, and the program computes its factorial recursively.

2. Solve the Tower of Hanoi Puzzle
- If the user chooses the Tower of Hanoi Puzzle, the user will enter the number of disks and rod labels (source, target, auxiliary) and the program will output the move instructions to solve the puzzle.

3. Exit the program
- If the user chooses this, the program is terminated
"""

def factorial_recursive(n):
    if n == 0 or n == 1:
        print("Reached base case with n=", n, ": returning 1")
        return 1
    else:
        print("Calculating factorial(", n, ") as", n, "* factorial(", n - 1, ")")
        return n * factorial_recursive(n - 1)

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", target)
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print("Move disk", n, "from rod", source, "to rod", target)
    tower_of_hanoi(n - 1, auxiliary, target, source)

def display_menu():
    print("\nRecursive Program Demonstration")
    print("1. Calculate Factorial")
    print("2. Solve Tower of Hanoi")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-3): ")

        if choice == "1":
            num = int(input("Enter a number to calculate its factorial: "))
            if num < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print("The factorial of", num, "is:", factorial_recursive(num))

        elif choice == "2":
            disks = int(input("Enter the number of disks: "))
            source_rod = input("Enter the source rod (e.g., A): ")
            target_rod = input("Enter the destination rod (e.g., B): ")
            auxiliary_rod = input("Enter the auxiliary rod (e.g., C): ")
            print("\nTower of Hanoi solution for", disks, "disks:")
            tower_of_hanoi(disks, source_rod, target_rod, auxiliary_rod)

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

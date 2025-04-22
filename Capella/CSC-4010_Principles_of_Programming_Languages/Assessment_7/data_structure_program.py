# Each data structure example will be placed in a seperate function to make it easier to call when in a list of the user

# LIST EXAMPLE [MATCHING THE POWERPOINT SLIDE]
def show_list_example():
    # CREATING AND SHOWING THE LIST
    fruits = ['Apple', 'Banana', 'Strawberry']
    print("The original list of fruits is:", fruits)

    # PROMPTING THE USER FOR A NEW FRUIT AND APPENDING IT TO THE LIST
    new_fruit = input("Enter new fruit: ")
    fruits.append(new_fruit)
    print("The fruit list after adding the fruit you entered:", fruits)

    # DELETING A FRUIT BY CHECKING IF ITS IN THE LIST AND REMOVING IT IF IT IS, OTHERWISE LET THE USER KNOW ITS NOT IN THE LIST
    fruit_to_delete = input("Enter fruit to delete: ")
    if fruit_to_delete in fruits:
        fruits.remove(fruit_to_delete)
        print("The fruit list after deleting the fruit entered is:", fruits)
    else:
        print(f"{fruit_to_delete} is not in the list.")

# TUPLE EXAMPLE [MATCHING THE POWERPOINT SLIDE]
def show_tuple_example():
    # CREATING AND SHOWING THE TUPLE
    fruits_tuple = ('Apple', 'Banana', 'Strawberry')
    print("The original tuple of fruits is:", fruits_tuple)
    print("Fruit at index 1:", fruits_tuple[1])

# SET EXAMPLE [MATCHING THE POWERPOINT SLIDE]
def show_sets_example():
    # CREATING AND SHOWING THE SET
    states = {'California', 'Alabama', 'Arkansas', 'Pennsylvania'}
    print("The original set of states is:", states)

    # ALLOWS THE USER TO ADD A NEW STATE TO THE SET BY USING THE .ADD FUNCTION OF SETS
    new_state = input("Enter name of new state: ")
    states.add(new_state)
    print("Updated states in the set:", states)

    # SIMILAR TO THE LIST, THIS ALLOWS THE USER TO DELETE A STATE FROM THE SET BY USING THE .REMOVE FUNCTION OF SETS, OTHERWISE TELL THE USER THE STATE IS NOT IN THE SET
    state_to_delete = input("Enter name of state to delete: ")
    if state_to_delete in states:
        states.remove(state_to_delete)
        print("Updated states in the set after deletion:", states)
    else:
        print(f"{state_to_delete} is not in the set.")

# DICTIONARY EXAMPLE [MATCHING THE POWERPOINT SLIDE]
def show_dictionary_example():
    # CREATING THE DICTIONARY
    city_info = {
        'city1': 'Berlin', 
        'country1': 'Germany', 
        'population1': 364500, 
        'city2': 'London', 
        'country2': 'England', 
        'population2': 14500721
    }
    # SHOWING THE DICTIONARY IS DIFFERENT FROM THE OTHER DATA STRUCTURES AS WE NEED TO USE THE KEY AND VALUES TO SHOW ALL ITEMS
    print("Printing city info using dictionary:")
    print(city_info.keys())
    print(city_info.values())
    print("City1:", city_info['city1'])
    print("Country1:", city_info['country1'])
    print("Population1:", city_info['population1'])
    print("City2:", city_info['city2'])
    print("Country2:", city_info['country2'])
    print("Population2:", city_info['population2'])

# CREATING THE MAIN FUNCTION FOR THE USER MENU THAT WILL TRIGGER A SPECIFIED FUNCTION [BASED ON POWERPOINT SLIDE]
def main():
    print("This program gives a practice on using data structures in Python.")
    print("1. For List Example")
    print("2. For Tuple Example")
    print("3. For Sets Example")
    print("4. For Dictionary Example")
    print("5. For Exit")

    # THIS IS AN INFINITE LOOP THAT WILL BREAK OUT IF THE USER CHOOSES OPTION 5, OTHERWISE, IT WILL CONTINUE TO ASK THE USER WHAT THEY WOULD LIKE TO DO
    while True:
        choice = int(input("Select one of the options above: "))

        if choice == 1:
            show_list_example()
        elif choice == 2:
            show_tuple_example()
        elif choice == 3:
            show_sets_example()
        elif choice == 4:
            show_dictionary_example()
        elif choice == 5:
            print("Program ended, have a good day!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()

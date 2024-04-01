'''
2. The Shopping List Maker
Objective:
The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.
Task 2: Include a feature to remove items from the list.
Task 3: Add a function that prints out the entire list in a formatted way.
'''
shopping_list = []

def add_to_list(user_add):
    global shopping_list
    shopping_list.append(user_add)

def remove_from_list(user_remove):
    global shopping_list
    shopping_list.remove(user_remove)

def print_list():
    global shopping_list
    print("\nThis is your current list:\n")
    for i in shopping_list:
        print(f"{i}\n")


while True:
    user_operation = input("Welcome! Would you like to [A]dd to list, [R]emove from list, [V]iew your list, or [Q]uit? ").upper()

    if user_operation == 'A':
        user_added = input("Great! What would you like to add to your shopping list? ")
        add_to_list(user_added)
    elif user_operation == 'R':
        user_removed = input("What would you like to remove from your shopping list? ")
        remove_from_list(user_removed)
    elif user_operation == 'V':
        print_list()
    elif user_operation == 'Q':
        break
    else:
        print("Invalid choice! Please try again.")


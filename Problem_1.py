'''1. The Calculator App
Objective:
The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

Task 1: Create functions for each arithmetic operation.
Task 2: Implement user input to receive numbers and an operation choice.
Task 3: Ensure your program can handle division by zero and other potential errors.'''

def addition(number_1, number_2):
    return number_1 + number_2
    

def subtraction(number_1, number_2):
    return number_1 - number_2


def multiplication(number_1, number_2):
    return number_1 * number_2


def division(number_1, number_2):
    return number_1 / number_2

user_operation = input("Welcome to the calculator!\nPlease decide between: [A]ddition, [S]ubtraction, [M]ultiplication, or [D]ivision\n").upper()
user_num1 = float(input("What is the first value you would like?\n"))
user_num2 = float(input("What is the second value you would like?\n"))

if user_operation == 'A':
    add_result = addition(user_num1, user_num2)
    print(f"Your final value is: {add_result}")
elif user_operation == 'S':
    sub_result = subtraction(user_num1, user_num2)
    print(f"Your final value is: {sub_result}")
elif user_operation == 'M':
    m_result = multiplication(user_num1, user_num2)
    print(f"Your final value is: {m_result}")
elif user_operation == 'D':
    if user_num2 == 0:
        print("Your second number can't be zero, sorry! Try again.")
    else:
        d_result = division(user_num1, user_num2)
        print(f"Your final value is: {d_result:.2f}")
else:
    print("Invalid choice!")
              









    
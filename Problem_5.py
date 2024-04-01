'''
5. The Fitness Tracker
Objective:
The aim of this assignment is to create a program that tracks fitness activities and calories burned.

Task 1: Develop a function to log different fitness activities and their duration. 
For instance, activities = [Dancing, Swimming, Biking] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, 
Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.

Task 2: Write a simple function that estimates calories burned based on the activity and duration. 
For instance, Total calories burned = Duration (in minutes)*3.5

Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.
'''

activities = ["Dancing", "Swimming", "Biking"]
duration = [10, 20, 15]

def log_fitness():
    global activities
    global duration

    user_workout = input("What workout would you like to add? ")
    activities.append(user_workout)
    user_duration = int(input("Great! How long was the workout for?(minutes) "))
    duration.append(user_duration)


def cals_burned():
    global duration
    total_calories = 0
    for i in range(len(duration)):
        total_calories = total_calories + duration[i]
    total_calories = total_calories * 3.5
    print(f"You have made amazing progress! You already burned {total_calories} calories!")


def summary():
    global activities
    global duration
    for i in range(len(activities)):
        print(f"\nActivity: {activities[i]} / Time Spent: {duration[i]} minutes")
    print("\n")

while True:
    user_answer = input("Welcome to the fitness tracker! Would you like to [L]og your workout, view [C]alorie estimations, view your [S]ummary, or [Q]uit? ").upper()

    if user_answer == 'L':
        log_fitness()
    elif user_answer == 'C':
        cals_burned()
    elif user_answer == 'S':
        summary()
    elif user_answer == 'Q':
        print("Great work today! Hope to see you soon!")
        break
    else:
        print("Invalid selection. Please try again!")
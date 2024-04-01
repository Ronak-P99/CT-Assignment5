'''
3. The Grade Analyzer
Objective:
The aim of this assignment is to analyze a set of grades and provide statistics.

Task 1: Code a function to calculate the average grade.
Task 2: Implement a function to find the highest and lowest grade.
Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
'''

def average_grade(grade):
    i = 0
    addition = 0
    while i < len(grade):
       addition = addition + grade[i]
       i = i + 1
    average = addition / len(grade)
    print(f"\nAverage grade comes out to: {average:.2f}")

def high_low(grade):
    highest_grade = max(grade)
    lowest_grade = min(grade)

    print(f"\nThe highest grade is: {highest_grade}")
    print(f"The lowest grade is: {lowest_grade}\n")



def letter_grades(grades):
    for grade in grades:
        if grade <= 100 and grade >= 90:
            print(f"Your grade is a {grade} which is an A!")
        elif grade < 90 and grade >= 80:
            print(f"Your grade is a {grade} which is a B!")
        elif grade < 80 and grade >= 70:
            print(f"Your grade is a {grade} which is a C!")
        elif grade < 70 and grade >= 60:
            print(f"Your grade is a {grade} which is a D!")
        else:
            print(f"Your grade is a {grade} which is a F!")
    print("\n")



grades = [90, 80, 56, 74, 100, 83, 84, 66, 77]

average_grade(grades)
high_low(grades)
letter_grades(grades)




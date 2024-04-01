'''
4. The Quiz Game
Objective:
The aim of this assignment is to create a quiz game that asks questions and checks answers.

Task 1: Develop a list of questions and answers.
Task 2: Write a function that quizzes the user and takes their answers.
Task 3: Score the quiz and give the user feedback on their performance.
'''

questions = [
    "What is 5 + 4?",
    "Kobe Bryant was a football player?(True/False)",
    "What did Isaac Newton Discover?",
    "What is 45 * 2?"
]
answers = [9, False, "Gravity", 90]
type_ans = [int, bool, str, int]

def quiz_user():
    global questions
    global answers
    global type_ans
    score = 0

    for i in range(len(questions)):
        user_answer = input(questions[i] + " ")
        try:
            if type_ans[i] == bool:
                converted_answer = user_answer.upper() in ["false", 'f', "no", '0', 'n']
            else:
                converted_answer = type_ans[i](user_answer)
            
            if converted_answer == answers[i]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
        except ValueError:
            print("Invalid Value Type!")
    print(f"Great job on your quiz! You received a score of {score}/{len(questions)}")
        

user_decision = input("Welcome to the quiz, are you ready to begin?(y/n) ").upper()

if user_decision == 'Y':
    quiz_user()
else:
    print("Please come back whenever you have time!")


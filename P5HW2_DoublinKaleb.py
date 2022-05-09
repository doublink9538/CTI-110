# MathQuizHW
# 04/14/2022
# CTI-110 P5HW2 - Math Quiz
# Kaleb Doublin
#
import random

def additionQuiz():
    X = random.randint(1,1000)
    Y = random.randint(1,1000)

    print("  {}\n+ {}\n------".format(X,Y))
    userAnswer = int(input(" "))
    correctAnswer = X + Y
    if userAnswer == correctAnswer:
        print("Congratulations!")
    else:
        print("Wrong answer!")
        print("Correct answer is: {}".format(correctAnswer))

def subtractionQuiz():
    X = random.randint(1,1000) 
    Y = random.randint(1,1000) 

    print("  {}\n- {}\n------".format(X,Y))
    userAnswer = int(input("  "))
    correctAnswer = X - Y
    if userAnswer == correctAnswer:
        print("Congratulations!")
    else:
        print("Wrong answer!")
        print("Correct answer is: {}".format(correctAnswer))

runProgram = True
while runProgram:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")
    userChoice = int(input("Enter your choice: "))
    if userChoice == 1:
        additionQuiz()
    elif userChoice == 2:
        subtractionQuiz()
    elif userChoice == 3:
        runProgram = False 

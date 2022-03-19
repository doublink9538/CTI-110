# Debugging HW Assignment 
# Doublin

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    # TO DO: define the rest of the scores

    
    score = int(input('Enter grade: '))

    if(score > A_score):
        print('Your grade is: A')
    elif(score > B_score and score < A_score):
        print('Your grade is: B')
    elif(score > C_score and score < B_score):
        print('Your score is: C')
    elif (score > D_score and score < C_score): 
        print('Your score is: D')
    else:
        print('Your grade is: F') # TO DO: finish this







# program start
main()

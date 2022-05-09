#ScoreListProject
#04/10/2022
#CTI-110 P5HW1 - Score List
#Kaleb Doublin
#

def displayMenu():
    print("---------------MENU--------------------")
    print("1) Create Score List")
    print("2) Display results")
    print("3) Exit")
    print("---------------------------------------")

def getMenuChoiceFromUser():    
    valdChoice = False
    while valdChoice == False:
        userChoice = input("Enter your choice: ")
        if userChoice in ['1', '2', '3']:
            valdChoice = True
        else:
            print("Invalid choice entered.Enter a vaid choice")
            displayMenu()
            valdChoice = False
    return userChoice
        
def isValidNumber(number):
    try:
        number = int(number)
        return True
    except ValueError:
        print("Enter a numeric value")
        return False
    
def createScoreList():
    scoreList = []
    validScoreCount = False
    while validScoreCount == False:    
        scoreCount = input("Enter the number of score you want to enter: ")  
        if isVaidNumber(scoreCount):
            scoreCount = int(scoreCount)
            if scoreCount > 0:            
                validScoreCount = True
            else:
                print("Invalid Entry.Enter a positive number greater than zero")
                validScoreCount = False
        else:
            validScoreCount = False
    
    validScore = False
    for i in range(scoreCount):
        validScore = False
        while validScore == False:
            score = input("Enter the #{} score: ".format(i+1))
            if isVaidNumber(score):
                score = float(score)
                if (score >=0 and score <= 100):
                    validScore = True                    
                    scoreList.append(score)
                else:
                    print("Invalid Score Entered.Valid score is a number between 0 and 100")
                    validScore = False
            else:
                validScore = False
    return scoreList

def evaluateScoreList(scoreList):
    lowestScore = float("Inf")
    for score in scoreList:
        if score <= lowestScore:
            lowestScore = score
    scoreList.remove(lowestScore)    
    averageScore = sum(scoreList) / len(scoreList)
    averageScore = round(averageScore, 2)    
    gradeLetter = ""
    if averageScore >= 0 and averageScore <= 35:
        gradeLetter = "F"
    elif averageScore > 35 and averageScore <= 50:
        gradeLetter = "E"
    elif averageScore > 50 and averageScore <= 60:
        gradeLetter = "D"
    elif averageScore > 60 and averageScore <= 70:
        gradeLetter = "C"
    elif averageScore > 70 and averageScore <= 80:
        gradeLetter = "B"
    elif averageScore > 80 and averageScore <= 90:
        gradeLetter = "A"
    elif averageScore > 90:
        gradeLetter = "A+"
    return scoreList, lowestScore, averageScore, gradeLetter
        
userEnteredScoreList = []
exitProgram = False            
while (exitProgram == False):
    displayMenu() 
    choice = getMenuChoiceFromUser()    
    if choice == '1':        
        userEnteredScoreList = createScoreList()        
    elif choice == '2':              
        if len(userEnteredScoreList) > 0:    
            modifiedScorelist, lowScore, avgScore, gradeLtr = evaluateScoreList(userEnteredScoreList)
            print("The score list after removing the lowest score is {}".format(userEnteredScoreList))
            print("The Lowest Score entered is", lowScore)
            print("The Average of score entered is", avgScore)
            print("The Grade Letter is", gradeLtr)
        else:
            print("No Score Entered.Enter a score to display the results")
    elif choice == '3':       
        print("Good Bye Have a nice Day!!!")
        exitProgram = True

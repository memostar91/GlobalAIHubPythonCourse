#Final project of course
import numpy as np
import pandas as pd
#Questions
question1 = "What is the capital city of Turkey? "
question2 = "What is the capital city of Japan? "
question3 = "What is the capital city of Russia? "
question4 = "What is the capital city of United States of America? "
question5 = "What is the capital city of England? "
question6 = "What is the capital city of Germany? "
question7 = "What is the capital city of Mexico? "
question8 = "What is the capital city of Indonesia? "
question9 = "What is the capital city of Malaysia? "
question10 = "What is the capital city of China? "
#Answer Key
answer1 = "Ankara"
answer2 = "Tokyo"
answer3 = "Moscow"
answer4 = "Washington D.C."
answer5 = "London"
answer6 = "Berlin"
answer7 = "Mexico City"
answer8 = "Jakarta"
answer9 = "Kuala Lumpur"
answer10 = "Beijing"
#Asking user for answers
while True:
    userAnswer1 = input("What is the capital city of Turkey? ").title()
    userAnswer2 = input("What is the capital city of Japan? ").title()
    userAnswer3 = input("What is the capital city of Russia? ").title()
    userAnswer4 = input("What is the capital city of United States of America? ").title()
    userAnswer5 = input("What is the capital city of England? ").title()
    userAnswer6 = input("What is the capital city of Germany? ").title()
    userAnswer7 = input("What is the capital city of Mexico? ").title()
    userAnswer8 = input("What is the capital city of Indonesia? ").title()
    userAnswer9 = input("What is the capital city of Malaysia? ").title()
    userAnswer10 = input("What is the capital city of China? ").title()
    break
print("*********")
#Evaluating score
score = 0
if userAnswer1 == answer1:
    score = score + 1
if userAnswer2 == answer2:
    score = score + 1
if userAnswer3 == answer3:
    score = score + 1
if userAnswer4 == answer4:
    score = score + 1
if userAnswer5 == answer5:
    score = score + 1
if userAnswer6 == answer6:
    score = score + 1
if userAnswer7 == answer7:
    score = score + 1
if userAnswer8 == answer8:
    score = score + 1
if userAnswer9 == answer9:
    score = score + 1  
if userAnswer10 == answer10:
    score = score + 1

#Showing question and answer table
questionList = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10,]
answerList = [answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10]
userAnswerList = [userAnswer1, userAnswer2, userAnswer3, userAnswer4, userAnswer5, userAnswer6, userAnswer7, userAnswer8, userAnswer9, userAnswer10]
checkMark = []
scoreList = []
for i in range(10):
    if answerList[i] == userAnswerList[i]:
        checkMark.append('\u2705')
        scoreList.append(str(10))
    else:
        checkMark.append('\u274C')
        scoreList.append(str(0))
data = {"Correct Answer": answerList, "User's answer": userAnswerList, "Check Mark": checkMark, "Score":scoreList}
tableList = [questionList, answerList, userAnswerList]
table = pd.DataFrame(data, index=[questionList])
print(table)
print("___________________________")
#Result text
if score <= 5:
    print("Unsuccessful... Score: " + str(score *10))
    print("You have answered only " + str(score) + " questions correctly. Better luck next time.")
elif score == 10:
    print("Congratulations!!! Score: " + str(score *10))
    print("You have answered all questions correctly.")
else:
    print("Congratulations!!! Score: " + str(score *10))
    print("You have answered " + str(score) + " questions correctly.")

#end
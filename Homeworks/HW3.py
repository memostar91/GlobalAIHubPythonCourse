#Homeword Day 3
#Creating Dictionary of 5 Students' Exam Scores

#Dictionary created by user input, passing grade calculated automatically and added to it
studentDict = {}
for i in range(2):
    name = input("Student's Name: ")
    midterm = int(input("Midterm Score: "))
    project = int(input("Project Score: "))
    finals = int(input("Final Score: "))
    passingGrade = int((midterm+project)*0.3 + finals*0.4)

    studentDict[name] = {
        "Midterm Score" : midterm,
        "Project Score" : project,
        "Final Score" : finals,
        "Passing Grade" : passingGrade
    }

print(studentDict)

#Sorting whole dictionary by passing grade
studentDictSortedByPassingGrade = sorted(studentDict.items(), key=lambda item: item[1]["Passing Grade"], reverse=True)
print(studentDictSortedByPassingGrade)

#Student name and passing grade transferred into a list and sorted by passing grade
scoreList = []
for k, v in studentDict.items():
    scoreList.append([k, int(studentDict[str(k)]["Passing Grade"])])

def order(x):
    return(sorted(x, key=lambda x: x[1]))

studentListSortedByPassingGrade = sorted(scoreList)
print(studentListSortedByPassingGrade)

#end
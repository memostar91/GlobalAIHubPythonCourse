#Homework Day 1
#List of even numbers
list1 = [i for i in range(20) if i % 2 == 0]
#List of odd numbers
list2 = [i for i in range(20) if i % 2 != 0]
#---Range could be any number---

#Merging lists and sorting
mergedList = list1 + list2
mergedList.sort()

#Multiplying values by 2 in merged list
multipliedList = [i*2 for i in mergedList]
print(multipliedList)

#Data types of values in multipliedList
for i in multipliedList:
    print(type(i))
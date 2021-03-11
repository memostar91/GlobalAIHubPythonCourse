#Homework Day 2
#CV Application

#Necessary modules
import random as rnd
from faker import Faker

#---Creating name list---
fake = Faker(['tr_TR'])
nameList = {}
for x in range(1,6):
	nameList["Person{0}".format(x)] = fake.name()
#print(nameList)

#---Creating age list---
ageList = {}
for x in range(1,6):
	ageList["Person{0}".format(x)] = rnd.randint(25,50)
#print(ageList)

#---Creating address list---
addressList = {}
for x in range(1,6):
	addressList["Person{0}".format(x)] = fake.address()


print(addressList)

#---Creating id number list---
idNoList = {}
for x in range(1,6):
	idNoList["Person{0}".format(x)] = fake.ssn()
#print(idNoList)

#---Creating job list---
jobSet = ("Java Developer", "Web Developer", "Python Developer", "R Developer", "Software Engineer")
jobList = {}
for x in range(1,6):
	jobList["Person{0}".format(x)] = jobSet[x-1]
#print(jobList)

#---CV automation---
CV = [idNoList, nameList, ageList, jobList, addressList]
CVs = {}
for i in nameList.keys():
	CVs[i]= tuple(CVs[i] for CVs in CV)
#print(CVs)

for i, var in CVs.items():
	print(str(i) + ":	ID Number: " + str(var[0]) + "\n		Full Name: " + str(var[1]) + "\n		Age: " + str(var[2]) + "\n		Job: " + str(var[3]) + "\n		Address: " + str(var[4]))



for i, var in CVs.items():
	print(str(i) + ":	ID Number: " + str(var[0]) + " Full Name: " + str(var[1]) + " Age: " + str(var[2]) + " Job: " + str(var[3]) + " Address: " + str(var[4]))






CV1 = {}


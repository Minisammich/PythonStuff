import random
from datetime import datetime

#Gets current time in seconds
time = datetime.now()
timeAtRun = "%s:%s:%s" %(time.hour, time.minute, time.second)

def randNum(randMin,randMax,numOfNums):
    num = 0
    for i in range(numOfNums):
        num += random.randint(randMin,randMax)
    return(num)

randNumList = []
randNumList2 = []
randNumDict = {}
outputStr = ""
numSets = int(input("Number of Sets of Dice to roll: "))
set = int(input("Number of Dice per Set: "))
numSides = int(input("Number of Sides per Die: "))

for i in range(numSets):
    randNumList.append(randNum(1, numSides, set))


randNumList.sort()
for i in randNumList:
    if i not in randNumList2:
        randNumList2.append(i)
for i in randNumList2:
    randNumDict.update({i: randNumList.count(i)})
for key, value in randNumDict.items():
    outputStr += (str(key) + "   -   " + str(value) + "\n") #Formats the characters and counts.
print(outputStr)

timeAtFinish = "%s:%s:%s" %(time.hour, time.minute, time.second)

f=open("dice_sim-results.txt","a+")
f.write("\n---%s---%s--- \nSum of %s %s-Sided Dice - Repetitions/%s\n\n%s \n" %(timeAtRun, timeAtFinish, set, numSides, numSets, outputStr))
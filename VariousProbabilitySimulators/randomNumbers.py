import random
from datetime import datetime

#Gets current time in seconds
time = datetime.now()
timeAtRun = "%s:%s:%s" %(time.hour, time.minute, time.second)

def randNum(randMin,randMax,numOfNums):
    numList = []
    for i in range(numOfNums):
        numList.append(random.randint(randMin,randMax))
    return(numList)

randNumList = randNum(1,6,2)
randNumInt = 0

for i in randNumList:
    randNumInt += i

print(randNumList,"\n",randNumInt, "\n")

f=open("random-results.txt","a+")
f.write("\n---%s---\nList Of Random Numbers: %s \nSum Of List: %s \n" %(timeAtRun, randNumList, randNumInt))
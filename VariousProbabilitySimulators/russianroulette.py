import random
from datetime import datetime
from pathlib import Path

#This is the path the rr-results.txt file will save to.
results_path = '/home/minisammich/Documents/GitHub/PythonStuff/VariousRandomSimulators/rr-results.txt'

simulations = int(input('Input # of Simulations to run: '))

infolist = []
infolist2 = []
infodict = {}
dead = False
count = 0
chamber = [0,0,0,0,0,0]
outputstring = ""

#Gets current time in seconds
time = datetime.now()
seconds = time.second
minutes = time.minute * 60
hours = time.hour * 3600
time_start = seconds + minutes + hours

for i in range(simulations):
    count = 1
    dead = False
    chamber = [0,0,0,0,0,0]
    rand1 = random.randint(0,5)
    rand2 = random.randint(0,5)
    while rand2 == rand1:
        rand2 = random.randint(0,5)
    chamber[rand1] = 1
    chamber[rand2] = 1
    while dead == False:
        if chamber[random.randint(0,5)] == 1:
            dead = True
            infolist.append(count)
        else:
            count +=1

#Gets the current time and compares it to the start time to get total time played.
    time_end = datetime.now()
    sec_end = time_end.second
    min_end = time_end.minute * 60
    hour_end = time_end.hour * 3600
    time2_end = sec_end + min_end + hour_end
    time_played = time2_end - time_start
    simtime = time_played
    #Converts 60 seconds into a minute, and 60 minutes into an hour.
    if time_played >= 60:
      simulation_seconds = time_played % 60
      simulation_minutes = int(time_played / 60)
    else:
      simulation_seconds = time_played
      simulation_minutes = 0

#Gets current time in seconds
ptime = datetime.now()
pseconds = ptime.second
pminutes = ptime.minute * 60
phours = ptime.hour * 3600
ptime_start = pseconds + pminutes + phours

infolist.sort()
for i in infolist:
    if i not in infolist2:
        infolist2.append(i)
for i in infolist2:
    infodict.update({i: infolist.count(i)})
for key, value in infodict.items():
    outputstring += (str(key) + " - " + str(value) + "\n") #Formats the characters and counts.
print(outputstring)

#Gets the current time and compares it to the start time to get total time played.
ptime_end = datetime.now()
psec_end = ptime_end.second
pmin_end = ptime_end.minute * 60
phour_end = ptime_end.hour * 3600
ptime2_end = psec_end + pmin_end + phour_end
processing_time = ptime2_end - ptime_start
processing_minutes = 0
processing_seconds = processing_time
#Converts 60 seconds into a minute, and 60 minutes into an hour.
if processing_time >= 60:
    processing_seconds = processing_time % 60
    processing_minutes = int(processing_time / 60)
    
else:
    processing_seconds = processing_time
    processing_minutes = 0

if time_played !=0:
    simspersec = simulations/simtime
else:
    simspersec = "inf"
print("Simulation Finished in %sm %ss with a sim/s of %s" %(simulation_minutes, simulation_seconds,simspersec))
print("Data Processing took %sm %ss" %(processing_minutes, processing_seconds))
totalmin = simulation_minutes+processing_minutes
totalsec = simulation_seconds+processing_seconds
if totalsec >= 60:
    totalsec -= 60
    totalmin += 1
print("Total time taken was %sm %ss" %((totalmin, totalsec)))
with open(results_path, 'a') as results:
    results.write("\n------------------\n%s\nSimulation of size %s Finished in %sm %ss with a sim/s of %s\nData Processing took %sm %ss" %(outputstring, simulations, simulation_minutes, simulation_seconds,simspersec, processing_minutes, processing_seconds))
#f.write("\n------------------\n%s\nSimulation of size %s Finished in %sm %ss with a sim/s of %s\nData Processing took %sm %ss" %(outputstring, simulations, simulation_minutes, simulation_seconds,simspersec, processing_minutes, processing_seconds))
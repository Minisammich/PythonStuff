f = open("D:\SharedFolders\Documents\GitHub\PythonStuff\Other\keylog.txt" , "r")

lines = [0]
hits = []
counter = 0
narrow = []

for line in f:
    line = line.strip().lower()
    lines.append(line)
    if lines[counter] == "t" and lines[counter-1] == "s":
        hits.append([counter,lines[counter-4],lines[counter-3],lines[counter-2],lines[counter-1],lines[counter]])

    if counter > 7170 and counter < 7230:
        narrow.append(line)
        
    counter += 1
    
print(hits)
print(narrow)
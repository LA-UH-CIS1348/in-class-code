file = open("combatlog.txt","r")
lines = file.readlines()#reads each line into a string and stores them in a list

for line in lines:
    print(line.strip())

#print(lines)

file.close()

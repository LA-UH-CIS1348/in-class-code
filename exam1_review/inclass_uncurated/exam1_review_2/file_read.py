#FILE READ (reads entire file) -> READ ENTIRE CONTENTS INTO A STRING
file = open("combatlog.txt","r")
contents = file.read()
print(contents)
file.close()

#FILE READLINES (reads entire file) -> MAKE A LIST OF ALL THE LINES IN THE FILE
file = open("combatlog.txt","r")
lineslist = file.readlines()
print(lineslist)
file.close()

#FILE READ LINES DIRECTLY FROM THE FILE ONE AT A TIME
#could be useful when file is VERY large
file = open("combatlog.txt","r")
for line in file:
    print(line)
file.close()
#THESE ARE FUNCTIONS I USE OFTEN

def getlineslongerthanK(filename, k):
    f = open(filename, "r")
    a = f.readlines()
    b = []
    for line in a:
        strippedline = line.strip()
        if len(strippedline) >= k:
            b.append(strippedline)
    f.close()
    return b


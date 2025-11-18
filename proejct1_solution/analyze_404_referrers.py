import sys
inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

f = open(inputfilename,"r")
lines = f.readlines()

dictionary = {}
for line in lines:
    parts = line.split('"')
    returncode = parts[2].strip().split()[0]
    referrer = parts[3].strip()
    
    if referrer == "-":
        continue
    if returncode != "404":
        continue
    
    if referrer in dictionary:
        dictionary[referrer] += 1
    else:
        dictionary[referrer] = 1

tmplist = []
for key in dictionary:
    tmplist.append( (dictionary[key], key) )

tmplist.sort(reverse=True)
f = open(outputfilename,"w")
f.write("referrer\tcount\n")
for item in tmplist:
    f.write(f"{item[1]}\t{item[0]}\n")
    
f.close()
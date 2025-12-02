import sys

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

referrercounts = {}
lines = open(inputfilename,"r").readlines()
for line in lines:
    parts = line.strip().split('"')

    returncode = parts[2].strip().split()[0]
    referrer = parts[3]

    if returncode != "404":
        continue
    if referrer == "-":
        continue

    if referrer in referrercounts:
        referrercounts[referrer] += 1
    else:
        referrercounts[referrer] = 1

result = []
for referrer in referrercounts:
    pair = (referrercounts[referrer], referrer)
    result.append(pair)
    
result.sort(reverse = True)
f = open(outputfilename,"w")
f.write("referrer\tcount\n")
for r in result:
    f.write(f"{r[1]}\t{r[0]}\n")
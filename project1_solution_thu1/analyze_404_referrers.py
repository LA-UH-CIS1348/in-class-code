import sys

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

uniquereferrers = {}
lines = open(inputfilename, "r").readlines()
for line in lines:
    parts = line.strip().split('"')
    returncode = parts[2].strip().split()[0]
    referrer = parts[3]
    
    if returncode != "404":
        continue
    if referrer == "-":
        continue

    if referrer in uniquereferrers:
        uniquereferrers[referrer] += 1
    else:
        uniquereferrers[referrer] = 1
    
result = []
for referrer in uniquereferrers:
    r = (uniquereferrers[referrer], referrer)
    result.append(r)

result.sort(reverse = True)
f = open(outputfilename,"w")
f.write("referrer\tcount\n")
for r in result:
    f.write(f"{r[1]}\t{r[0]}\n")
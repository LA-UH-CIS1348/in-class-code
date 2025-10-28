#THIS IS THE PROGRAM I NEED

import sys
import util

print(sys.argv[0])
k = int(sys.argv[1])
filename = sys.argv[2]
lines = util.getlineslongerthanK(filename, k)
for l in lines:
    print(l)
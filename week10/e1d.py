
pokemons = ["mimejr", "pikachu","pikachu","togepi","ratatta","pikachu","togepi"]

counts = {}
for p in pokemons:
    if counts.get(p) == None:
        counts[p] = 1
    else:
        counts[p] += 1

mylist = []
for p in counts:
    mylist.append( [counts[p], p] )

mylist.sort()
print(mylist)


















import json
f = open("example.json", "r")
data = json.load(f)
print(data)
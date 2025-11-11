
pokemons = ["gengar","pikachu", "togepi","pikachu","pikachu","togepi","dragonite","pikachu","chikorita"]

counts = {}
for pokemon in pokemons:
    if counts.get(pokemon) == None:
        counts[pokemon] = 1
    else:
        counts[pokemon] += 1

for p in counts:
    print(p, counts[p])


mylist = []
for p in counts:
    mylist.append( [counts[p], p] )

mylist.sort(reverse=True)
print(mylist)

#cool link
# [json examples very nice] (https://jsonconsole.com/json-examples)

import json

f = open("example.json", "r")
data = json.load(f)
print(data)












f = open("example.json", "r")
s = f.read()

data = json.loads(s)

print(data)

pokemons = ["pikachu", "togepi", "charizard", "togepi", "pikachu","pikachu"]

counts= {}
for pokemon in pokemons:
    if counts.get(pokemon) == None:
        counts[pokemon] = 1
    else:
        counts[pokemon] += 1

for pokemon in counts:
    print(pokemon, counts[pokemon])

print("-----------------")

counts= {}
for pokemon in pokemons:
    counts[pokemon] = counts.get(pokemon, 0) + 1

for pokemon in counts:
    print(pokemon, counts[pokemon])

#-------------------------------------------



grades = {
    "john":91.2,
    "kendrick":42.5,
    "drake":42.5,
    "jayce":20.8
}






result = []
for student in grades:
    result.append( (grades[student], student) )
    
result.sort()
print(result)














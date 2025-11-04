import json

prices = {}

prices["apple"] = 3.56
prices["potato"] = 1.12

print(prices.get("orange"))


colors = {
            "blue":0, 
            "red":5, 
            "green":1
        }



f = open('example.json', 'r')
data = json.load(f)

print(data)


prices = {}
prices["apple"] = 3.56
prices["potato"] = 1.12
prices["kiwi"] = 7.57
prices["tomato"] = 9.82
prices["orange"] = 8.16
prices["banana"] = 1.35






for item in prices:
    print(item, prices[item])





prices = {}
prices["apple"] = 3.56
prices["potato"] = 1.12
prices["kiwi"] = 7.57
prices["tomato"] = 9.82
prices["orange"] = 8.16
prices["banana"] = 1.35
prices["grapes"] = 1.35

pairs = []
for item in prices:
    tmplist=(prices[item], item)
    pairs.append(tmplist)

pairs.sort()
print(pairs)






listofobservations = ["charizard", "pikachu", "togepi", "pikachu", "togepi", "pikachu", "pikachu", "pikachu", "charizard","charizard"]
frequencyofpokemon = {}

for pokemon in listofobservations:
    if frequencyofpokemon.get(pokemon)!=None:
        frequencyofpokemon[pokemon] += 1
    else:
        frequencyofpokemon[pokemon] = 1


print(frequencyofpokemon)























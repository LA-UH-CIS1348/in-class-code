arr = ["gloom", "stunfisk", "chikorita","mimejr", "togepi", "gengar"]

#LINEAR SEARCH
#find out if "chikorita" is in the array

query = "chikorita"
found = False
for name in arr:
    if name == query:
        found = True
        break

if found:
    print(f"found {query}!")
else:
    print(f"could not find {query}!")


query = "pikachu"
found = False
for name in arr:
    if name == query:
        found = True
        break

if found:
    print(f"found {query}!")
else:
    print(f"could not find {query}!")

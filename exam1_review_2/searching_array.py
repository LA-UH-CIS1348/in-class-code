pokebelt = ["gloom","stunfisk","chikorita","mimejr","togepi","gengar"]

#Linear search

query = "pikachu"
found = False#flag
for pokemon in pokebelt:
    if pokemon == query:
        found = True
        break


if found:
    print("Yes")
else:
    print("No")


names = ["gloom", "stunfisk", "chikorita","mimejr", "togepi", "gengar"]
health = [100,100,100,100,100,100]
#TO AVOID LINEAR SEARCH WE CAN USE INDEX
#TO DO DIRECT LOOK UP
file = open("combatlogwithids.txt", "r")
lines = file.readlines()

for entry in lines:
    splitentry = entry.split()
    attackerindex = int(splitentry[0])
    defenderindex = int(splitentry[1])
    damage = int(splitentry[2])

    health[defenderindex] -= damage

    if damage >= 100:
        print(f"SMACKKKKK!")
    print(f"{names[attackerindex]} hit {names[defenderindex]} for {damage} damage!!!")
    print(f"{names[defenderindex]} health is {health[defenderindex]}!!")


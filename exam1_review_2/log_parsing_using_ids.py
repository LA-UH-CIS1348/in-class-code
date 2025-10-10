names = ["gloom","stunfisk","chikorita","mimejr","togepi","gengar"]
health = [100,100,100,100,100,100]

file = open("combatlog_idsonly.txt","r")
events = file.readlines()

for event in events:
    attackerindex = int(event.split()[0])
    defenderindex = int(event.split()[1])
    damage = int(event.split()[2])

    health[defenderindex] -= damage

    if damage < 100:
        print(f"{names[attackerindex]} hits {names[defenderindex]} for {damage}!")
        print(f"{names[defenderindex]} remaining health is {health[defenderindex]}")
    else:
        print(f"{names[attackerindex]} SMACKS {names[defenderindex]} for {damage}!")
        print(f"{names[defenderindex]} remaining health is {health[defenderindex]}")
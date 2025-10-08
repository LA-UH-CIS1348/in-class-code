file = open("combatlog.txt","r")
lines = file.readlines()

for line in lines:
    print(line.split(','))
    splitline = line.split(',')
    attacker = splitline[0].split(':')[1]#index ["attacker","pikachu"] with [1] to get "pikachu" out
    defender = splitline[1].split(':')[1]
    damage = int(splitline[2].split(':')[1])
    print(f"{attacker} attacks {defender} for {damage} damage!")
    
file.close()

file = open("combatlog.txt", "r")
lineslist = file.readlines()
file.close()#i can close file because i am done reading

print(lineslist)

for event in lineslist:
    a = event.split(',')

    b = a[0]
    c = b.split(':')
    d = c[1]
    attacker = d

    b = a[1]
    c = b.split(':')
    d = c[1]
    defender = d

    b = a[2]
    c = b.split(':')
    d = c[1]
    damage = int(d)

    print(f"{attacker} hit {defender} for {damage}!")
















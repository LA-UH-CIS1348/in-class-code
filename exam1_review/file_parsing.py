# FILE PARSING - Reading and parsing log files

# Read the file first
file = open("combatlog.txt", "r")
lineslist = file.readlines()
file.close()  # Can close now because data is in memory

print("Raw lines from file:")
print(lineslist)
print("\n" + "="*50 + "\n")

# Process each line (event)
for event in lineslist:
    # Step 1: Split by comma
    a = event.split(',')
    # Result: ["attacker:pikachu", "defender:togepi", "damage:5\n"]

    # Step 2: Extract attacker (verbose way)
    b = a[0]  # "attacker:pikachu"
    c = b.split(':')  # ["attacker", "pikachu"]
    d = c[1]  # "pikachu"
    attacker = d

    # Step 3: Extract defender (verbose way)
    b = a[1]  # "defender:togepi"
    c = b.split(':')  # ["defender", "togepi"]
    d = c[1]  # "togepi"
    defender = d

    # Step 4: Extract damage (verbose way)
    b = a[2]  # "damage:5\n"
    c = b.split(':')  # ["damage", "5\n"]
    d = c[1]  # "5\n"
    damage = int(d)  # Convert to integer (int() ignores \n)

    print(f"{attacker} hit {defender} for {damage}!")


# ALTERNATIVE: More compact version (same result)
print("\n" + "="*50 + "\n")
print("Compact version:")

file = open("combatlog.txt", "r")
for line in file:
    parts = line.split(',')
    attacker = parts[0].split(':')[1]
    defender = parts[1].split(':')[1]
    damage = int(parts[2].split(':')[1])
    print(f"{attacker} attacks {defender} for {damage} damage!")
file.close()

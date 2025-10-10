# DIRECT LOOKUP WITH INDEX
# When you already know the index (position) of data, you can access it directly
# This is called O(1) lookup - constant time access

# REQUIREMENTS FOR USING INDEX AS ID:
# 1. Fixed size arrays (no insertions or deletions)
# 2. Agreed upon ID system (0, 1, 2, 3...)
# 3. Parallel lists where same index = same entity

# Simple example - direct lookup
pokebelt = ["gloom", "stunfisk", "chikorita", "mimejr", "togepi", "gengar"]

# When you know chikorita is at index 2
print(f"Pokemon at index 2: {pokebelt[2]}")  # chikorita


# Example with parallel lists (using index as ID)
names = ["gloom", "stunfisk", "chikorita", "mimejr", "togepi", "gengar"]
health = [100, 100, 100, 100, 100, 100]

# TO AVOID LINEAR SEARCH WE CAN USE INDEX AS ID
# TO DO DIRECT LOOK UP
file = open("combatlog_idsonly.txt", "r")
lines = file.readlines()
file.close()

for entry in lines:
    # Parse the line: attacker_id defender_id damage
    splitentry = entry.split()
    attackerindex = int(splitentry[0])
    defenderindex = int(splitentry[1])
    damage = int(splitentry[2])

    # Update health using direct index lookup
    health[defenderindex] -= damage

    # Print results with special message for big hits
    if damage >= 100:
        print(f"SMACKKKKK!")
    print(f"{names[attackerindex]} hit {names[defenderindex]} for {damage} damage!!!")
    print(f"{names[defenderindex]} health is {health[defenderindex]}!!")

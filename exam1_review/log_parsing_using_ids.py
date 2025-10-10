# LOG PARSING WITH ID-BASED LOOKUP
# When log files use numeric IDs instead of names

# Setup parallel lists where index = ID
names = ["gloom", "stunfisk", "chikorita", "mimejr", "togepi", "gengar"]
health = [100, 100, 100, 100, 100, 100]

# Read log file with IDs
file = open("combatlog_idsonly.txt", "r")
events = file.readlines()
file.close()

# Process each event
for event in events:
    # Parse: "0 1 12" means attacker_id=0, defender_id=1, damage=12
    parts = event.split()  # Split by whitespace

    attackerindex = int(parts[0])
    defenderindex = int(parts[1])
    damage = int(parts[2])

    # Use IDs as indexes to look up data and update health
    health[defenderindex] -= damage

    # Print with conditional formatting
    if damage < 100:
        print(f"{names[attackerindex]} hits {names[defenderindex]} for {damage}!")
        print(f"{names[defenderindex]} remaining health is {health[defenderindex]}")
    else:
        print(f"{names[attackerindex]} SMACKS {names[defenderindex]} for {damage}!")
        print(f"{names[defenderindex]} remaining health is {health[defenderindex]}")

# WHY THIS WORKS:
# - Fixed size arrays (no insertions/deletions)
# - Agreed ID system (0=gloom, 1=stunfisk, 2=chikorita, etc.)
# - Index in names[] matches index in health[] for same entity
# - Can directly access data without searching: O(1) instead of O(n)

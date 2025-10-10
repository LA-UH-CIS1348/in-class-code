# STRING PARSING WITH SPLIT()
# Breaking down structured data into usable pieces

# Example: Parse a combat event
event = "attacker:togepi,defender:pikachu,damage:500"

# HOW TO PARSE:
# 1. IDENTIFY TOKENS (delimiters) SEPARATING DATA
#    - In this example: comma separates major parts, colon separates key:value
# 2. SPLIT BY FIRST DELIMITER
# 3. CONTINUE SPLITTING RESULTING TOKENS UNTIL YOU GET WHAT YOU NEED

# Step 1: Split by comma (first delimiter)
eventsplitresult = event.split(',')
print("After splitting by comma:")
print(eventsplitresult)
# Result: ["attacker:togepi", "defender:pikachu", "damage:500"]

# Step 2: Split each part by colon (second delimiter) to get values
attacker = eventsplitresult[0].split(':')[1]  # Get "togepi"
defender = eventsplitresult[1].split(':')[1]  # Get "pikachu"
damage = int(eventsplitresult[2].split(':')[1])  # Get 500 as integer

print(f"\n{attacker} TEACHES {defender} a LESSON for {damage} damage!")


# Alternative: More verbose step-by-step approach (same result)
parts = event.split(',')  # ["attacker:togepi", "defender:pikachu", "damage:500"]

attacker_part = parts[0]  # "attacker:togepi"
attacker_pieces = attacker_part.split(':')  # ["attacker", "togepi"]
attacker_name = attacker_pieces[1]  # "togepi"

defender_part = parts[1]  # "defender:pikachu"
defender_pieces = defender_part.split(':')  # ["defender", "pikachu"]
defender_name = defender_pieces[1]  # "pikachu"

damage_part = parts[2]  # "damage:500"
damage_pieces = damage_part.split(':')  # ["damage", "500"]
damage_value = int(damage_pieces[1])  # 500

print(f"{attacker_name} vs {defender_name}: {damage_value} damage")

# LINEAR SEARCH
# When you DON'T know the index, you must search through the list
# This checks each item one by one until found (or end of list)

arr = ["gloom", "stunfisk", "chikorita", "mimejr", "togepi", "gengar"]

# Example 1: Simple search with flag
query = "chikorita"
found = False  # Flag to track if we found it

for name in arr:
    if name == query:
        found = True
        break  # Stop searching once found

if found:
    print(f"Found {query}!")
else:
    print(f"Could not find {query}!")


# Example 2: Search to find the INDEX of an item
# This is very useful when you need to know WHERE the item is located
query = "togepi"
index = -1  # -1 means "not found"

for i in range(len(arr)):
    if arr[i] == query:
        index = i
        break  # Stop once found

if index != -1:
    print(f"Found {query} at index {index}")
else:
    print(f"Could not find {query}")


# Example 3: Using the index for parallel lists
names = ["gloom", "stunfisk", "chikorita", "mimejr", "togepi", "gengar"]
health = [100, 100, 100, 100, 100, 100]

# Find defender's index, then update their health
defender = "stunfisk"
defender_index = -1

for i in range(len(names)):
    if names[i] == defender:
        defender_index = i
        break

# Now use the index to update health
if defender_index != -1:
    health[defender_index] -= 25
    print(f"{names[defender_index]} health is now {health[defender_index]}")


print("\n" + "="*60 + "\n")


# USING THE 'in' OPERATOR
# A simpler way to check if a value exists in a list or string

# IMPORTANT CONCEPT:
# Both lists and strings are essentially ARRAYS
# - List: each element is an item
# - String: each element is a character

# Example 4: Using 'in' with LISTS
# Finds if the ITEM exists in the list
arr = ["gloom", "stunfisk", "chikorita", "mimejr", "togepi", "gengar"]

query = "chikorita"
if query in arr:
    print(f"Found {query}!")
else:
    print(f"Could not find {query}!")


# Example 5: Using 'in' with STRINGS
# Finds if CONSECUTIVE CHARACTERS match (substring search)
sentence = "I really like apples"

if "like" in sentence:
    print("You like something!")

# This works because strings are arrays of characters:
# ['I', ' ', 'r', 'e', 'a', 'l', 'l', 'y', ' ', 'l', 'i', 'k', 'e', ' ', 'a', 'p', 'p', 'l', 'e', 's']
# It finds consecutive characters: 'l', 'i', 'k', 'e'


# NOTE: The 'in' operator only tells you IF something exists
# If you need to find the INDEX, you must use a loop with range()
# (see Examples 2 and 3 above)

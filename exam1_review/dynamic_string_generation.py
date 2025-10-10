# DYNAMIC STRING GENERATION WITH F-STRINGS
# Creating variable file names and messages dynamically

# Example: Reading multiple files with a pattern
# Files: pokemonid_0.txt, pokemonid_1.txt, pokemonid_2.txt, pokemonid_3.txt

# We agree there are 4 files with IDs 0, 1, 2, 3

for i in range(4):
    # Generate filename dynamically using f-string
    filename = f"pokemonid_{i}.txt"

    # Open and read the file
    f = open(filename, "r")
    contents = f.read()

    # Print with dynamic message
    print(f"=== Contents of {filename} ===")
    print(contents)

    f.close()


# F-STRING FORMAT:
# f"text {variable} more text"
# - The f before the quote makes it an f-string
# - Variables in {} are replaced with their values
# - Very useful for:
#   * Dynamic file names
#   * Dynamic output messages
#   * Creating formatted strings

# Examples:
name = "Pikachu"
level = 25
health = 100

print(f"{name} is level {level} with {health} HP")
print(f"File: pokemon_{level}.txt")
print(f"Status: {name} has {health/100*100:.0f}% health")

# THREE WAYS TO READ FILES

# Method 1: file.read() - Reads ENTIRE file into ONE STRING
file = open("combatlog.txt", "r")
content = file.read()  # Entire file as a single string
print("=== Using read() ===")
print(content)
file.close()

print("\n" + "="*50 + "\n")

# Method 2: file.readlines() - Reads ENTIRE file into a LIST OF STRINGS
# Each line becomes one string in the list
file = open("combatlog.txt", "r")
lines = file.readlines()  # List of strings, one per line
print("=== Using readlines() ===")
print(lines)  # See the list structure
print("\n--- Processing each line ---")
for line in lines:
    print(line.strip())  # strip() removes the \n at end of line
file.close()

print("\n" + "="*50 + "\n")

# Method 3: for line in file - Read lines ONE AT A TIME
# More memory efficient for VERY large files
# Doesn't load entire file into memory at once
file = open("combatlog.txt", "r")
print("=== Reading lines directly from file ===")
for line in file:
    print(line.strip())
file.close()

# WHICH METHOD TO USE?
# - read(): Small files, need content as one string
# - readlines(): Need all lines in a list, or need to process multiple times
# - for line in file: Large files, process once line-by-line

# NOTE: There are also ways to seek() to a particular position in a file
# to read or write at specific locations. This works best for very large files.
# (Not covered in this exam)


print("\n" + "="*60 + "\n")


# WRITING TO FILES

# Method 1: Write mode ("w") - OVERWRITES the file if it exists
file = open("output.txt", "w")
file.write("Hello World!\n")
file.write("How are you?\n")
file.write("This is the last line\n")
file.close()

print("File written with 'w' mode")

# If you run this again, the file will be COMPLETELY REPLACED


# Method 2: Append mode ("a") - ADDS to the end of the file
# Does NOT delete existing content
file = open("output.txt", "a")
file.write("This line is APPENDED\n")
file.write("This is another appended line\n")
file.close()

print("New lines appended with 'a' mode")

# Now output.txt contains:
# Hello World!
# How are you?
# This is the last line
# This line is APPENDED
# This is another appended line


# SUMMARY:
# "w" mode: Overwrites/creates file (use for new files)
# "a" mode: Appends to existing file (use to add more data)

# NOTE: There is also seek() for writing at specific positions
# This works best for very large files (Not covered in this exam)

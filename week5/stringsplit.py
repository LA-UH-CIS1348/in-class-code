"""
read in integers from the user input separated by spaces into a list
print the list
create a new list and store the values as integers - use a for loop without range object
print the list
"""

s = input()#get the input as a string
a = s.split()
print(a)

b = []

for numberstring in a:
    x = int(numberstring)
    b.append(x)

print(b)
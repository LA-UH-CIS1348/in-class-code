
"""
A)write a program that takes in 5 integers from the user and stores them in a list using a for loop.
B)modify the list by multiplying each integer by 5 using a while loop. 
C)modify the list by adding 2 to each value using a for loop with range. 
D)print the list using a for loop without range.
"""

#A
a = []

for i in range(5):
    x = int(input())
    a.append(x)
#B
i = 0
while i < 5:
    a[i] *= 5
    i += 1

#C
for i in range(5):
    a[i] += 2

#B AND C DO THE SAME KIND OF LOOP WITH INDEX

#D
for number in a:
    print(number)
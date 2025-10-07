"""
write a program that asks addition problems to beginners (10 problems)
keep score
if all correct congratulate
"""

import random

print("welcome to math gym")
print("press enter to continue")
input()

score=0
problemcounter=0
while problemcounter < 10:
    a = random.randint(1,99)
    b = random.randint(1,99)

    print("what is",a,"+",b,"?")
    answer = int(input("answer:"))
    correctanswer = a + b
    if answer == correctanswer:
        print("correct")
        score+=1
    else:
        print("incorrect")

    problemcounter+=1

if score == 10:
    print("good job, proceed to dining table!")
else:
    print("goodnight!")
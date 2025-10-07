"""
blackjack
"""
import random

stillplaying=True
money=20
roundcounter=0
maxrounds=10
while stillplaying:
    roundcounter+=1
    print("\nround:", roundcounter, "money:", money)
    money -= 5

    input()
    card1 = random.randint(1,10)
    print("drew", card1)
    input()

    card2=0
    if random.random() < 0.3:
        card2=11
    else:
        card2 = random.randint(1,10)
    print("drew", card2)

    total = card1+card2
    if total == 21:
        money += 20
    elif total < 21:
        money += 2
    else:
        print("boo")


    if money <= 0 or roundcounter>=maxrounds:
        stillplaying=False

print("money:", money) 
    
# JUMPTABLES
def add(x,y):
    return x+y
def mult(x,y):
    return x*y

A = {"0xADD":add, "0xM":mult}

actions = open("robloxhack.txt","r").readlines()
for action in actions:
    parts = action.strip().split()
    f = A[parts[0]]
    x = int(parts[1])
    y = int(parts[2])
    print(f"execute(hack):{f(x,y)}")

for action in actions:
    parts = action.strip().split()
    f = None
    if parts[0] == "0xADD":
        f = add
    elif parts[0] == "0xM":
        f = mult 
    x = int(parts[1])
    y = int(parts[2])
    print(f"execute(hack):{f(x,y)}")

A = [1,2,3,4,5]
B = list(map(lambda item:item*item-2, A))
print(B)

A = [1,2,3,4,5]
B = list(map(lambda item:item*item-2, filter(lambda x:x==3,A)))
print(B)

A = (x-2 for x in range(5))
print(list(A))

A = [["Alice",10], ["Bob", 2], ["Joe", 5]]
B = sorted(A,key = lambda x:x[1])
print(B)

print("---")
A = [ {"name":"Alice", "magic":10},{"name":"Bob", "magic":2},{"name":"Joe", "magic":5}]
B = sorted(A, key = lambda x : x["magic"])
print(B)


print("---")
A = [
    {"name":"Joe", 
     "magic": {"fire":5,"ice":1,"shadow":600}
    },
    {"name":"Alice", 
     "magic": {"fire":5,"ice":1000,"shadow":6}
    },
    {"name":"Bob", 
     "magic": {"fire":500,"ice":10,"shadow":6}
    }
    
]
B = sorted(A, key = lambda item: item["magic"]["fire"])
print(B)

#SAME THING
A = [x*x for x in range(5)]

A=[]
for x in range(5):
    A.append(x*x)

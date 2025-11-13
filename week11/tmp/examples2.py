## JUMPTABLE
def add(x,y):
    return x + y

def mult(x,y):
    return x * y

##
functionlist = [add,mult]
print(functionlist[0](2,3))
print(functionlist[1](2,3))

##
functiondictionary = {"tomato":add, "potato":mult}
print(functiondictionary["tomato"](2,3))
print(functiondictionary["potato"](2,3))

## ROBOT WALKING

def forward():
    print("motors L R +12V")

def back():
    print("motors L R -12V")

def left():
    print("motors L -12V")
    print("motors R +12V")

def right():
    print("motors L +12V")
    print("motors R -12V")


actions = open("robot.txt","r").readlines()
for a in actions:
    if a.strip() == "FWD":
        forward()
    elif a.strip() == "BACK":
        back()
    elif a.strip() == "LEFT":
        left()
    elif a.strip() == "RIGHT":
        right()


## MAP
A = [1,2,3,4,5]
B = list(map(lambda x : x * x, A))
print(B)

A = [1,2,3,4,5]
print(list(
    map(lambda x : x+2, 
        map(lambda x:x*x, 
            filter(lambda x : x%2 == 1, A)))))


A = [["Bob",8], ["Alice", 20], ["Joe", 1]]
B = sorted(A, key = lambda x : x[0])
C = sorted(A)
print(A)
print(B)
print(C)

print("---------------------")
A = [
    {"name":"Bob", "health":100,"magic":50},
    {"name":"Alice", "health":20,"magic":100},
    {"name":"Joe", "health":30,"magic":10}
]
B = sorted(A, key = lambda item : item["magic"], reverse = True)
print(B)



print("-------------------")

A = [
    {
        "name":"Joe",
        "health":20,
        "magic":{
            "ice":1000,"fire":20,"shadow":50
        }
    },
    {
        "name":"Alice",
        "health":100,
        "magic":{
            "ice":10,"fire":200,"shadow":5
        }
    },
    {
        "name":"Bob",
        "health":100,
        "magic":{
            "ice":10,"fire":20,"shadow":50
        }
    }
    
]

B = sorted(A, key=lambda item : item["magic"]["shadow"])
print(B)


A = [x*x for x in range(5) if x%2==1]
print(A)






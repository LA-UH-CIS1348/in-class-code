## JUMPTABLES
def add(x,y):
    return x+y

def mult(x,y):
    return x*y

jumptable_list = [add, mult]
jumptable_dict = {"ADD": add, "MULT": mult}

print(jumptable_list[0](2,5))
print(jumptable_list[1](2,5))
print(jumptable_dict["ADD"](2,5))
print(jumptable_dict["MULT"](2,5))

## JUMPTABLE ROBOT
def up():
    print("*motors LR ON +V")

def down():
    print("*motors LR ON -V")

def left():
    print("*motor L ON +V")
    print("motor R ON -V")

def right():
    print("*motor L ON -V")
    print("motor R ON +V")          

file = open("actions.txt", "r")
actions = file.readlines()

### IF/ELIF BLOCK
for a in actions:
    a = a.strip()
    if a == "UP":
        up()
    elif a == "DOWN":
        down()
    elif a == "LEFT":
        left()
    elif a == "RIGHT":
        right()

### DICTIONARY VERSION OF THE SAME THING ABOVE
robot = {"UP":up,"DOWN":down,"LEFT":left,"RIGHT":right}
for a in actions:
    a = a.strip()
    robot[a]()


## MAP
def square(x):
    return x * x

def my_map(op, elements):
    result = []
    for element in elements:
        result.append(op(element))
    
    return result

A = [5,2,4,1,3]
B = my_map(square, A)
C = list(map(square, A))

print(B)
print(C)

## FILTER
def is_odd(x):
    if x%2==1:
        return True
    return False

def my_filter(op, items):
    result = []
    for item in items:
        if op(item) == True:
            result.append(item)

    return result

A = [5,2,4,1,3]
B = my_filter(is_odd, A)
C = list(filter(is_odd, A))

print(B)
print(C)

## LAMBDA VERSION OF SQUARE
### **lambda is an anonymous function without a name or body**
A = [5,2,4,1,3]
B = list(map(lambda x : x*x, A))
print(B)

## LAMBDA VERSION OF IS_ODD
A = [5,2,4,1,3]
B = list(filter(lambda x : x % 2 == 1, A))
print(B)

## SORTED
A = [5,2,4,1,3]
B = sorted(A)#sorted does not modify its argument
print(A)
print(B)

## SORTED WITH FUNCTION
def pick_index_zero(item):
    return item[0]

def pick_index_one(item):
    return item[1]

A = [["Bob", 2], ["Alice", 5]]
B = sorted(A, key = pick_index_zero)#sorted by name
C = sorted(A, key = pick_index_one)#sorted by number
print(A)
print(B)
print(C)

## SORTED WITH LAMBDA
A = [["Bob", 2], ["Alice", 5]]
B = sorted(A, key = lambda item: item[0])#sorted by name
C = sorted(A, key = lambda item: item[1])#sorted by number
print(A)
print(B)
print(C)


## SORTED WITH FUNCTION, DIFFICULT CASE
def pick_magic_power(item):
    return item["magic"]

A = [
    {"name":"Bob", "health":100, "magic":10},
    {"name":"Alice", "health":10, "magic":20},
    {"name":"Joe", "health":20, "magic":2}
    ]

B = sorted(A, key = pick_magic_power)
print("before sort")
print(A)
print("after sort")
print(B)

## SORTED WITH FUNCTION, MORE DIFFICULT CASE
def pick_shadow(item):
    return item["magic"]["shadow"]

A = [
    {"name":"Bob", "health":100, "magic":{"ice":10,"fire":20,"shadow":50}},
    {"name":"Alice", "health":10, "magic":{"ice":10,"fire":200,"shadow":5}},
    {"name":"Joe", "health":20, "magic":{"ice":100,"fire":20,"shadow":40}}
    ]

B = sorted(A, key = pick_shadow)
print("before sort")
print(A)
print("after sort")
print(B)

size=5
myarray = [0]*size

currentindex = 0
while True:
    s = input("hacking>")
    #commands
    #push 7
    #pop
    #quit
    #otherwise complain

    cmd = s.split()#cmd is a list
    if cmd[0] == "quit":
        print("goodbye")
        break
    elif cmd[0] == "pop":
        currentindex -= 1
    elif cmd[0] == "push":
        x = int(cmd[1])
        myarray[currentindex]=x
        currentindex += 1
    else:
        print("unknown command:", s)

    for i in range(currentindex):
        print(f"{myarray[i]},", end="")
    print()
    
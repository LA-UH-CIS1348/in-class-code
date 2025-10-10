
for i in range(4):
    filename = f"pokemon{i}.txt"
    file = open(filename,"r")
    print(file.read())
    file.close()
#we agree there are 4 files
#ids are 0,1,2,3

for i in range(4):
    f = open(f"pokemonid_{i}.txt")
    contents = f.read()
    print(contents)
    f.close()
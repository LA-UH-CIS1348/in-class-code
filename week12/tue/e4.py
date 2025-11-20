class Cat:
    def __init__(self):
        print("I HAVE BEEN SUMMONED")
        self.name = ""
        self.weight = 0.0
    
    def speak(self):
        print(f"meow i weigh {self.weight} and my name is {self.name}")

class Kitten(Cat):
    def __init__(self):
        super().__init__()
        self.soul = "innocent"
        self.attitude = "reasonable"
        self.fur = "soft"
        print("meow =o.o=")

    def speak(self):
        print(f"im an innocent soul")

    def be_nice():
        print("pet me teheheheh")    

class Dog:
    def __init__(self):
        self.name = ""
        self.weight = 0.0
    
    def speak(self):
        print(f"woof {self.weight} and my name is {self.name} please let me walk with you and buy you food")


cats = []
for i in range(10):
    cat = Cat()
    cat.name = f"Pringles the {i+1}rd"
    cat.weight = 24.0 + i*2.0
    cats.append(cat)

kittens = []
for i in range(10):
    kitten = Kitten()
    kitten.name = f"fluffi {i+1}rd"
    kitten.weight = 2.0 + i*2.0
    kittens.append(kitten)

dogs = []
for i in range(10):
    puppy = Dog()
    puppy.name = f"Lucy the {i+1}rd"
    puppy.weight = 14.0 + i*2.0
    dogs.append(puppy)

zoo = cats + dogs + kittens
for pet in zoo:
    pet.speak()
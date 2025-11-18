class Cat:
    def __init__(self):
        print("I HAVE BEEN SUMMONED")
        self.name = ""
        self.weight = 0.0
    
    def speak(self):
        print(f"meow i weigh {self.weight} and my name is {self.name}")


class Dog:
    def __init__(self):
        print("I WILL BE YOUR BEST FRIEND")
        self.name = ""
        self.weight = 0.0
    
    def speak(self):
        print(f"woof {self.weight} and my name is {self.name} please let me walk with you and buy you food")


cats = []
for i in range(10):
    kitten = Cat()
    kitten.name = f"Pringles the {i+1}rd"
    kitten.weight = 24.0 + i*2.0
    cats.append(kitten)

dogs = []
for i in range(10):
    puppy = Dog()
    puppy.name = f"Lucy the {i+1}rd"
    puppy.weight = 14.0 + i*2.0
    dogs.append(puppy)

zoo = cats + dogs
for pet in zoo:
    pet.speak()
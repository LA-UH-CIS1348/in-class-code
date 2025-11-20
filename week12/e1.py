class Animal:
    def __init__(self):
        self.name = "JUST AN ANIMAL"
        self.x = 0.0
        self.y = 0.0

    def print(self):
        print(self.name)

class Cat(Animal):
    def __init__(self, name):#CONSTRUCTOR
        super().__init__()
        self.name = name
        self.numberofclaws = 20

    def meow(self):
        print("meow")

    def __add__(self,other):
        newname = self.name + "-" + other.name
        newcat = Cat(newname)
        newcat.numberofclaws = (self.numberofclaws + other.numberofclaws)/2
        return newcat
    
    def __mul__(self, other):
        newname = "!!!!!" + self.name + "-" + other.name
        newcat = Cat(newname)
        newcat.numberofclaws = (self.numberofclaws * other.numberofclaws)/2
        return newcat
    
    def __lt__(self, other):
        if self.numberofclaws < other.numberofclaws:
            return True
        return False
    
    def __str__(self):
        return f"{self.name} {self.numberofclaws}"

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = "STANDARD DOG"
        self.friendlinesslevel = 5
        self.numberofteeth = 900
    #OVERRIDE
    def print(self):
        print("HELLO FRIEND MY NAME IS " + self.name)

    #SETTER
    def set_name(self, name): 
        self.name = name

    #GETTER
    def get_name(self): 
        return self.name

cat1 = Cat("floofi")
cat2 = Cat("ploopi")
dog1 = Dog()
dog2 = Dog()

dog1.name = "Toby"#no do not do this
dog1.set_name("Toby")
happybirthdaymessage = "Happy birthday " + dog1.get_name()

cat1.print()
cat2.print()
dog1.print()
dog2.print()

zoo = [cat1, cat2, dog1, dog2, dog1, dog2, cat1]








#polymorphism
for pet in zoo:
    pet.print()









class Person:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.balance = 0











zoo = []
zoo.append(Cat("mrclaws"))
zoo.append(Dog())
zoo.append(Animal())
zoo.append(Dog())
zoo.append(Cat("thepunisher"))













print("------------------------------")
for pet in zoo:
    pet.print()








print("----------------------")
toby = Cat("toby")
pringles = Cat("pringles")

cat1 = toby + pringles
cat2 = toby * pringles
cat3 = (cat1 + cat2) * cat1

print(cat1.name, cat1.numberofclaws)
print(cat2.name, cat2.numberofclaws)
print(cat3.name, cat3.numberofclaws)

print("------------------")
cats = [cat2,cat3,cat1,toby,pringles]
cats.sort()
for c in cats:
    print(c)
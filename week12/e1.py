class Animal:
    def __init__(self):
        self.x=0.0
        self.y=0.0
        self.name=""

    def run(self):
        print("rolling really fast")


class Cat(Animal):
    def __init__(self, n):
        super().__init__()
        self.numberofteeth = 30

    def run(self):
        print("sneaking around fast")

    def walk(self):
        print("sneaking around")

    def eat(self, food):
        print("meow thanks for the " + food + " just kidding here is a scratch mark!!!!")
        self.numberofteeth -= 1

    #GETTER
    def get_name(self):
        return self.name
    #SETTER
    def set_name(self, n):
        self.name = n

    #OPERATOR OVERLOADING
    def __add__(self, other):
        newname = self.name + "-_-" + other.name
        newcat = Cat(newname)
        newcat.numberofteeth = (self.numberofteeth + other.numberofteeth)/2
        return newcat

    def __lt__(self, other):
        if self.numberofteeth < other.numberofteeth:
            return True
        return False


c1 = Cat("pringles")
c1.walk()
c1.eat("tuna")
c2 = Cat("garfield")

c3 = c1 + c2
c3.set_name("garfield jr")
print(c3.get_name())
print(c3.numberofteeth)
c1.x=9











name = [""]*100
balance = [0]*100

class Person:
    def __init__(self):
        name = ""
        balance = 0



people = [Person()]*100





























floofi = Cat("floofi")
floofi.run()
class Cat:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __add__(self, other):
        newname = f"{self.name}-{other.name}"
        newweight = (self.weight + other.weight) / 2
        result = Cat(newname, newweight)
        return result
    
    def __mul__(self, other):
        newname = f"!!!{self.name}-{other.name}!!!"
        newweight = (self.weight * other.weight)
        result = Cat(newname, newweight)
        return result
    
    def __str__(self):
        return f"name:{self.name} weight: {self.weight}"

    def __le__(self,other):
        if self.weight <= other.weight:
            return True
        return False

cat1 = Cat("pringles", 12.0)
cat2 = Cat("fluufi", 15.0)
cat3 = cat1 + cat2
cat4 = cat1 * cat2
cat5 = cat3*cat4+cat2+cat1*cat3
print(cat3)
print(cat4)
print(cat5)

print(cat1 <= cat2)
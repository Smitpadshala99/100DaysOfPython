x = [1,2,3]
print(dir(x))
print(x.__add__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("Smit", 19)
print("\n\n\n",p.__dict__)

print("\n\n\n",help(Person))
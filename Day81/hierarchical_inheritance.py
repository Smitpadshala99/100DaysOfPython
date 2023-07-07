# class BaseClass:
#     pass

# class D1(BaseClass):
#     pass

# class D2(BaseClass):
#     pass

# class D3(D1):
#     pass

class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("\nName:", self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show_details(self):
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)

dog = Dog("Max", "Golden Retriever")
dog.show_details()
cat = Cat("Luna", "Black")
cat.show_details()
class Person:
    # Parameterized Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("I am a Person")

    # Default Constructor
    def info(self):
        print(f"{self.name} is {self.age} years old.")

a = Person("Smit",19)
a.info()

b = Person("Ram",0)
b.info()

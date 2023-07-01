class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"The name of Employee: {self.name} is {self.id}")

class Programmar(Employee):
    def Language(self):
        print(f"The language of Programmar: Python")

e1 = Employee("Smit", 187)
e1.show()
e2 = Programmar("Smit Padshala", 99)
e2.show()
e2.Language()
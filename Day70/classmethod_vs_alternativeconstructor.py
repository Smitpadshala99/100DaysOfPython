class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls,line):
        return cls(line.split("-")[0],int(line.split("-")[1]))

e1 = Employee("Smit", 35000)
print(e1.name)
print(e1.salary)

string = "Smit-45000"
# e2 = Employee(string.split("-")[0], string.split("-")[1])
e2 = Employee.from_string(string)
print(e2.name)
print(e2.salary)
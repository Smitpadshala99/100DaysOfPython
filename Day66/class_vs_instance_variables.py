class MyClass:
    class_variable = 0
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)
        

obj1 = MyClass()
obj1.print_class_variable() # Output: 1
obj2 = MyClass()

obj1.print_class_variable() # Output: 2
obj2.print_class_variable() # Output: 2

class Employee:
    companyName = "Apple" # class variable
    def __init__(self,name):
        self.name = name
        self.amount = 0.5  # instance variable
    def show(self):
        print(f"In Company {self.companyName}, Employee name is {self.name} and amount is {self.amount}")

e1 = Employee("Smit")
e1.show()
e1.amount = 0.4
Employee.companyName = "Google"
e1.show()
e1.companyName = "Apple India"
e1.show()
Employee.companyName = "Google"
e2 = Employee("Ram")      
e2.show()
print(Employee.companyName)
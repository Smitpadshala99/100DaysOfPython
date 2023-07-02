# public
class Employee:
    def __init__(self):
        self.name = "Smit"

a = Employee()
print(a.name) 

# private
class Employee:
    def __init__(self):
        self.__name = "Smit"

a = Employee()
# print(a.__name) # cannot accessed directly
print(a._Employee__name) # can be accessed indirectly
print(a.__dir__())

# Protected
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())


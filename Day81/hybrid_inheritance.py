# class BaseClass:
#     pass

# class Derived1(BaseClass):
#     pass

# class Derived2(BaseClass):
#     pass

# class Derived3(Derived1, Derived2):
#     pass

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def show_details(self):
    print("Name:", self.name)
    print("Age:", self.age)
    
class Person(Human):
  def __init__(self, name, age, address):
    Human.__init__(self, name, age)
    self.address = address
    
  def show_details(self):
    Human.show_details(self)
    print("Address:", self.address)
    
class Program:
  def __init__(self, program_name, duration):
    self.program_name = program_name
    self.duration = duration
    
  def show_details(self):
    print("Program Name:", self.program_name)
    print("Duration:", self.duration)
    
class Student(Person):
  def __init__(self, name, age, address, program):
    Person.__init__(self, name, age, address)
    self.program = program
    
  def show_details(self):
    Person.show_details(self)
    self.program.show_details()

person = Person("Smit", 19, "Gujarat")
person.show_details()

program = Program("Computer Science", "4 years")
student = Student("Smit Padshala", 19, "Ahmedabad", program)
student.show_details()

program1 = Program("CSE", "3 years")
student1 = Student("Ram", 5, "Ahmedabad", program1)
student1.show_details()

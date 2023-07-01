class Person:
    name="Smit"
    occupation="Software Developer"

    def info(self):
        print(f"{self.name} is {self.occupation}")
        
a = Person()
b = Person()
c = Person()

a.name = "Nisarg"
a.occupation = "Manager"

b.name = "Shlok"
b.occupation = "HR"

a.info()
b.info()
c.info()


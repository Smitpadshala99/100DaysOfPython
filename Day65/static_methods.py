class Math:
    def __init__(self,num):
        self.num = num


    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        return a+b
    
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(a.add(2,7)) # using instance name
print(Math.add(9,10)) # using class name
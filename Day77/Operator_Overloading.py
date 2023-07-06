class Vector:
    def __init__(self, i,j,k):
        self.i = i
        self.j = j  
        self.k = k
    
    def __str__(self):
        return f"({self.i}i + {self.j}j + {self.k}k)"

    def __add__(self, other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)
v1 = Vector(3,5,6)
print(v1)

v2 = Vector(7,8,9)
print(v2)

v3 = v1 + v2
print(v3)
print(type(v3))
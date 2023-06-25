info = {"Carla", 19, False, 5.9}
if "Carla" in info:
  print("Carla is present.")
else:
  print("Carla is absent.")

a = {"a", "b", "c", "d"}
b = {"a", "e", "f", "d"}
c = a.union(b)
print(c)

a.update(b)
print(a)

a = {1, 2, 3, 4}
b = {1, 5, 6, 2}
c = a.intersection(b)
print(c)

a.intersection_update(b)
print(a)

a = {1, 2, 3, 4}
b = {1, 5, 6, 2}
c = a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)

a = {1, 2, 3, 4}
b = {1, 5, 6, 2}
c = a.difference(b)
print(c)
a.difference_update(b)
print(a)

a = {1,2,3,4}
b = {1,5,6,2}
c = {5,6,7,8}
print(a.isdisjoint(b))
print(a.isdisjoint(c))

d = {1,2,3}
print(a.issuperset(b))
print(a.issuperset(d))

e = {1,2,3,4,5,6}
print(a.issubset(b))
print(a.issubset(e))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop()
# print(cities)
# print(item)

a = {1,2,3,4,5}
item = a.pop()
print(a)
print(item)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# # print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
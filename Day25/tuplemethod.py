tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)
res = tuple1.index(3, 4, 8)
# res = len(tuple1)
print(res)

countries = ("Spain", "Italy", "India", "England")
temp = list(countries)
print(temp)
temp.append("Russia")       #add item 
print(temp)
temp.pop(3)                 #remove item
print(temp)
temp[2] = "UK"         #change item
print(temp)
countries = tuple(temp)
print(countries)
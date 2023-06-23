marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

print(marks[-3]) # Negative index
print(marks[len(marks)-3]) # Positive index
print(marks[5-3]) # Positive index
print(marks[2]) # Positive index

if "6" in marks:
  print("Yes")
else:
  print("No")

# Same thing applies for strings as well!
if "Ha" in "Harry":
  print("Yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])

#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])

if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")
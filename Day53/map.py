def cube(x):
    return x*x*x

l = [1,2,3,4,5]
# newl = []
# for item in l:
#     newl.append(item**3)

newl = list(map(cube, l))
print(newl)


# List of numbers
numbers = [1, 2, 3, 4, 5]

# cube each number using the map function
cubed = map(lambda x: x ** 3, numbers)

# Print the cubed numbers
print(list(cubed))
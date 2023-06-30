def filter_function(a):
    return a>3

l = [1,8,3,7,2,4,5]
newl = list(filter(filter_function, l))
print(newl)

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
print(list(evens))
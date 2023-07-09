def my_generators():
    for i in range(15):
        yield i

g = my_generators()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for i in g:
    print(i, end=" ")

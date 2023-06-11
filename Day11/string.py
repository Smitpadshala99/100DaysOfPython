name = "Smit"
friend = "Henil"
anotherFriend = 'Yash'
apple = '''Hello, 
Hi
"How are you!"
Bye'''
 
print("Hello, " + name) # Hello, Smit
 
print(name[0]) #S
print(name[1]) #m
print(name[2]) #i
print(name[3]) #t
# print(name[4]) # Throws an error

print("Lets use a for loop\n")
for character in apple:
    print(character)
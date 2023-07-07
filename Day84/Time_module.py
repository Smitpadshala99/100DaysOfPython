import time
print(time.time())
# Output: 1688643834.8681507

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)
# Output: 2023-07-06 17:30:22
print(time.strftime("%Y-%m-%d %H:%M:%S"))

time.sleep(3)
print("This is printed after 3 seconds")
# Output: This is printed after 3 seconds
t1 = time.localtime()
formatted_time1 = time.strftime("%Y-%m-%d %H:%M:%S", t1)
print(formatted_time1)

print(time.strftime("%Y-%m-%d %H:%M:%S"))

def usingWhile():
    i=0
    while i<10:
        i = i+1
        print(i ,end=" ")
    
def usingfor():
    for i in range(10):
        print(i, end=" ")

init = time.time()
usingfor()
print(time.time() - init)
usingWhile()
print(time.time() - init)

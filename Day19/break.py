for i in range(1,12):
  if(i == 10):
    print("Skip the iteration")
    continue
  print("5 X", i, "=", 5 * i)
  
i = 0
while True:
  print(i)
  i = i + 1
  if(i%10 == 0):
    break

for i in range(1,10,1):
    print(i ,end=" ")
    if(i==5):
        break
    else:
        print("Mississippi")
print("Thank you")
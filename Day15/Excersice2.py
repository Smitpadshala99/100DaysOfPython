import time

current_hour = int(time.strftime('%H'))
if ( current_hour < 12 ):
    greeting = "Good Morning"
elif ( current_hour < 18 ):
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"
print(greeting)

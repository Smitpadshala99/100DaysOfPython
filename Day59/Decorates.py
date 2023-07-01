import logging
def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        print(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

my_function(1, 2)

def greet(fx):
    def nfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return nfx

def greetadd(fx):
    def nfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return nfx

@greet
def hello():
    print("Hello World")

def add(a, b):
    print(a + b)
        
hello()
greetadd(add)(1, 2)
greetadd(hello)()

# import time
# current_time = time.time()
# print(current_time)
# def speed_calc_decorator():
#     def wrapper(*args, **kwargs):
#
# def fast_function():
#     for i in range(0, 1000000):
#         i * i
# def slow_function():
#     for i in range(0, 10000000):
#         i * i
import math
import time

# A function as an object
# def shout(text):
#     return text.title()
# heelo = shout("hELLo")
# print(heelo)

# as an argument
# def shout(text):
#     return text.upper()
# def whisper(text):
#     return text.lower()
# def greet(func):
#     greeting = func("Hi, I am created by a function passed as an argument.")
#     print(greeting)
# greet(shout)
# greet(whisper)

# def create_adder(x):
#     def adder(y):
#         return x + y
#     return adder
# add_15 = create_adder(15)
# print(add_15(10))

# def hello_decorator(func):
#     def inner1():
#         print("Hello, this is before function execution")
#         func()
#         print("This is after function execution")
#     return inner1

# def hello_decorator(function):
#     def inner():
#         print("Hello, this is before function execution")
#         function()
#         print("This is after function execution")
#     return inner
# def function_to_be_used():
#     print("This is inside the function !!")
# function_to_be_used = hello_decorator(function_to_be_used)
# function_to_be_used()

def execution_time_decorator(func):
    def wrapper_function(*args):
        begin = time.time()
        func(*args)
        ending = time.time()
        print(f"Total time taken in: {func.__name__}: {ending - begin} ")
    return wrapper_function

@execution_time_decorator
def factorial(num):
    time.sleep(1)
    print(math.factorial(num))
factorial(10)

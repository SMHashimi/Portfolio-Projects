# A decorator in Python is a function that extends the behavior of another function
                                # without changing the base function.
                                # We are going to pass the base function as an argument
                                # to the decorator.

def python_decorator_function(func):
    def python_wrapper():
        print("Decorator Started")
        func()
        print("Decorator Ended")
    return python_wrapper
@python_decorator_function
def another_function():
    print("Hello")
another_function()
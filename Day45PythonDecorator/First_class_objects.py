def outer_function():
    print("I'm outer")
    def nested_function():
        print("I'am inner")
    return nested_function
inner_function = outer_function()
inner_function()
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
# Higher-order function (calculator) - takes another function
                                  # as an argument
def calculator(calc_function, n1, n2):
    return calc_function(n1, n2)
print(calculator(multiply, 3, 3))
# Nested Functions
def outer_function():
    print("I'm outer")
    def nested_function():
        print("I'm inner")
    return nested_function # The returned is saved inside (inner function)
                                        # and then is called - See line 30
inner_function = outer_function()
inner_function()
















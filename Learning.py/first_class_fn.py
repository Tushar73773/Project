# Assign a function to a variable
def greet():
    return "Hello"

say_hello = greet

print(say_hello())


#Pass a function as an argument
def greet():
    return "Hello"

def display(func):
    print(func())

display(greet)

#Return a function from another function
def outer():
    def inner():
        return "Hi!"
    return inner

f = outer()
print(f())

#Store functions in a list
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

operations = [add, multiply]

print(operations[0](2, 3))
print(operations[1](2, 3))
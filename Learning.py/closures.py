def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)
double(5)
triple(5)


def outer():
    x = 10

    def inner():
        print(x) 


    return inner

f=outer()
f()
#Unpacking arguments with * and ** kwargs
def add(a,b,c):
    return a+b+c

nums=[1,2,3] # unpacking list into positional arguments
add(*nums)

info={"a": 1, "b": 2, "c": 3} # unpacking dictionary into keyword arguments
add(**info)
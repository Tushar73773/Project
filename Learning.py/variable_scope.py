x=10 #global variable 
def show():
    x=5 # local variable
    print(x)

show() #5
print(x) #10

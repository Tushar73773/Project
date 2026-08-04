def outer():
    x = 10

    def inner():
        nonlocal x # here we are using nonlocal keyword to access the variable x from the outer function to avoid creating a new local variable x in the inner function
        x = 20

    inner()
    print(x)

outer()
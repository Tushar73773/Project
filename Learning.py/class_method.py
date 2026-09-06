class number:
    a=1
    @classmethod
    def show(cls):
        print(cls.a)

e=number()
e.a=5 
e.show() 
number.show()

""" class method is used to access class variables and methods. It takes cls as the first parameter which refers to the class itself
"""


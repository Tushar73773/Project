#single expression function
square = lambda x: x*x
print(square(5)) #25
#


#common use as a key function in sorting

names=["Alice", "Bob", "Charlie", "David"]
sorted_names=sorted(names,key=lambda name: len(name))
print(sorted_names)
print(type(sorted_names)) #['Bob', 'Alice', 'David', 'Charlie']

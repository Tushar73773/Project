#single expression function
square = lambda x: x*x
print(square(5)) #25



#common use as a key function in sorting

names=["Alice", "Bob", "Charlie", "David"]
sorted_names=sorted(names,key=lambda name: len(name))
print(sorted_names)
print(type(sorted_names)) #['Bob', 'Alice', 'David', 'Charlie']



students = [("Ram", 85), ("Shyam", 92), ("Mohan", 78)]

sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)
print(type(sorted_students)) 
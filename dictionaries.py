#dictionaries
students = {}
students = {"Alice":25, "Bob":27,"Claire":17, "Dan":21, "Emma":22}
#error_students = {Alice:25,Bob:27}
#print(error_students)
print(students)
print(students["Dan"])
students["Fred"]=25
print(students["Fred"])
print(students["Alice"])
students["Alice"]=26
print(students["Alice"])

del students["Fred"]
#print(students["Fred"])
print(students.keys())

#print(students.keys()[0])
a=list(students.keys())
print(a)
print(a[1])
print(a[2])

print(list(students.values())[2:])

#dictionaries doesnot have order unlike lists and tuples
print(students)

print(students.items())

students = {
    "male": ["Tom", "Harry","Frank"],
    "female": ["Sarah","Huda","Samantha","Emily","Elizabeth"]
    }

for key in students.keys():
    print(key)
    print(students[key])
    for name in students[key]:
        if "a" in name:
            print(name)

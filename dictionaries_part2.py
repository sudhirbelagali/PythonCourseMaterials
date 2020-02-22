#capable of storing unlimited amount of information
#each key can hold multiple values

students = {
    "Alice":["ID0001",25,"A"],
    "Bob":["ID0002",27,"B"],
    "Claire":["ID0003",17,"C"],
    "Dan":["ID0004",21,"D"],
    "Emma":["ID0005",22,"E"]
    }
print(students["Bob"][0])
print(students["Dan"][1:])

students1 = {
    "Alice":{"ID":"ID0001","age":25,"grade":"A"},
    "Bob":{"ID":"ID0001","age":25,"grade":"A"},
    "Claire":{"ID":"ID0001","age":25,"grade":"A"},
    "Dan":{"ID":"ID0001","age":25,"grade":"A"},
    "Emma":{"ID":"ID0001","age":25,"grade":"A"}
    }
print(students1["Bob"]["age"])

print(students1["Emma"]["ID"],students1["Emma"]["grade"] )

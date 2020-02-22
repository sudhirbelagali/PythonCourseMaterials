#packing and unpacking arguments

print(1,2,3,4,5)

numbers = [1,2,3,4,5]
print(numbers)

print(*numbers) #unpacking

print("abc")
print(*"abc") #unpacking
print("a","b","c")

def add(x,y):
    return x+y
print(add(10,10))

#packing
def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return(total)

print(add(3,2,1))

#keyword arguments

def about(name,age,likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name,age,likes)
    return sentence

dictionary = {"name":"Sudhir","age":30,"likes":"Python"}
#one star for normal arguments and 2 stars for keyword arguments
dictionary = {"age":30,"name":"Sudhir","likes":"Python"}
print(about(**dictionary))



def foo(**kwargs): #it produces dictionary called kwargs
    for key,value in kwargs.items():
        print("{},{}".format(key,value))

foo(Huda="Female",Sudhir="Male",John="Male")

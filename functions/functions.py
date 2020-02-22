#function is a block of reusable organized peace of code that perfroms an action
#define a function - def

def add(x,y):
    return x + y

res = add(5,10)
print(res)

answer = add(100,20)
print(answer)


def Add(x,y):
    print(x + y)

answer = Add(5,2)
print(answer)
print(type(answer))

word = "pen"
print(word[::-1])

def rev(text):
    return text[::-1]

answer = rev("sudhir")
print(answer)

answer = rev([1,2,3,4])
print(answer)

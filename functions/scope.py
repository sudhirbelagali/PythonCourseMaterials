#global scope
#local scope

a = 100

def f1():
    print(a)
    
def f2():
    print(a)

f1() #100 prints as 'a' is in global scope
f2() #100 prints as 'a' is in global scope

def f1():
    b = 100
    print(b)
    
def f2():
    b = 50
    print(b)

f1() #100 prints as 'b' is in local scope
f2() #variable b is outside the scope 


def f1():
    a=100
    print(a)
    
def f2():
    a=50
    print(a)

f1() #It creates a variable locally instead of modifying global variable
f2()
print(a)

a = 250

def f1():
    b=100+a
    print(b)
    
def f2():
    b=50+a
    print(b)

f1() #It creates a variable locally instead of modifying global variable
f2()
print(a)

def f1():
    global a
    a = 300
    print(a)
    
def f2():
    b=50+a
    print(b)

f1() #It creates a variable locally instead of modifying global variable
f2()
print(a)



def f1():
    b = 100
    print(b)
    
#def f2():
    #print(b)

f1() #100 prints as 'b' is in local scope
#f2() #variable b is outside the scope

print("New update")
a = [1,2,3]
def f1():
    a[0]=5
    print(a)

def f2():
    a=50 #local
    print(a)
f1()
f2()
print(a)
 



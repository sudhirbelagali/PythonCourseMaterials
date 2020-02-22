#Logical Operators < <= == > >=
print(not(True))
print(not(False))
print(not(2<3))
print(not(4==3))
x=10
y=20
if(not(y<x)):
    print("It worked");

c=10
d=5
if((c>=10) and (d>1)):
    print("It worked")

if not((c>10) and (d>1)):
    print("It worked")


C=5
D=-1
if(C>1 or D>1):
    print("It worked")

if(C>100 or D>100):
    print("It worked")

if not(C>100 or D>100):
    print("It worked")


C=6
D=2
if not((C>5) and (D>5)) or ((C>1) and (D>1)):
    print("It worked")


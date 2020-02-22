A = [5,2,3,4,6,89]
#A = A + 1 It won't work out
#this works
A = A + [1]

#A = A + "BCD" It won't work out
A = A + ["BCD"]

A = A + list("BCD") #strings are iterable

#A = A + list(123) it won't work out because integers are not iterable

A = A + [1,2,3]

A = A + list(str(123))

A = [5,2,3,4,6,89]
print(A)

A= A + [5,6,7,8]
print(A)

A = A + [[5,6,7,8]]
print(A)
print(A[-1])
A.append([10,11,12,13])
print(A)

A = [5,6,7,8]
print(A)

A = A.append(10) #append returns 0 at the end
print(A)

A = [5,6,7,8]
A.insert(2,100)
print(A)
A.insert(2,[10,20,30])
print(A)

#lists are mutable data types, not immutable, means they can be changed after you declare them
A=A.insert(2,60)
print(A)
 
s="123"
s[0]=5 #Strings are immutable but lists are mutable
A=[1,2,3]
A[0]=5
print(A)

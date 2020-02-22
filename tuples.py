#lists and tuples work the same but the difference is tuple cannot be changed- immutable datatypes
our_tuple=1,2,3,"A","B","C"
print(our_tuple)
print(type(our_tuple))
our_tuple=(1,2,3,"A","B","C")
#tuples are iterable datatypes just like strings and lists

print(our_tuple[0:3])

A=[1,2,3,4]
print(tuple(A))

(A,B,C) = 1,2,3
print(A)
print(B)
print(C)

(D,E,F)=[1,2,3]
print(D)
print(E)
print(F)

(G,H,I)="789"
print(G)
print(H)
print(I)



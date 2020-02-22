
#Ask user for name
name = input("What is yout name?: ")
#print(name)
#print(type(name))

#Ask user for age
age = input("How old are you?: ")
#age = int(age)
#age = raw_input("How old are you?: ")
#print(age)
#print(type(age))

#Ask user for city
city = input("What city do you live in?: ")
#print(city)

#Ask user what they enjoy
love = input("What do you love doing?: ")
#print(love)

#Create output text
string="Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, love)

#Print output to screen
print(output)


#playground
A="part"
B=1
print("{}-{}".format(A,B))
print("{1}-{0}".format(A,B))


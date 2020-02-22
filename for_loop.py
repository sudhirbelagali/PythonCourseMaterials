#for loop

#range function - create iterable of numbers
range(1,11)
#[1,2,3,4,5,6,7,8,9,10] - python-2
#it gives iterable in python 3

for number in range(1,11):
    print(number)

for number in [1,2,3,4]:
    print(number)
    
for letter in "sudhir":
    print(letter)

for number in range(1,11,2):
    print(number)

vowels = 0
consonants = 0

for letter in "supercalifragilisticexpialidocious":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == "":
        pass
    else:
        consonants = consonants + 1

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))

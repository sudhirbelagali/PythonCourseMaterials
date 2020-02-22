string = "ABCDEFG123456"
word = "supercalifragilisticexpialidocious"
print(word[0])
print(word[2])

#give one extra number

print(word[0:5:1])

print(word[0:5:2])

print(word[5:9:1]) 

print(word[5:])

print(word[5::2]) 

print(word[:8])

print(word[:5])

print(word[::-1])

print(word[::])

#print(word[-1:-5:1])

print(word[-2])
print(word[-5])
print(word[-1])
print(word.index("cali"))
print(word.index("fragi"))

print(word[word.index("cali"):word.index("fragi")])

print(word[word.index("docious")])

print(word[word.index("fragilistic"):word.index("exp")])

print(word[word.index("fragilistic"):word.index("e")])

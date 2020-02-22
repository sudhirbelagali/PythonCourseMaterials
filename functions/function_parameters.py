def about(name,age,likes):
    sentence = "Meet {}! they are {} years old and they like {}".format(name,age,likes)
    return sentence

ret = about("Jack",23,"Python")
print(ret)

ret = about(age=23,name="Jack",likes="Python") #function keywords
print(ret)


def about(name,age,likes="Python"):
    sentence = "Meet {}! they are {} years old and they like {}".format(name,age,likes)
    return sentence

ret = about(age=23,name="Jack") #function keywords
print(ret)

ret = about("Jack",23,"Football") #function keywords
print(ret)


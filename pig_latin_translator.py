#Pig latin translator - langugage - First it copies word till it gets vowel and
#appends the word at the end of the remaining word. and the final word should be
#appended with 'ay'
#if you have the word
#pig -> igPay
#happy -> appyHay
#duck -> uckDay
#glove -> oveGlay

#get sentence from the user
original = input("Please enter a sentence: ").strip().lower()

#split the sentence into words
words = original.split()
print(words)

#loop through the words and convert to pig latin
new_words = []

for word in words:
    print(word)
    #if it starts with vowel, just add "yay"
    if word[0] in "aeiou":
        new_word = word+"yay"
        new_words.append(new_word)
        print(new_words)
    #otherwise, move the first consonant cluster to the end, and add "ay"
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest+cons+"ay"
        new_words.append(new_word)
        print(new_words)
        
#stick words back together
output = " ".join(new_words)
# ["happy","birthday"] -> "happy birthday"
#output the final string

print(output)

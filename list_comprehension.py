#variable x stored in the list  and loops through 100

even_numbers = [x for x in range(1,101) if x%2==0]
print(even_numbers)

odd_numbers = [x for x in range(1,101) if x%2!=0]
print(odd_numbers)

words = ["the","quick","brown","fox","jumps","over","the","lazy","dog"]

answers = [[w.upper(),w.lower(),len(w)] for w in words]
print(answers)

print([[w.upper(),w.lower(),len(w)] for w in words])

 

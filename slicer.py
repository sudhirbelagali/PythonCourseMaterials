#get user email address

email = input("What is your email address?: ").strip()

#slice out the username

user = email[:email.index("@")]

#slice out the domain name

domain = email[email.index("@")+1:]

#format message

output = "Your username is {} and your domain name is {}.".format(user,domain)

#display output message

print(output)


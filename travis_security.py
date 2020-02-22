known_users = ["Alic", "Bob", "Sudhir", "Dan", "Claire","Georgie", "Harry"]
print(len(known_users))
#L=[1,2,3,4,5]
#print(2 in L)
#L=[1,2,3,4,5]
#del L[0]
#del L[0:2]

while True:
    print("Hi! My name is Travis")
    name = input("Hi! What is your name?: ").strip().capitalize()
    
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()
        
        if(remove == "y"):
            print(known_users)
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
            
    else:
        #print("Name NOT recognized")
        print("Hmm! I don't think I have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if(add_me == "y"):
            print(known_users)
            known_users.append (name)
            print(known_users)
        elif add_me == "n":
            print("No worries, see you around!")
            
    

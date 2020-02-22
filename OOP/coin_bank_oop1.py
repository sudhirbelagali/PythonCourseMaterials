#classes and objects
import random

class Pound:

    def __init__(self, rare=False): #constructor - self is specific instance of the class
                        #self would be replaced by coin1 when we instantiate the
                        #class with coin1
        self.rare = rare
        if self.rare:
            self.value=1.25
        else:
            self.value=1.00
            
        #self.value = 1.00
        self.color = "gold"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True
        #constructor doesnot return any value

    def __del__(self):
        #destructor
        print("Coin Spent!")        
        

    def rust(self):
        self.color="greenish"

    def clean(self):
        self.color="gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

coin1 = Pound(rare=True)
coin2 = Pound()

print(coin1.rare)
print(coin2.rare)

print(coin1.value)
print(coin2.value)

coin3 = Pound()
coin4 = Pound()
print(coin3.color)
print(coin4.color)
coin3.rust()
print(coin3.color)
print(coin4.color)

coin3.clean()
print(coin3.color)

print(coin3.heads)
coin3.flip()
#coin3.flip()
print(coin3.heads)


del coin1
print(coin1)




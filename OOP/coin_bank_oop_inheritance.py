#classes and objects
import random

class Coin:
    #generic class or abstract class
    def __init__(self, rare=True, clean=True,heads=True, **kwargs): #kwargs - keyword arguments

        for key,value in kwargs.items():
            setattr(self,key,value)
            #self.thickness = 3.15
            
        self.rare = rare
        self.clean = clean
        self.heads = heads
        
        if self.rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
            
        if self.clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color
            
    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color=self.clean_color

    def __del__(self):
        print("Coin Spent!")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
        

class Pound(Coin):
    def __init__(self):
        data = {
            "original_value":1.00,
            "clean_color":"gold",
            "rusty_color":"greenish",
            "num_edges":1,
            "diameter":22.5, #mm
            "thickness":3.15, #mm
            "mass":9.5
            }
        super().__init__(**data)

one_pound_coin = Pound()

print(one_pound_coin)

print(one_pound_coin.color)

one_pound_coin.rust()

print(one_pound_coin.color)

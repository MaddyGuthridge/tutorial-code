"""intro_to_classes.py

This file contains the source code for the tutorial video on my YouTube channel,
Introduction to Classes. This video is available at:
https://youtu.be/0OM8OMDJ5yg

Author: Miguel Guthridge
"""

class Pet:
    name = ""
    animal_type = ""
    sound = ""
    
    def __init__(self, name, animal_type, sound):
        self.name = name
        self.animal_type = animal_type
        self.sound = sound

    def make_noise(self):
        print(f"{self.name} the {self.animal_type}: {self.sound}")

my_first_pet = Pet("Sally", "dog", "Woof")
my_second_pet = Pet("Tiggy", "cat", "Meow")

my_first_pet.make_noise()
my_second_pet.make_noise()

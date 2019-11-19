
from cat import Cat
from random import randint

# "Give me everything from Cat so I can customize my version"
# This is called "Inheritance"
# We say that CuddlyCat inherits from Cat.
# Or: CuddlyCat is a subclass of Cat.
# Cat is the superclass of CuddlyCat.

class CuddlyCat(Cat):
    
    def cuddle(self, whom):
        cuddle_chance = randint(0, 10)/10
        if cuddle_chance <= self.friendliness:
            print(f"I cuddle you, {whom.name}!")
            whom.happiness *= self.cuddle_power
        else:
            print(f"Bad touch, bad touch!")

artemis = CuddlyCat("Artie")




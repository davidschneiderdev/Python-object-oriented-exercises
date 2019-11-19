
from random import randint

class Cat:
    # In __init__ python allows you to refer to 
    # the object as its being created
    def __init__(self, name, friendliness=0.5, happiness=10, cuddle_power=3):
        self.name = name
        self.friendliness = friendliness
        self.happiness = happiness
        self.cuddle_power = cuddle_power

    def greet(self, whom):
        print(f"Hello I am {self.name}. Nice to meet you {whom.name}!")

    def cuddle(self, whom):
        cuddle_chance = randint(0, 10)/10
        if cuddle_chance <= self.friendliness:
            print(f"I cuddle you, {whom.name}!")
            whom.happiness += self.cuddle_power
        else:
            print(f"Bad touch, bad touch!")

    
milla = Cat("Milla")
oakley = Cat("Oakley") # Use the class to create a new Cat "instance"







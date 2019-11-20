
from random import randint
from toy import Toy

# Classes are for:
# bundling related data (like a dictionary)
# with the functions that modify that data

# Encapsulation - hiding the details about how something is done (usually inside of methods)
# Encapsulation, alternate definition - bundling related data along with functions that use and modify that data.

# Inheritance - making specialized versions of classes.

# Polymorphism - methods can interact with lots of different kinds of objects, and it doesn't care what Class created it.

# Composition - not stuffing everything into a single class. Instead make classes that help other classes. Create specialized objects that cooperate with each other.



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

    def receive_toy(self, toy):
        # You can add new properties to an object in any method
        # not just __init__()
        self.toy = toy

    def play_with_toy(self):
        print(f"{self.name} plays with {self.toy.name}")
        self.happiness += self.toy.quality
    
milla = Cat("Milla")
oakley = Cat("Oakley") # Use the class to create a new Cat "instance"






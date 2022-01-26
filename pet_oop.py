class Pet:
    def __init__(self, input_name, input_age, input_breed = None, input_friendliness = False):
        self.name = input_name
        self.age = input_age
        self.breed = input_breed
        self.friends = []
        self.friendliness = input_friendliness
    # use on the pet's birthday 
    def birthday(self):
        self.age += 1 
        print(("happy birthday {name}! You are now {age} years old.").format(name=self.name, age = self.age))
    # trying to interact
    def interact(self, otherHamster):
        if otherHamster.friendliness:
            self.friends.append(otherHamster)
            print("they are now friends")
            print("the friendlist is now", self.friends)
        else:
            print("They are not friends")

Hamster1 = Pet("Boba", 1, input_friendliness=True, input_breed="Syrian Hamster")
Hamster2 = Pet("Oompa", 1, input_friendliness=False, input_breed="Dog")
Hamster3 = Pet("loompa", 2, input_friendliness=True, input_breed="Cat")
Hamster1.interact(Hamster3)


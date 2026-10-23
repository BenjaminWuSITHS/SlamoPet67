class pet:                                 
    def __init__(self, name, hunger=0, time=0, hp=100): 
        self.name = name                     
        self.hunger = hunger
        self.hp = hp
        self.time = time


    def timepasses(self):                        
        self.hunger += 1
        self.time += 1
        if self.time % 12 and self.time != 0:
            self.time = 0
        elif self.hunger > 10:
            self.ouch

    def feed(self):
        self.hunger -= 3
        self.timepasses

    def nap(self):
        for i in range(3):
            self.timepasses
        self.time += 8

    def ouch(self):
        self.hp -= 10

def getstats():
    print(pets.name)
    print("--------------------------")
    print(f"Health: {pets.hp}")
    print(f"The current time = {pets.time}:00")
    print(f"Hunger: {pets.hunger}")
    print("--------------------------")

def action():
    print("j")

name = input("What would you like to name ur pet?")
pets = pet(name)      

while pets.hp > 0:
    

import random

class pet:                                 
    def __init__(self, name, energy=100, happiness=5, thirst=0, hunger=0, time=0, hp=100): 
        self.name = name                     
        self.hunger = hunger
        self.hp = hp
        self.time = time
        self.happiness = happiness
        self.thirst = thirst
        self.energy = energy


    def timepasses(self):                        
        self.hunger += 0.5
        self.thirst += 0.5
        self.energy -= 2
        self.time += 1
        if self.time % 24 == 0 and self.time != 0:
            self.time = 0
        elif self.thirst > 10 and self.hunger > 10:
            for i in range(2):
                self.ouch()
                self.happiness -= 2
        elif self.hunger > 10 and self.thirst < 10:
            self.ouch()
            self.happiness -= 1
        elif self.thirst > 10 and self.hunger < 10:
            self.ouch()
            self.happiness -= 1
        elif self.energy == -100:
            for i in range(8):
                self.ouch()
        elif self.happiness < 0:
            self.happiness = 0
        

    def feed(self):
        self.timepasses()
        self.hunger -= 3.5
        self.energy += 17
        self.hp += 15
        self.happiness +=1
        if self.hunger >= 10:
            self.hunger -= 5
            self.energy += 15
        elif self.hunger < 0:
            self.hunger = 0
        elif self.energy > 100:
            self.energy = 100
        elif self.happiness < 0:
            self.happiness = 0   

    def drink(self):
        self.timepasses()
        self.energy += 7
        self.hp += 5
        self.thirst -= 3.5
        if self.thirst >= 10:
            self.thirst-= 5
            self.energy += 5
        elif self.thirst < 0:
            self.thirst = 0
        elif self.energy > 100:
            self.energy = 100

    def play(self):
        self.timepasses()
        self.happiness += 1.5
        if self.happiness < 0:
            self.happiness = 0
        elif self.happiness <= 3:
            self.happiness += 4
            self.energy -= 15
        else:
            self.energy -= 8
        if self.energy < -100:
            self.energy = -100

        

    def nap(self):
        for i in range(3):
            self.timepasses()
        self.time += 8
        self.energy += 20
        self.happiness += 0.5
        if self.energy <= 39:
            self.energy +=10
        if self.energy <= 0:
            self.energy +=15
        elif self.energy > 100:
            self.energy = 100

    def ouch(self):
        self.hp -= 10

def getstats():
    print(pets.name)
    print("STATS")
    print("--------------------------")
    print(f"Health: {pets.hp}")
    print(f"The current time = {pets.time}:00")
    print(f"Hunger: {pets.hunger}")
    print(f"Thirst: {pets.thirst}")
    print("--------------------------")
    print(f"Happiness: {pets.happiness}")
    print(f"Energy: {pets.energy}")
    print("--------------------------")

def action():
    getstats()
    print(f"What would you like to do with {pets.name}?")
    action = input().lower()
    if action == "nap":
        if pets.energy == 100:
            pets.timepasses()
            return(f"{pets.name} tried to nap but was simply too energetic!")
        elif 100 > pets.energy >= 90:
            pets.nap()
            return(f"{pets.name} did not need this nap, but enjoyed it anyway!")
        elif 89 > pets.energy >= 40:
            pets.nap()
            return(f"{pets.name} had a nice nap!")
        elif 39 > pets.energy >= 10:
            pets.nap()
            return(f"{pets.name} desperately climbed into bed and fell to sleep instantly.")
        elif 9 > pets.energy >= -50:
            pets.nap()
            return(f"{pets.name} went unconscious instantly when being dropped on the bed.")
        else:
            pets.nap()
            return(f"{pets.name} literally almost died crawling to the bed.")
    elif action == "feed":
        if pets.hunger == 0:
            pets.timepasses()
            return(f"{pets.name} didn't take a bite of its meal")
        elif 3 > pets.hunger >= 1:
            pets.nap()
            return(f"{pets.name} ate their food with a big smirk")
        elif 6 > pets.hunger >= 3:
            pets.nap()
            return(f"{pets.name} quickly gobbled down whatever was on the plate")
        elif 15 > pets.hunger >= 6:
            pets.nap()
            return(f"{pets.name} evis")
        else:
            pets.nap()
            return(f"{pets.name} literally almost died crawling to the bed.")
    elif action == "drink":
        pets.drink()
    elif action == "play":
        pets.play()
    elif action == "punch":
        pets.ouch()
        pets.timepasses()
        return(f"You punt {pets.name} across the room, it is beaten up and crying")
    else:
        pets.timepasses()


name = input("What would you like to name your pet?")
pets = pet(name)      

while pets.hp > 0:
    print(action())
    print("--------------------------")
print(f"{pets.name} has died.")
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
        if self.time % 12 and self.time != 0:
            self.time = 0
        elif self.thirst > 10 and self.hunger > 10:
            for i in range(2):
                self.ouch
        elif self.hunger > 10 and self.thirst < 10:
            self.ouch
        elif self.thirst > 10 and self.hunger < 10:
            self.ouch

        

    def feed(self):
        self.hunger -= 3
        self.energy += 15
        self.hp += 15
        if self.hunger >= 10:
            self.hunger -= 5
            self.energy += 15
        if self.hunger < 0:
            self.hunger = 0
        if self.energy > 100:
            self.energy = 100
        self.timepasses

    def drink(self):
        self.energy += 5
        self.hp += 5
        self.thirst -= 3
        if self.thirst >= 10:
            self.thirst-= 5
            self.energy += 5
        if self.thirst < 0:
            self.thirst = 0
        if self.energy > 100:
            self.energy = 100
        self.timepasses

    def play(self):
        self.happiness += 1.5
        if self.happiness < 0:
            self.happiness = 0
            self.energy -= 10
        if self.happiness <= 3:
            self.happiness += 4
            self.energy -= 15
        self.timepasses

    def nap(self):
        for i in range(3):
            self.timepasses
        self.time += 8
        self.energy += 20
        if self.energy > 100:
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
    action = input().lower
    if action == "nap":
        pets.nap
    if action == "nothing":
        pets.timepasses
    if action == "feed":
        pets.feed
    if action == "drink":
        pets.drink
    if action == "play":
        pets.play


name = input("What would you like to name your pet?")
pets = pet(name)      

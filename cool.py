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


    def check(self):
        if self.hunger < 0:
            self.hunger = 0
        if self.hunger > 20:
            self.hunger = 20
        if self.thirst < 0:
            self.thirst = 0
        if self.thirst > 20:
            self.thirst = 20
        if self.hp > 100:
            self.hp = 100
        if self.happiness > 20:
            self.happiness = 20
        if self.happiness < 0:
            self.happiness = 0
        if self.energy > 100:
            self.energy = 100
        if self.energy < -100:
            self.energy = -100

    def timepasses(self):                        
        self.hunger += 0.5
        self.thirst += 0.5
        self.energy -= 2
        self.time += 1
        if self.time % 24 == 0 and self.time != 0:
            self.time = 0
        if self.thirst > 10 and self.hunger > 10:
            for i in range(2):
                self.ouch()
                self.happiness -= 2
        if self.hunger > 10 and self.thirst < 10:
            self.ouch()
            self.happiness -= 1
        if self.thirst > 10 and self.hunger < 10:
            self.ouch()
            self.happiness -= 1
        if self.energy == -100:
            for i in range(8):
                self.ouch()
        if self.happiness < 0:
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
        self.check()

    def drink(self):
        self.timepasses()
        self.energy += 7
        self.hp += 5
        self.thirst -= 3.5
        if self.thirst >= 10:
            self.thirst-= 5
            self.energy += 5
        self.check()

    def play(self):
        self.timepasses()
        self.happiness += 1.5
        self.energy -= 8
        self.hunger += 1
        self.thirst += 1
        if self.happiness < 0:
            self.happiness = 0
        if self.happiness <= 3:
            self.happiness += 4
            self.energy -= 15
            self.hunger += 0.5
            self.thirst += 0.5
        self.check()

        

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
        self.check()

    def ouch(self):
        self.hp -= 10
        self.check()

def getstats():
    print(pets.name)
    print("STATS")
    print("--------------------------")
    print(f"Health: {pets.hp}/100")
    print(f"The current time = {pets.time}:00")
    print(f"Hunger: {pets.hunger}/20")
    print(f"Thirst: {pets.thirst}/20")
    print("--------------------------")
    print(f"Happiness: {pets.happiness}/20")
    print(f"Energy: {pets.energy}/100")
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
        elif 3 > pets.hunger > 0:
            pets.feed()
            return(f"{pets.name} ate their food with a big smirk")
        elif 6 > pets.hunger >= 3:
            pets.feed()
            return(f"{pets.name} quickly gobbled down whatever was on the plate")
        elif 15 > pets.hunger >= 6:
            pets.feed()
            return(f"{pets.name} eviserated every ounce of food in the universe...")
        else:
            pets.feed()
            return(f"{pets.name}'s limp, hungered skeleton limped acrossed the floor, dead..?")
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


deathstats = [pets.hunger, pets.thirst]
if max(deathstats) == pets.thirst and max(deathstats) == pets.hunger:
    print(f"{pets.name}'s shriveled and bare skeleton was already dead, limp, before turning into a pile of dust with a grim skull of {pets.name} ontop. You hear sirens in the background. Evading the police would be easy, you thought as you quickly scramble towards your house. Hiding in the crawlspace, you hear the FBI barging in 'FBI OPEN UP!' You stay absolutely silent. Why did you not nourish your only goal in your life? Unfortunately for you, the FBI prys the floorboards up and you are shot instantly. Your gravestone lies directly across from {pets.name}'s grave. This is your end.")
elif max(deathstats) == pets.thirst and max(deathstats) != pets.hunger:
    print(f"{pets.name}'s shriveled body gave its last breath before turning into a small raisin which is picked up by a vulture overhead.")
elif max(deathstats) == pets.hunger and max(deathstats) != pets.thirst:
    print(f"{pets.name}'s bare skeleton crawled across the floor, begging for the food in your hand, but it suddenly went limp and was picked up by a vulture overhead.")
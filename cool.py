class pet:                                  # 1. the class name (Capitalized)
    def __init__(self, name, hunger=10, sleep=0, hp=100): # 2. setup method, runs on creation
        self.name = name                     # 3. attributes saved on "self"
        self.hunger = hunger
        self.hp = hp
        self.sleep = sleep


    def timepasses(self):                        # 4. a method - always takes self first
        self.hunger -= 1
        self.sleep += 1

    def feed(self):
        self.hunger += 3
        self.timepasses

    def takeabigassnap(self):
        for i in range(5):
            self.timepasses
        self.sleep += 8

    def ouch(self):
        self.hp -= 10



input("What would you like to name ur pet?") = pet("Ethan Chen")                




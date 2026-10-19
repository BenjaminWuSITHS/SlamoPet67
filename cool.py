class Hero:                                  # 1. the class name (Capitalized)
    def __init__(self, name, money, hp=100): # 2. setup method, runs on creation
        self.name = name                     # 3. attributes saved on "self"
        self.money = money
        self.hp = hp

    def potion(self):                        # 4. a method - always takes self first
        self.hp += 10

class Hero:                                  # 1. the class name (Capitalized)
    def __init__(self, name, money, hp=100): # 2. setup method, runs on creation
        self.name = name                     # 3. attributes saved on "self"
        self.money = money
        self.hp = hp

    def potion(self):                        # 4. a method - always takes self first
        self.hp += 10

athena = Hero("Athena", 500)                 # 5. create an object
athena.potion()                              # 6. call a method with a dot
print(athena.hp)                             # 110

class Ethan():
      def __init__(self, chillness, coolness):
           self.chillness = chillness
           self.coolness = coolness
      def chill(self):
            print("I am SOOOOO chill")
            self.chillness += 10
      def cool(self):
            print("I am SOOOOO cool")
            self.coolness += 10

ethan = Ethan("ethan", 0, 0)

ethan.chillness
class Entity:
    def __init__(self, name:str, attack, defense, health, max_health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
        self.max_health = max_health
        self.defend = False

    def add_health(self, amount):
        if self.health + amount > self.max_health:
            self.health = self.max_health
        elif self.health + amount < 0:
            self.health = 0
        else:
            self.health += amount

    def perform_attack(self, target):
        if target.defend:
            target.add_health(self.attack - target.defense)
            target.use_defense()
        else:
            target.add_health(-self.attack)

    def perform_defense(self):
        self.defend = True

    def use_defense(self):
        self.defend = False

class Player(Entity):
    def __init__(self, name:str):
        super().__init__(name, 1, 1, 100, 100)

    def add_attack(self, amount):
        self.attack += amount
    def add_defense(self, amount):
        self.defense += amount
    def add_max_health(self, amount):
        self.max_health += amount

#the below is likely not to be used
class Enemy(Entity):
    def __init__(self, name:str):
        super().__init__(name, 1, 1, 100, 100)
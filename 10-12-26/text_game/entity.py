import room

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
        print(f"Their health is {self.health}")

    def perform_attack(self, target):
        if target.defend:
            attack_amount = self.attack - target.defense
            if attack_amount < 0:
                attack_amount = 0
            target.add_health(-attack_amount)
            target.use_defense()
        else:
            target.add_health(-self.attack)

    def perform_defense(self):
        self.defend = True

    def use_defense(self):
        self.defend = False

class Player(Entity):
    def __init__(self, name:str, start_location_name: str):
        super().__init__(name, 1, 1, 100, 100)
        self.location = start_location_name
        self.items = []

    def add_attack(self, amount):
        self.attack += amount
    def add_defense(self, amount):
        self.defense += amount
    def add_max_health(self, amount):
        self.max_health += amount
    def get_item(self, item):
        print(f"You take the {item.name}")
        self.items.append(item.name)
        for stat in item.stat_pairs:
            if stat[0] == "attack":
                self.add_attack(stat[1])
            elif stat[0] == "defense":
                self.add_defense(stat[1])
            elif stat[0] == "max_health":
                self.add_max_health(stat[1])
        print(f"Your stats are now: Attack={self.attack}, Defense={self.defense}, Health={self.health}/{self.max_health}")


    def go_to(self, go_to_room_name: str, from_room: room.Room):
        #TODO check if import is necessary
        if go_to_room_name in from_room.get_connections():
            self.location = go_to_room_name
        else:
            print("You can't go there!")

    def __str__(self):
        return f"You are {self.name}, you are currently at {self.location}. Your health is {self.health} out of a possible {self.max_health} max health, your attack is {self.attack}, your defense is {self.defense}\nYou are holding {self.items}"

class NPC(Entity):
    def __init__(self, name:str, attack, defense, health, max_health, talk):
        super().__init__(name, attack, defense, health, max_health)
        self.talk = talk

    def __str__(self):
        return self.talk

class Item:
    def __init__(self, name:str, stat_pairs: list):
        self.name = name
        self.stat_pairs = stat_pairs

#the below is likely not to be used
class Enemy(Entity):
    def __init__(self, name:str):
        super().__init__(name, 1, 1, 100, 100)
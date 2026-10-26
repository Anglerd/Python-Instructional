from utils import get_input
import sys
import db_connector
from db_config import db_config
"""
pokemon = [
    card,
    card
]
"""
"""
card = {
    "set_number": 1,
    "name": "charizard",
    "category": "Pokemon",
    "type": "Fire",
    "rarity": "Rare"
}

set_stuff = ["name1", "name2"]

def load_card(set_number, name, category, type, rarity):
    return {
    "set_number": set_number,
    "name": name,
    "category": category,
    "type": type,
    "rarity": rarity
}
"""

class Card:
    def __init__(self, set_number, name, category, type, rarity):
        self.set_number = set_number
        self.name = name
        self.category = category
        self.type = type
        self.rarity = rarity

    def __str__(self):
        return f"This is {self.name}, a {self.category} card with the type {self.type}. It is a {self.rarity} in set number {self.set_number}"

table_name = "card"

global_enums = {
    "category": db_connector.get_enums(db_config["database"], table_name, "category"),
    "type": db_connector.get_enums(db_config["database"], table_name, "type"),
    "rarity": db_connector.get_enums(db_config["database"], table_name, "rarity")
}

# card_sets = ["name1", "name2"]

class Set:
    def __init__(self, name):
        self.name = name

def check_enums(enum_to_check):
    while True:
            user_input = input(f"Enter the {enum_to_check} of this card")
            for this_enum in global_enums[enum_to_check]:
                if user_input.lower() == this_enum.lower():
                    return user_input
            print(f"That is not an allowed {enum_to_check}, please enter an entry from the following {global_enums[enum_to_check]}")

if __name__ == "__main__":
    print(Card(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]))
    print(sys.argv[6] + sys.argv[7])
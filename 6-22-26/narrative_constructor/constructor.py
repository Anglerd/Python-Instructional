import random

class Player:
    def __init__(self, name, alignment=0, level=1, weapon=""):
        self.name = name
        self.alignment = alignment
        self.level = level
        self.weapon = weapon
    
    def level_up(self):
        self.level += 1

# some_players = {player_name: player, player_name: player}

class Action:
    def __init__(self, action_type, this_player, action_result=""):
        self.action_type = action_type
        self.result = action_result
        self.player = this_player
        # self.player = player("Trudy", 0, 1)

    def make_sentence(self, fancy_adjectives):
        this_transition = f" {get_rand_array(transitions)} {self.result}" if self.result else ""
        some_adjective = f" {get_rand_array(fancy_adjectives[self.player.alignment])}" if random.randrange(10) > 3 else ""
        return f"{self.player.name}{some_adjective} {self.action_type}{this_transition}"

transitions = [" which caused ", " this resulted in "]

def get_rand_array(array):
    return array[random.randrange(array.__len__())]

# action_history = [action, action]

if __name__ == "__main__":
    this_character = Player("Trudy")
    this_action = Action("swung a sword", this_character)
    print(this_action.make_sentence())
    this_action.result = "this kills the crab"
    print(this_action.make_sentence())
import entity
from room import Room
import combat_logic
def get_input(prompt, type_converter):
    while True:
        try:
            return type_converter(input(f"{prompt}\n"))
        except ValueError:
            print(f"Please enter a valid value of the type {type_converter}")

def load_player_history():
    #eventually will load from mysql to determine if the player has done anything so far
    return None

def load_rooms():
    return {
    "ballroom": Room("Large Chandelier"),
    "foyer": Room("Large Staircase"),
    "throne room": Room("Large Chair")
}

def dev_add_connections(castle):
    for dev_room in castle.values():
        for second_room in castle.values():
            dev_room.add_connection(second_room)

if __name__ == "__main__":
    this_castle = load_rooms()
    #dev_add_connections(this_castle)
    player_history = load_player_history()
    if not player_history:
        print("Welcome to Spookies jumpscarrrre mansion")
        player = entity.Player(input("What is your name?\n"), this_castle["foyer"])
    else:
        #TODO add loading logic here
        player = entity.Player("john", this_castle["ballroom"])
    while True:
        this_room = player.location
        this_name = "Default"
        """
        for room in this_castle:
            if room == this_room:
                #TODO double check how to get the key name from a dictionary
                this_name = room.get_key()
                break
        """
        print(f"This is the {this_name} {this_room}")
        if this_room.trap:
            print("This room was trapped!")
            this_room.trap()
            print(f"Your health is now {player.health}")
        if this_room.npc:
            npc_prompt = input(f"Would you like to talk or attack to {this_room.npc}\n").lower().strip()
            if npc_prompt == "talk":
                print(this_room.talk.npc)
            else:
                while combat_logic.check_combat_end(player, this_room.npc):
                    combat_prompt = get_input("Enter 1 to attack or 2 to defend", int)
                    player.use_defense()
                    this_room.npc.use_defense()
                    if combat_prompt == 1:
                        combat_logic.combat_turn("attack", player, this_room.npc)
                    else:
                        combat_logic.combat_turn("defend", player, this_room.npc)
        while True:
            player_prompt = input("What would you like to do?\n").lower().strip()
            if "go" == player_prompt:
                location_prompt = input("Where would you like to go?\n").lower().strip()
                player.go_to(location_prompt)
            elif "heal" == player_prompt:
                this_room.heal(player)
            elif "take" == player_prompt:
                item_prompt = input("What would you like to take?\n").lower().strip()
                this_item = this_room.get_item(item_prompt)
                if this_item:
                    player.get_item(this_item)
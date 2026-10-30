import entity
from room import Room
import combat_logic
def get_input(prompt, type_converter):
    while True:
        try:
            return type_converter(input(f"{prompt}\n"))
        except ValueError:
            print(f"Please enter a valid value of the type {type_converter}")

def load_rooms():
    """Does all the logic to load the rooms"""
    #step 1, Load most room data except connections
    these_rooms = {
        "ballroom": Room("Large Chandelier", heal=20),
        "foyer": Room("Large Staircase", save=True),
        "throne room": Room("Large Chair", trap=50),
        "weapon room": Room("Weapon Rack", item_list= [
            entity.Item("Blade of awesomeness", [
                ("attack", 1)
                ])
        ]),
        "cantina": Room("Cantina chicken wrap", npc=entity.NPC("George Romero",
                                                               100,
                                                               100,
                                                               1000,
                                                               1000,
                                                               "I'm gonna eat you")),
    }
    #step 2, load connections, connections cannot be loaded in step 1 as the connecting room doesn't exist yet
    these_connections = [
        ("ballroom", "foyer"),
        ("ballroom", "throne room"),
        ("ballroom", "cantina"),
        ("ballroom", "weapon room"),
        ("foyer", "throne room"),
        ("foyer", "cantina"),
    ]
    for connection in these_connections:
        these_rooms[connection[0]].add_connection(connection[1])
        these_rooms[connection[1]].add_connection(connection[0])
    return these_rooms

def load_player_history():
    #eventually will load from mysql to determine if the player has done anything so far
    return None

"""
def dev_add_connections(castle):
    for dev_room in castle.values():
        for second_room in castle.values():
            dev_room.add_connection(second_room)
"""

if __name__ == "__main__":
    this_castle = load_rooms()
    #dev_add_connections(this_castle)
    player_history = load_player_history()
    if not player_history:
        print("Welcome to Spookies jumpscarrrre mansion")
        player = entity.Player(input("What is your name?\n"), "cantina")
    else:
        #TODO add loading logic here
        player = entity.Player("john", "ballroom")
    while True:
        this_room_name = player.location
        this_room = this_castle[this_room_name]
        """
        for room in this_castle:
            if room == this_room:
                #TODO double check how to get the key name from a dictionary
                this_room_name = room.get_key()
                break
        """
        print(f"This is the {this_room_name} {this_room}")
        if this_room.trap:
            print("This room was trapped!")
            this_room.get_trap(player)
            # print(f"Your health is now {player.health}") # add_health now mentions current health
        combat = False
        if this_room.npc:
            npc_prompt = input(f"Would you like to talk or attack to {this_room.npc.name}\n").lower().strip()
            if npc_prompt == "talk":
                print(f"They say {this_room.npc}")
            else:
                combat = True
                while not combat_logic.check_combat_end(player, this_room.npc):
                    combat_prompt = get_input("Enter 1 to attack or 2 to defend", int)
                    if combat_prompt == 1:
                        combat_logic.combat_turn("attack", player, this_room.npc)
                    else:
                        combat_logic.combat_turn("defend", player, this_room.npc)
        if combat:
            print(f"This is the {this_room_name} {this_room}")
        player_prompt = input("What would you like to do?\n").lower().strip()
        if "go" == player_prompt:
            location_prompt = input("Where would you like to go?\n").lower().strip()
            player.go_to(location_prompt, this_room)
            if player.location == "foyer" and "Blade of awesomeness" in player.items:
                print("You win!")
                quit()
        elif "heal" == player_prompt:
            this_room.get_heal(player)
        elif "take" == player_prompt:
            for item in this_room.get_all_items():
                print(f"You see a {item.name}")
            item_prompt = input("What would you like to take?\n").lower().strip()
            this_item = this_room.get_item(item_prompt)
            if this_item:
                player.get_item(this_item)
            else:
                print("That item doesn't exist")
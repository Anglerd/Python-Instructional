class Room:
    def __init__(self, room_description, npc=None, item_list=None, trap=False, heal=False, save=False):
        self.room_description = room_description
        self.connections = []
        self.npc = npc
        self.item_list = item_list
        self.trap = trap
        self.heal = heal
        self.save = save

    def add_connection(self, connection: str):
        self.connections.append(connection)

    def get_connections(self):
        return self.connections
    """#remove a rickety bridge after use
    def remove_connection(self, connection):
        self.connections.remove(connection)
    """
    def get_all_items(self):
        return self.item_list

    def get_item(self, item: str):
        if self.item_list:
            for this_item in self.item_list:
                if this_item.name.lower().strip() == item:
                    self.item_list.remove(this_item)
                    return this_item
        return None

    def get_trap(self, player):
        if self.trap:
            player.add_health(-self.trap)
            self.trap = False
    def get_heal(self, player):
        if self.heal:
            player.add_health(self.heal)
            self.heal = False

    def __str__(self):
        #Caller should say something like f"This is the {room_name} {room}"
        room_string = self.room_description
        if self.npc:
            room_string += f"\nYou can see a {self.npc.name}"
        if self.heal:
            room_string += f"\nThere is a healing fountain in this room"
        if self.save:
            room_string += f"\nYou can save in this room"
        for connection in self.connections:
            room_string += f"\nThis room connects to the {connection}"
        #crazy single f-string below
        #single_line = f"{self.room_description}{f"\n{You can see a {self.npc.name}" if self.npc else ""}{"\nThere is a healing fountain in this room" if self.heal else ""}"#etc...
        return room_string

this_castle = {
    "ballroom": Room("Large Chandelier"),
    "foyer": Room("Large Staircase"),
    "throne room": Room("Large Chair")
}

"""
# connection section
this_castle["ballroom"].add_connection(this_castle["throne room"])
this_castle["ballroom"].add_connection(this_castle["foyer"])
this_castle["throne room"].add_connection(this_castle["foyer"])
"""
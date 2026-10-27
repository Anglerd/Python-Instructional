class Room:
    def __init__(self, room_description, action_list=None, npc=None, item_list=None):
        self.room_description = room_description
        self.connections = []
        self.action_list = action_list
        self.npc = npc
        self.item_list = item_list

    def add_connection(self, connection, connect_back:bool=True):
        self.connections.append(connection)
        if connect_back:
            connection.add_connection(self, False)

    def get_connections(self):
        return self.connections
    """#remove a rickety bridge after use
    def remove_connection(self, connection):
        self.connections.remove(connection)
    """
    def get_all_items(self):
        return self.item_list
    def get_item(self, item):
        self.item_list.remove(item)
        return self.item_list[item]


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
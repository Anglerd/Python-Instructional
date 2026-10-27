"""
rooms
player can walk into rooms
things will happen in rooms including:
    combat
    loot
    trap
    talk to npc
    heal
    save
players walk between rooms

history will be saved of player actions that gets saved to db when players save
load happens from db
"""

# 3 ways of performing the same concepts

# Way 1, all dictionaries

def create_room(room_description):
    return {"room_description": room_description,
            "room_connections": []
            }

def connect_rooms(castle, connection_list):
    for room in castle:
        for connection in connection_list:
            if room in connection:
                room["connections"].append(connection)

all_room_connections = [
    ["ballroom", "foyer"],
    ["ballroom", "throne room"],
    ["throne room", "foyer"]
]

this_castle = {
    "ballroom": create_room("Large Chandelier"),
    "foyer": create_room("Large Staircase"),
    "throne room": create_room("Large Chair")
}

connect_rooms(this_castle, all_room_connections)

player_location = this_castle["foyer"]
player_location = this_castle["ballroom"]

# Way 2 dictionary of room classes

class Room:
    def __init__(self, room_description):
        self.room_description = room_description
        self.connections = []

    def add_connection(self, connection, connect_back:bool=True):
        self.connections.append(connection)
        if connect_back:
            connection.add_connection(self, False)

this_castle = {
    "ballroom": Room("Large Chandelier"),
    "foyer": Room("Large Staircase"),
    "throne room": Room("Large Chair")
}

# connection section
this_castle["ballroom"].add_connection(this_castle["throne room"])
this_castle["ballroom"].add_connection(this_castle["foyer"])
this_castle["throne room"].add_connection(this_castle["foyer"])

player_location = this_castle["foyer"]
player_location = this_castle["ballroom"]

# Way 3 list of dictionaries, as can be seen this way is "unwieldy" and hard to use properly

this_castle = [
    {
        "room_name": "ballroom",
        "connections": []
    },
    {
        "room_name": "throne room",
        "connections": []
    },
    {
        "room_name": "foyer",
        "connections": []
    }
]

player_location = this_castle[2]
player_location = this_castle[0]
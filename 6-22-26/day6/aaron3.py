class rooms(
    
)

rooms = {
    "outside": {
        "description": "You are outside a dark stone house. A path leads north.",
        "exits": {"north": "foyer"},
        "items": []
    },
    "foyer": {
        "description": "You are in the foyer. Dust covers the floor. Doors lead east and west.",
        "exits": {"south": "outside", "east": "library", "west": "kitchen"},
        "items": ["key"]
    },
    "library": {
        "description": "Tall bookshelves surround you. One book seems oddly out of place.",
        "exits": {"west": "foyer", "north": "secret room"},
        "items": ["book"]
    },
    "kitchen": {
        "description": "You are in an old kitchen. A locked trapdoor is on the floor.",
        "exits": {"east": "foyer", "down": "cellar"},
        "items": ["lantern"]
    },
    "secret room": {
        "description": "You found a secret room filled with ancient markings ooo wonder if that will be relevent.",
        "exits": {"south": "library"},
        "items": ["treasure"]
    },
    "cellar": {
        "description": "The cellar is dark and cold. Something shiny rests in the corner.",
        "exits": {"up": "kitchen"},
        "items": ["coin"]
    }
}
 
current_room = "outside"
inventory = []
game_running = True
 
 
def show_room():
    room = rooms[current_room]
    print("\n" + room["description"])
 
    if room["items"]:
        print("You see:", ", ".join(room["items"]))
 
    print("Exits:", ", ".join(room["exits"].keys()))
 
 
def show_help():
    print("""
Commands:
  go north/east/south/west/up/down
  take item
  drop item
  inventory
  look
  help
  quit
""")
 
 
def move(direction):
    global current_room
 
    room = rooms[current_room]
 
    if direction not in room["exits"]:
        print("You cannot go that way.")
        return
 
    # Locked cellar rule
    if current_room == "kitchen" and direction == "down":
        if "key" not in inventory:
            print("The trapdoor is locked. You need a key.")
            return
 
    current_room = room["exits"][direction]
    show_room()
 
 
def take_item(item):
    room = rooms[current_room]
 
    if item not in room["items"]:
        print("That item is not here.")
        return
 
    room["items"].remove(item)
    inventory.append(item)
    print(f"You picked up the {item}.")
 
    check_win()
 
 
def drop_item(item):
    if item not in inventory:
        print("You do not have that item.")
        return
 
    inventory.remove(item)
    rooms[current_room]["items"].append(item)
    print(f"You dropped the {item}.")
 
 
def check_win():
    if "treasure" in inventory and "coin" in inventory:
        print("\nYou collected the treasure and the coin!")
        print("You win!")
        quit()
 
 
def handle_command(command):
    if command == "":
        print("Please enter a command.")
        return
 
    words = command.lower().split()
 
    if words[0] == "go":
        if len(words) < 2:
            print("Go where?")
        else:
            move(words[1])
 
    elif words[0] == "take":
        if len(words) < 2:
            print("Take what?")
        else:
            item = " ".join(words[1:])
            take_item(item)
 
    elif words[0] == "drop":
        if len(words) < 2:
            print("Drop what?")
        else:
            item = " ".join(words[1:])
            drop_item(item)
 
    elif words[0] == "inventory":
        if inventory:
            print("Inventory:", ", ".join(inventory))
        else:
            print("Your inventory is empty.")
 
    elif words[0] == "look":
        show_room()
 
    elif words[0] == "help":
        show_help()
 
    elif words[0] == "quit":
        print("Thanks for playing!")
        quit()
 
    else:
        print("I do not understand that command.")
 
 
print("Welcome to Mini Game!")
print("Type 'help' to see commands.")
show_room()
 
while game_running:
    user_input = input("\n> ")
    handle_command(user_input)
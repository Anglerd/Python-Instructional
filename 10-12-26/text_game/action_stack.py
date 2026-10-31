import entity
import room
action_dict = {
    "GO": entity.Player.go_to,
    "COMBAT": entity.Player.add_health,
    "TRAP": entity.Player.add_health,
    "HEAL": entity.Player.add_health,
    "TAKE": entity.Player.get_item,
    "KILL": room.Room.kill_npc
}

class Calculator:
    def add(self, x, y):
        return x + y
calc = Calculator()
method_name = "add"
# Get the method and call it
method = getattr(calc, method_name)
result = method(5, 3)
print(result)  # Output: 8
import random
 
player_name = input("Enter your hero name: ")
 
player_health = 100
enemy_health = 80
 
print(f"\nWelcome, {player_name}!")
print("A wild Goblin appears!")
 
while player_health > 0 and enemy_health > 0:
    print("\n--- Battle Status ---")
    print(f"{player_name} Health: {player_health}")
    print(f"Goblin Health: {enemy_health}")
 
    print("\nChoose an action:")
    print("1. Attack")
    print("2. Heal")
 
    choice = input("Enter 1 or 2: ")
 
    if choice == "1":
        damage = random.randint(10, 25)
        enemy_health -= damage
        print(f"\nYou attacked the Goblin for {damage} damage!")
 
    elif choice == "2":
        heal_amount = random.randint(10, 20)
        player_health += heal_amount
 
        if player_health > 100:
            player_health = 100
 
        print(f"\nYou healed for {heal_amount} health!")
 
    else:
        print("\nInvalid choice. You lost your turn!")
 
    if enemy_health > 0:
        enemy_damage = random.randint(8, 18)
        player_health -= enemy_damage
        print(f"The Goblin attacked you for {enemy_damage} damage!")
 
if player_health <= 0:
    print("\nYou were defeated by the Goblin... How?")
else:
    print("\nYou defeated the Goblin!")
    print(f"Congratulations, {player_name}...  you murder!")
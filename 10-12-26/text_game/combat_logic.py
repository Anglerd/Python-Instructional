import random

def check_combat_end(player, enemy):
    if player.health <= 0 or enemy.health <= 0:
        return True
    return False

def combat_turn(action, player, enemy):
    player.use_defense()
    enemy.use_defense()
    enemy_intent_roll = random.random()
    enemy_defense_chance = 0.4
    #70% = 0.7
    #45% = 0.45
    if action == "defend":
        player.perform_defense()
    else:
        if enemy_intent_roll <= enemy_defense_chance:
            enemy.perform_defense()
        player.perform_attack(enemy)
    if not check_combat_end(player, enemy):
        if enemy_intent_roll > enemy_defense_chance:
            enemy.perform_attack(player)
#There is no block scope in python
game_level = 2
enemies = ["Skeleton", "Zombies", "Aliens"]

def new_enemy_spawn():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]


    print(new_enemy)
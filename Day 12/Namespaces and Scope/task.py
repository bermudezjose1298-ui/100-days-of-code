# Global Scope - This variable can be used all around
enemies = 1
potion_hp_amount = 10

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope - This variables can only be used inside the function they are declared
def drink_potion():
    potion_hp_amount = 5
    print(potion_hp_amount)

drink_potion()
print(potion_hp_amount)

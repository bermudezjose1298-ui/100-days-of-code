print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("Do you wish to take the treasure? Y or N.").lower()
if choice1 == "y":
    choice2 = input("The treasure you have tried to take is too heavy\n"
                    "You can feel something else start climbing your shoulders\n"
                    "Do you want to keep continue grabbing the tresure? Y or N."
                    ).lower()
    if choice2 == "y":
        choice3 = input("As your pockets are full, you stop losing consciousness\n"
                        "Your body stops responding but you as you drop some coins\n"
                        "You get some force back in your body\n"
                        "Do you want to drop the treasure? Y or N."
                        ).lower()
        if choice3 == "y":
            print("You drop the treasure and get out of the place alive! You Win!")
        else:
            print("As your greed consumes you, you become another statue in the treasure room, Game Over")

    else:
        print("You escape with your life, You win!")
else:
    print("You escape with your life, You win!")
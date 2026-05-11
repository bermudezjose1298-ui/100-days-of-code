import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


rock_paper_scissors_logic = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if rock_paper_scissors_logic == 0:
    print(rock)
elif rock_paper_scissors_logic == 1:
    print(paper)
elif rock_paper_scissors_logic == 2:
    print(scissors)
else:
    print("That is not a valid option")

print("Computer chose:\n")

computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(rock)
    if rock_paper_scissors_logic == 1:
        print("You win")
    elif rock_paper_scissors_logic == 0:
        print("You tied")
    else:
        print("You lose")
elif computer_choice == 1:
    print(paper)
    if rock_paper_scissors_logic == 2:
        print("You win")
    elif rock_paper_scissors_logic == 1:
        print("You tied")
    else:
        print("You lose")
elif computer_choice == 2:
    print(scissors)
    if rock_paper_scissors_logic == 0:
        print("You win")
    elif rock_paper_scissors_logic == 2:
        print("You tied")
    else:
        print("You lose")
else:
    print("That is not a valid option")



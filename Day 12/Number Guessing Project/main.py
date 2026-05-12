import art
import random

guess_number = random.randint(1, 100)


def guessing_game():
    print(art.logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty level: easy or hard: ")
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5

    user_guess = 0
    while user_guess != guess_number:
        print(f"You have {lives} lives left, try to guess the number!")
        user_guess = int(input("Make a guess: "))
        if user_guess == guess_number:
            print(f"Correct! the answer was {guess_number}.")
        elif user_guess < guess_number:
            lives -= 1
            print("Your guess is too low.")
        else:
            lives -= 1
            print("Your guess is too high.")
        print("Guess again")

        if lives == 0:
            print("You could not guess the number! You lose!")
            print(f"The number I was thinking of was {guess_number}")

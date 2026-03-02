# Lab 5.3: Enhanced Guessing Game

import random
import math

secret_number = random.randint(1, 100)
max_guesses = 7
guesses_taken = 0
last_guess = None

print("Welcome to the Guessing Game!")

while guesses_taken < max_guesses:
    guess_str = input("Guess a number between 1 and 100 (or type 'hint'): ")

    if guess_str.lower() == "hint":
        if last_guess is None:
            print("Make at least one guess before asking for a hint!")
        else:
            if last_guess < secret_number:
                hints = [
                    "It's higher than your last guess!",
                    "Try increasing your guess.",
                    "The number is in the upper range."
                ]
            else:
                hints = [
                    "It's lower than your last guess!",
                    "Try decreasing your guess.",
                    "The number is in the lower range."
                ]
            print(f"Hint: {random.choice(hints)}")
        guesses_taken += 1
        continue

    try:
        guess = int(guess_str)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    guesses_taken += 1
    last_guess = guess

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {guesses_taken} guesses!")
        break

    if guesses_taken >= 3 and guess != secret_number:
        sqrt_hint = math.floor(math.sqrt(secret_number))
        print(f"Hint: The integer part of the square root is around {sqrt_hint}.")

if last_guess != secret_number:
    print(f"Sorry, you ran out of guesses. The number was {secret_number}.")
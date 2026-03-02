# Number Guessing Game

import random

# Generate Secret Number
secret_number = random.randint(1, 100)

# Initialize Counter
num_guesses = 0

# Start the Loop
while True:
    try:
        # Get Guess
        guess = int(input("Guess the number (1-100): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue  # Ask again without increasing counter

    # Optional range validation
    if guess < 1 or guess > 100:
        print("Please enter a number within the range 1 to 100.")
        continue

    # Increment Counter
    num_guesses += 1

    # Provide Feedback
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {num_guesses} attempts!")
        break  # Exit loop when correct
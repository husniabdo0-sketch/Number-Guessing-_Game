import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess a number from 1 to 100: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
else:
    print("Game Over!")
"This is the number guesser game"


import random
number = random.randint(1, 1000)
attempts = 0
while True:
    guess = input("Enter your guess (or type 'bye' or 'exit' to quit): ")
    if guess == "bye" or guess == "exit":
        break
    if not guess.isdigit():
        print("please enter a valid number")
        continue
    guess = int(guess)
    attempts += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break

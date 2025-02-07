import random
name = input("Hello! What is your name?")
random_num = random.randint(1, 20)
guess = int(input(f"Well, {name}, I am thinking of a number between 1 and 20. \nTake a guess.\n"))
n=1
while True:
    if guess < random_num:
        guess = int(input("Your guess is too low. \nTake a guess\n"))
        n+=1
    elif guess > random_num:
        guess = int(input("Your guess is too high. \nTake a guess\n"))
        n+=1
    else:
        print(f"Good job, {name}! You guessed my number in {n} guesses!")
        break
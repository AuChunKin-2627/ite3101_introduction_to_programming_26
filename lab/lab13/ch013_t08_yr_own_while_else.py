from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
guess = int(input("Your guess:"))
while guesses_left > 0:
    print(random_number)
    if random_number == 5:
        print("You win!")
        break
    guesses_left -= 1
else:
    print("You lose.")

import random

jackpot = random.randint(1,100)

guess = int(input("guess the jackpot number between 1 and 100: "))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("too low! try again.")
    else:
        print("too high! try again.")
    guess = int(input("guess the jackpot number between 1 and 100: "))
    counter += 1
if guess == jackpot:
    print("congratulations! you won the jackpot")
else:    print("sorry! better luck next time. the jackpot number was: ",jackpot)
print("you made", counter, "guesses.")
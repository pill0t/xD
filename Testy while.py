import random
my_number = random.randint(0,20)
guess = -1
trials = 0

print('Guess my number')

while guess != my_number:

    guess = int(input())
    trials +=1

    if guess == my_number:
        print("You're the best! It was", my_number,"You needed", trials, "trials")
    elif guess>my_number:
        print("Sorry, my number is diffrent, it a little bit smaller", guess, "Try again!")
    else:
        print("Sorry, my number is greater than", guess, "Try again!")

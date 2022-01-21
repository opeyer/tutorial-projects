import random

print('----------------------------')
print('   GUESS THAT NUMBER GAME')
print('----------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input('Player, what is your name? ')

print("I am thinking of a number... care to guess?")
print()

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry, {1}, your guess of {0} was too LOW!'.format(guess, name))
    elif guess > the_number:
        print('Sorry, {1}, your guess of {0} was too HIGH!'.format(guess, name))
    else:
        print("You got it! Man, I thought you weren't EVER going to get it!")
        print("Excellent work, {0}!".format(name))

print('Done.')

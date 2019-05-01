from random import *
import time

print('Welcome to The Guessing Game........')
time.sleep(2)
print('Developed by Xyber.......')
time.sleep(2)

e = True

while e == True:
    random_num = randint(1, 101)
    print(random_num)
    guess = int(input('Enter a number between 1 to 100: '))
    no_of_guesses = 0
    while guess != random_num:
        if abs(guess - random_num) < 10:
            print('WARMER')
            guess = int(input('Enter a number between 1 to 100: '))
            no_of_guesses += 1
        else:
            print('COLDER')
            guess = int(input('Enter a number between 1 to 100: '))
            no_of_guesses += 1
    if guess == random_num:
        print('Winner Winner chicken dinner!!!')
        print('You have made {} no of guesses'.format(no_of_guesses+1))
        retry = input('Do you want to play the game again? (y/n) : ')
        if retry == 'y':
            continue
        else:
            print('Thank you for playing!!!')
            e = False

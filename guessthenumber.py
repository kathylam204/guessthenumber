import random

"""def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a random number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
guess(5)
print(f'{random_number} is correct!')"""

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        computer_guess = random.randint(low,high)
        feedback = input(f'Is {computer_guess} too high (h), too low (l), or correct (c)?')
        if feedback == 'h':
            high = computer_guess - 1
        elif feedback == 'l':
            low = computer_guess + 1
print(f'Congrats {computer_guess} is the correct number!')

computer_guess(500)

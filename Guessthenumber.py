import random

def guess(x):
    random_number = random.randint(1, x)

    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess >  random_number:
            print('Sorry, guess agiain. Too high.') 

    print('Yay, congrats. You have guessed the number correctly.')

guess(10)  

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':  # Make sure 'c' is lowercase to match input
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # When low == high, it's the only possible number
        
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! You guessed the number, {guess}, correctly!')

# Correct function call
computer_guess(10)

 


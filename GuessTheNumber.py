import random

def main():
    # Set the upper limit for the range of random numbers
    upper_limit = 25

    # Starting messages
    print('I have picked a random number between 1 and %d.' % upper_limit)
    print('Can you guess it?')

    # Generate random number
    random_number = random.randint(1, upper_limit)

    # Loop until user guesses the random number
    while True:

        # Take input
        guess = input('Guess: ')

        # If user does not enter positive integer
        if not guess.isdigit():
            print('That is not a number. Try again.')

        # If user enters a positive integer
        # Check if guess is correct, too high, too low or out of range
        else:
            guess = int(guess)
            if guess == random_number:
                print('That was it!')
                break
            elif guess > upper_limit:
                print('The number is between 1 and %d.' % upper_limit)
            elif guess == 0:
                print('The number is between 1 and %d.' % upper_limit)
            elif guess > random_number:
                print('Too High')
            else:
                print('Too Low')
    
main()
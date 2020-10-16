# import dependencies
import random 

"""Setting up game"""
# store random number, initialize flag and starter gueess
num = random.randint(1,20)
flag = True
guess = 0
guess_counter = 1

# print starter message
print(f"Guess my number between 1-20 (Guess {guess_counter}): ",end='')

# create while loop with flag to check guess
while flag == True:

    guess = input()
    if not guess.isdigit() or int(guess) > 20 or int(guess) < 0:
        print("Invalid! Enter only digits between 1 and 20")
        break
    elif int(guess) < num:
        guess_counter += 1
        print(f'Too low, try again (Guess {guess_counter}): ', end='')
    elif int(guess) > num:
        guess_counter += 1
        print(f'Too high, try again (Guess {guess_counter}): ', end='')
    else:
        if guess_counter == 1: 
            print('Correct... My number is ' + guess)
            print('You must be a good guesser, you got it on the first try!')
            flag = False
        else: 
            print('Correct... My number is ' + guess, end='')
            print(f"It took you {guess_counter} tries.")
            flag = False
        
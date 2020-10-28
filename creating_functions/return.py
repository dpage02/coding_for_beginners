# initializing input 
num = input('Enter a number: ')

# function that accepts single arugment value to be passed from the caller
def square(num):

    # validate arg value as int OR halt further execution
    if not num.isdigit():
        return 'Invalid Entry'

    # pass argument as integer
    num = int(num)
    return num*num

print(f'{num} Squared Is: {square(num)}')
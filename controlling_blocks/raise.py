# store initial value
day = 32

# try statement to test day's value
try:
    if day > 31:
        raise ValueError('Invalid Day Number')

# except statement to display error message when ValueError occurs
except ValueError as msg:
    print('The Program found An', msg)

# finally statement 
finally: 
    print('But Today is Beautiful Day')
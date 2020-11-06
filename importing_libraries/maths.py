# import dependencies
import math, random

# display 2 rounded values
print('Rounded up 9.5:', math.ceil(9.5))
print('Rounded down 9.5:', math.floor(9.5))

# initialize var 
num = 4

# dispaly square/square root of bar
print(num, 'Squared:', math.pow(num,2))
print(num, 'Square Root:', math.sqrt(num))

# produce random list of six unique numbers between 1-49
nums = random.sample(range(1,49),6)

# display random list
print('Your Lucky Numbers Are:', nums)
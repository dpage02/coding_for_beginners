# import module 
from dog import *

# have user eneter pet name to overwrite default values 
pet = input('Enter a Pet Name: ')

# call each function with user arguement 
bark(pet)
lick(pet)
nap(pet)
# import module
import cat

# request user to enter a name to overwrite default value
pet = input('Enter A Pet Name: ')

# call functions, passing defined pet value as the arguement 
cat.purr(pet)
cat.lick(pet)
cat.nap(pet)
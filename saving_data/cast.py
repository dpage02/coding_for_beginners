# get user input for 2 numbers 
num1 = input("Please enter a whole number: ")
num2 = input("Please enter another whole number: ")

# showing the type of input the user input (str)
print('Input is: ', type(num1), type(num2))

# adding strings together (will simply put them togeather)
total = num1 + num2
print('Total: ', total, type(total))

# casting input to integers before adding numbers
total = int(num1) + int(num2)
print('Total: ', total, type(total))

# casting inputs to floats before adding numbers
total = float(num1) + float(num2)
print('Total: ', str(total), type(total))
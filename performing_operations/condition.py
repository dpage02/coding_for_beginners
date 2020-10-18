# inital values
a = 1
b = 2 

# conditional evals- describing first variable's value
print('\nVariable a is :', ' One' if (a ==1) else 'Not One')
print('Variable a is :', 'Even' if (a % 2 == 0) else 'Odd')

# conditional evaluatio describing the second variable's values
print('\nVariable b is :', 'One' if (b == 1) else 'Not One')
print('Variable b is :', 'Even' if (b % 2 == 0) else 'Odd')

# adding a statement to asign the result of a conditional evaluation to a new variable
top = a if (a > b) else b

# statement to siplay the assigned result- indentifying the greater of the two variables
print('\nGreater Value is:', top)
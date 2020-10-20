# initialize list, tuple, dict
chars = ['A','B','C']
fruit = ('Apple', 'Banana', 'Cherry')
info = {'name':'Mike','ref':'Python','sys':'Win'}

# display all list element values
print('Elements: \t', end='')
for item in chars:
    print(item, end='')

# display list element values and their relative index number
print('\nEnumerated:\t', end='')
for item in enumerate(chars):
    print(item, end='')

# display all list and tuple elements 
print('\nZipped: \t', end='')
for item in zip(chars,fruit):
    print(item, end='')

# display all dictionary key names and associated element values
print('\nPaired:')
for key, value in info.items():
    print(f"{key} = {value}")
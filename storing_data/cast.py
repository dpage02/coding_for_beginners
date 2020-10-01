# getting numbers
num1 = input('Please enter a whole number: ')
num2 = input("Now enter another whole number: ")

# looking at initial types
print("Input type is:", type(num1), type(num2))

# totaling - will get error (not correct types)
# total = num1 + num2
# print(f'Total: {total}, {type(total)}')

# changing to int and then adding
total = int(num1) + int(num2)
print(f'Total: {total}, {type(total)}')

# changing total to float, printing as a string
total = float(num1) + float(num2)
print(f"Total: {str(total)} {type(total)}")
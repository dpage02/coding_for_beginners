# setting initial values
a = 2
b = 4
c = 8

# finding default order and trying to force an order
print('\nDefault Order :\t', a, '*', c,'+',b,'=',a*c+b)
print(f'Forced Order :\t {a} * ({c}+{b}) = {a*(c+b)}')

# adding statements to display the results of default precendence and forcing subtraction
print(f"\nDefault Order :\t {c} // {b} - {a} = {c // b - a}")
print(f"Forced Order :\t {c} // ({b} = {a}) = {c // (b - a)}")

# exponent and remainder operation 
print(f"\nDefault Order :\t{c} % {a} + {b} = { c % a + b}")
print(f"Forced Order :\t{c} % ({a} + {b}) = {c % (a + b)}")
print(f'\nDefault Order: \t{c} ** {a} + {b} = {c ** a + b}')
print(f'Default Order: \t{c} ** ({a} + {b}) = {c ** (a + b)}')
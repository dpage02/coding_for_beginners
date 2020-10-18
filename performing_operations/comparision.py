# set initial values
nil = 0
num = 0
top = 1
cap = 'A'
low = 'a'

# results of numeric and character equality comparisons
print('Equality : \t', nil, '==', num, nil==num)
print(f'Equality :\t {cap} == {low} {cap==low}')

# adding statement to display the result of inequality comparison 
print('Inequality : \t', nil, '!=', top, nil != top)

# statements to diplay results of greater and less comparison
print('Greater: \t', nil, '>', top, nil > top)
print('Lesser: \t', nil, '<', top, nil < top)

# statements to display the results of greater or equal and lesser or equal comparisons 
print('More or Equal : \t', nil, '>=', num, nil >= num)
print('Less or Equal : \t', top, '<=', num, top < num)

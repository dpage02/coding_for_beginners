# creating def 
def echo(user, lang, sys):
    print(f'User: {user}. Language: {lang}. Platform: {sys}')

# call function with first set of arguements
echo('Mike','Python','Windows')

# cal function passing string arguments to the function parameters by specifying parameter names
echo(lang='Python', sys='Mac OS', user='Anne')

# seperate function with default values that will print out parameter values
def mirror(user='Carole', lang='Python'):
    print('\nUser:',user,'Language:',lang)

mirror()
mirror(lang='Java')
mirror(user="Tony")
mirror('Susan', 'C++')
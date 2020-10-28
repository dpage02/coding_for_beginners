# storing global variable
global_var = 1

# function to display value contained within the global variable
def my_vars():
    print("Global Variable:", global_var)

    # initialize a local variable and print
    local_var = 2
    print('Local Variable:', local_var)

    # coearced gloabl variable 
    global inner_var
    inner_var = 3

# call func
my_vars()

# display coerced global var
print(f'Coerced Global: {inner_var}')
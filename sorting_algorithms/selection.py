# function to recieve a list, loop through to store each element's value and current index number
def selection_sort(array):

    for index in range(0, len(array)-1):
        value = array[index]
        current = index

        # algorithm
        for element in range(index+1, len(array)):
            if array[element] < array[current]:
                current = element
        array[index] = array[current]
        array[current] = value

        print(f'\tResolving element[{index}] to {array}')

# creating and displaying unsorted list
array = [5,3,1,2,6,4]
print("Selection Sort...\nArray:", array)

selection_sort(array)
print(f'Array: {array}')
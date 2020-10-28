# function to recieve a list, loop through to store each element's value and current index number
def bubble_sort(array):

    for index in range(len(array)):

        for element in range((len(array)-1)-index):
            if array[element] > array[element+1]:
                array[element], array[element+1] =  array[element+1], array[element]

                print(f'\tResolving elemenet[{element}] to {array}')

# creating and displaying unsorted list
array = [5,3,1,2,6,4]
print(f'Bubble Sort...\nArray: {array}')

bubble_sort(array)
print('Array:',array)
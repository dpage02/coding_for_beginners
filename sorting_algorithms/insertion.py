# def to recieve list and loop through list 
def insertion_sort(array):

    for index in range(1, len(array)):
        value = array[index]

        while array[index-1] > value and index >= 1:
            array[index] = array[index-1]
            index -= 1
            array[index] = value

        print(f'\tResolivng element[{index}] to {array}')

# creating and displaying unsorted list
array = [5,3,1,2,6,4]
print('Insertion Sort...\nArray', array)

insertion_sort(array)
print('Array:', array)
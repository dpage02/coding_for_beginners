# funtion to recieve a list reference as input and return sorted copy as output
def copy_sort(array):
    copy = array[:]
    sorted_copy = []

    # algorithm sequence
    while len(copy) > 0:
        minimum = 0
        for element in range(0, len(copy)):
            if copy[element] < copy[minimum]:
                minimum = element
        print('\tRemoving value', copy[minimum], \
            'from', copy)
        sorted_copy.append(copy.pop(minimum))

    return sorted_copy


# creating and displaying unsorted list
array = [5,3,1,2,6,4]
print('Copy Sort...\nArray :', array)

# dispaly unsorted list and sorted copy
print('Copy:', copy_sort(array))
print('Original Array:', array)
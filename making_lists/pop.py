# setting initial lists
basket = ['Apple', 'Bun', 'Cola']
crate = ['Egg', 'Fig', 'Grape']

# display the contents of basket and length
print(f'Basket List: {basket}')
print(f'Basket Elements: {len(basket)}')

# add an element/display al list elements
# remove final element and display
basket.append('Damson')
print('Append:', basket)
print('Last Item Removed', basket.pop())
print('Basket List:', basket)

# add all elements of the second list to first list, dispaly
basket.extend(crate)
print('Extended:',basket)
del basket[1]
print('Item Removed:', basket)
del basket[1:3]
print('Slice Removed:', basket)
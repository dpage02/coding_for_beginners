# storing data
info = {'name':"Bob", "ref": 'Python', 'sys':'Win'}
print("info:", type(info))
print('Dictionary:', info)

# displaying a single value referenced by its key
print('\nReference:', info['ref'])

# displaying all keys within the dictionary 
print('\nKeys:', info.keys())


# deleting one pair from dict, add replacement pair 
del info['name']
info['user'] = 'Tom'
print('\nDictionary:', info)

# search the dictionary for a specific key
print('\nIs there a name key?:', 'name' in info)

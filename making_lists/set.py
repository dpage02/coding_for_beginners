# initialize set
party_goers = {'Andrew', 'Barbara', 'Carole', 'David'}
print('party_goers:', type(party_goers))

# search set elements fo two specified values
print('Did David go the party?' 'David' in party_goers)
print('Did Kelly go the party?' 'Kelly' in party_goers)

# initialize another set
students = {'Andrew', 'Kelly', 'Lynn', 'David'}

# create another set of common values from both lists
commons = party_goers.intersection(students)

# regular list of the common values 
# done so elements values can be individually accessed
party_students = list(commons)

# dispaly all comman values and value stored in first regular element 
print(f'Students at the part {party_students}')
print(f'First student at the party: {party_students[0]}')
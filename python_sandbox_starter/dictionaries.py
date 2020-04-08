# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'Crystal',
    'last_name': 'April',
    'age': 21
}

print(person, type(person))

# Use Constructor
person2 = dict(first_name = 'MarKata',last_name = 'Rhaimes')
print(person2, type(person2))

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '333-333-3333'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['City'] = 'Mumbai'
print(person2)

# Remove item
del(person['age']) #OR
person.pop('phone')

# Clear dict
person.clear()

# Get length
print(len(person2))
print(person)

# List of dict (This could be looked as an array of Dictionaries)
people = [
    {'name':'Claire', 'age':21},
    {'name':'Mark', 'age': 26}
]
print(people)
print(people[1]['name'])
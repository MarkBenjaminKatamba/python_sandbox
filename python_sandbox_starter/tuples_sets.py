# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))   #Not recommended still

#One thing to remember with tuples is that if you only have one value, you need to leave a trailing comma, e.g below
fruits2 = ('Apples',)
# print(fruits2, type(fruits2))

# Get value (same with lists)
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# print(fruits2)

# Get length
print(len(fruits))



# A Set is a collection which is unordered and unindexed. No duplicate members.
# [Note that a set is created with curly braces]
# So when you're programming you have to decide when to use what (list, tuple or set)

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set 
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')
print(fruits_set)

# Add duplicate
fruits_set.add('Apples')
print(fruits_set)           # Here, you won't get any error returned, it just won't add 'Apples' twice

# Remove from set
fruits_set.remove('Grape')
print(fruits_set)

# Clear set/Make it empty
fruits_set.clear()
print(fruits_set)

#Delete set (Wiping it out completely/Making it undefined)
del fruits_set
print(fruits_set)
# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]           # Most common way of creating lists
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
#numbers2 = list((1,2,3,4,5))
#print(numbers, numbers2)

# Get a single value from a list
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangoes')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Sort list (alphabetically)
fruits.sort()

# Reverse sort
fruits.reverse()
# OR
fruits.sort(reverse=True)

print(fruits)




# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Crystal'
age = 21

#Concatenate (basically means to insert a variable into a string)
#print ('Hello, my name is ' + name + ' and I am ' + str(age))


# String Formatting
#Arguments by position/Positional arguments
#print('My name is {name} and I am {age}'.format(name=name, age=age))

#Using F-stirngs (these are only available in Python 3.6+)
#print(f'Hello, my name is {name} and I am {age}')


# String Methods
s = 'hello world'

#Capitalize
print(s.capitalize())       #Capitalizes the first letter of the string

# Make all uppercase
print(s.upper())

# Make all lowercase
print(s.lower())

# Swap case
print(s.swapcase())

# Get lenght (gets the length of the string)
print(len(s)) 

# Replace
print(s.replace('world', 'Claire'))

# Count
#print(s.count('h'))
sub = 'h'
print(s.count(sub))

#Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find Position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1               # int
# y = 2.5             # float
# name = 'Claire'     # str
# is_cool = True      # bool

#Multiple assignment
x, y, name, is_cool = (1, 2.5, 'Claire', True)      #Same as above implementation, just that this is more compact.

#Basic math
a = x + y

#Casting (Here, we're able to change the type of an integer value)

x = str(x)          #Changoing the type of x from 'int' to 'string'
y = int(y)          #Changoing the type of y from 'float' to 'int' so it'll print out as 2 instead of 2.5
z = float(y)        #Changoing the type of x from 'int' back to 'float', so now it'll print out as 2.0

#print (x, y, name, is_cool, a)
print (type(y), y)

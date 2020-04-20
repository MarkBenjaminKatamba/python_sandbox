# Python has functions for creating, reading, updating, and deleting files.

# Open file
myFile = open('myfile.txt','w')

# Get some info about the file
print('Name: ', myFile.name)  # myFile is actually an object that has properties that we can access
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and VUE-JS')
myFile.close

# Append to file
myFile = open('myfile.txt','a')
myFile.write(', and I also love cars')

# Read from file
myFile = open('myfile.txt','r+')
text = myFile.read(100)
print(text)
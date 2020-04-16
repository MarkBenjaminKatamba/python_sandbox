# A function is a block of code which only runs when it is called. In Python, 
# we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello(name):
        print('Hello ' + name + '!')

#sayHello('Crystal April')


# Return Vlaues (Commonest use of functions, coz for the most part of 
# it you'll never simply print out stuff like you just did above)
def getSum(num1, num2):
        total = num1 + num2
        return total

# num = getSum(4.2, 7)
# print(num)
# print(getSum(3.5, 5))



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, # but can only have one expression. 
# Very similar to JS arrow functions
getSum = lambda num1, num2 : num1 + num2   #So here, the colon acts like the arrow in an arrow finction. "num1 + num2" is the body of the function, and it's going to implicitly return whatever the "num1 + num2" expression equals and it's going to put it in the getSum variable.
print(getSum(12, 18))
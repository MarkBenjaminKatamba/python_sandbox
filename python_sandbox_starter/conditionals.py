# If/ Else conditions are used to decide to do something based on something being true or false
c = 16
d = 16.4

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
# if c > d:
#     print(f'{c} is greater than {d}')

# If/else
# if c > d:
#     print(f'{c} is greater than {d}')
# else:
#     print(f'{d} is greater than {c}')

# elif
# if c > d:
#     print(f'{c} is greater than {d}')
# elif c==d:
#     print(f'{c} is equal to {d}') 
# else:
#     print(f'{d} is greater than {c}')

# Nested if  (Not always recommended; better to use logcal operators)
# if c > 2:
#     if c <= 10:
#         print(f'{c} is greater than 2 and less than or equal to 10')



# Logical operators (and, or, not) - Used to combine conditional statements

# # and (here, both conditions have to be true)
# if c > 2 and c <= 10:
#     print(f'{c} is greater than 2 and less than or equal to 10')
    

# # or (here, either one or the other of the conditions should be true)
# if c > 2 or c <= 10:
#     print(f'{c} is greater than 2 or less than or equal to 10')

# # not
# if not(c == d):
#     print(f'{c} is not equal to {d}')




# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5,6,7,8,9]

# #  in
# if c in numbers:
#     print(c in numbers) # This will just give us a true of false

# #  not in
# if c not in numbers:
#     print(c not in numbers)



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# # is
# if c is d:
#     print(c is d)

# # is not
# if c is not d:
#     print(c is not d)
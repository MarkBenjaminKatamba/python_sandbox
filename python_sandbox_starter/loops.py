# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# Simple for loop
people = ['Mark','Benjamin','Claire','Joanita']

# for person in people:
#     print(f'Current person is {person}')

# # Break
# for person in people:
#     if person == 'Claire':
#         break
#     print(f'Current person is {person}')


# # Continue
# for person in people:
#     if person == 'Claire':
#         continue
#     print(f'Current person is {person}')


# # range  (This one's similar to a simple for loop)
# for i in range(len(people)):
#     print(people[i])


# for i in range(0, 11):
#     print(f'Number: {i}')


# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1
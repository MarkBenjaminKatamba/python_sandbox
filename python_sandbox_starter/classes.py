# A class is like a blueprint for creating objects. An object has properties and methods(functions) 
# associated with it. Almost everything in Python is an object

# Create Class
class User:
    
    # Constructor (This is basically a function that runs when you instantiate an object from a class)
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # Creating a method with the class
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}' # Whenever we need to access any of the above properties from any method within the class, we need to use the `self` keyword

    def has_birthday(self):
        self.age += 1     # This simply adds an extra year to the 'age' property

# Init user object
kata = User('Katamba Mark Benjamin','kata@gmail.com','33')
# # Accessing the properties of the object
# print(kata.name)
# print(kata.email)
# print(kata.age)

kata.has_birthday()
print(kata.greeting())

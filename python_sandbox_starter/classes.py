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

# Extend class
class Customer(User):                   # Makes 'Customer' a child class for the 'User' class
    # Constructor 
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
            return f'My name is {self.name} and I am {self.age}, and my balance is {self.balance}'

# Init user object
kata = User('Katamba Mark Benjamin','kata@gmail.com', 25)
# # Accessing the properties of the object
# print(kata.name)
# print(kata.email)
# print(kata.age)

# Init customer object
claire = Customer('Claure Joanita', 'claire@rmail.com', 21)

claire.set_balance(500)
print(claire.greeting())       # Notice here that claire can still call 'greeting' even though it's not defined in the 'Customer' class.

kata.has_birthday()
print(kata.greeting())


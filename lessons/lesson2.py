# My Application Overview Lesson

# This function should be lowercase and if more than one word it
# should have an underscore to separate each word. You Should have
# a parenthesis after the name followed by a colon. Statements that are
# part of the function should be 4 spaces indented.
def my_function():
    print('Hello')
    print('World')


# To run the function, you must call it by name.
my_function()


# When defining a function with arguments, those arguments go in between
# the parenthesis and separated by commas.
def my_other(arg1, arg2):
    print(arg1)
    print(arg2)


my_other('red', 'green')

# Variable Names
# - must start with a letter or an underscore
# - Can not begin with a number
# - Can only contain alpha-numeric characters and underscores
# - Are case sensitive.

# The variables are on the left while the literal value is on the right
# Value & Value2 are variables
# blue and 10 literals
# combined they are a field
value = 'Blue'
value2 = '10'
print(value)
print(value2)

# Variables can even change types, although you may want to avoid this
value3 = "happy"
print(value3)
value3 = 20
print(value3)

# Multi-line statements use a backslash to continue a statement on a second line.
alpha = 1 + 2 + 3 \
    + 4 + 5
print(alpha)

# More than one variable on the same line
beta = 10; charlie = "python"; delta = 5

up, down, left = "town", "stairs", "right"
print(up)
print(down)
print(left)



# A class is an object, which is a blueprint. An instantiation of an object
# allows for all fields and functions to be accessed within. Like function
# outside the class, you need to provide 2 empty spaces before its defined.
# Basic class example
class MyFirstClass:
    name = 'Nick'

# This is a method instead a function
    def something(self):
        print('something')


my_class = MyFirstClass()
print(my_class.name)
my_class.something()



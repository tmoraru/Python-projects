"""
Variables are containers for storing data values.

Unlike other programming languages, Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
"""

x = 5
y = "John"
print(x)
print(y) 

#Variables do not need to be declared with any particular type and can even change type after they have been set.

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

#String variables can be declared either by using single or double quotes:

x = "mimi"
# is the same as
y = 'brrrr'

print(x)
print(y)


"""
Variable Names

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

"""

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
"""
Assign Value to Multiple Variables
Python allows you to assign values to multiple variables in one line:
"""

x, d, q = "Mia", "Josi", "Frederico"

print(x)
print(d)
print(q)

# And you can assign the same value to multiple variables in one line:

x = d = q = "Mia"

print(x)
print(d)
print(q)


"""
Output Variables
The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character:

"""

x = "awesome"

print(" Ptyhon is " + x)

#You can also use the + character to add a variable to another variable:

x = " awesome "
m = " and "
z = " easy "
q = x + m + z

print(" Python is "+ q)


#For numbers, the + character works as a mathematical operator:

x = 6
y = 6

print(x + y)

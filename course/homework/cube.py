# Enter a number, must be multiplied by itself
def cube ():
    number_1 = float (input (" Enter a number: "))
    a = ((number_1 * number_1) * number_1)
    return a
b = cube ()
# Number from the argument number, must be  is divisible by 3, by_three should call cube(number) and return its result.
# In other case will second function should return False.
def by_three():
    number_2 = float (input ("Enter second number: "))
    if (number_2 % 3) == True:
        print(b)
    else:
        print(False)
by_three()

# Context:
#You were recently hired by a start up company "Relativity" as DevOps Engineer.
#Your team has 3 members
#You'r first assigned task:
#Write a Python script that sets the following variables:

#first_name - Set to your first name

#last_name - Set to your last name

#age - Set to your age as an integer

#birth_date - Set to your birthdate as a string

#for more advanced exercise, set vars by getting the user input
#for even more advanced exercise, age variable should be the result of current year - year you were born.
#for even more advanced execise, use the appropriate method to capitalize you last and first name.
#Using the variables, print the following to the screen when you run the script:

# First example
first_name = input(" Please write   your first name: ")
last_name = input ( " Please write your last name: ")
birth_date = input( " Write your mm/dd/yyyy:" )
age = input ("How old are you:")

print("My name is " + first_name + " " + last_name)
print(" I was born on " +  birth_date +  " " + " , and I am " + age + " years old" ) 



# second example

first_name = input(" Please write   your first name: ")
last_name = input ( " Please write your last name: ")
birth_date = input( " Write your mm/dd:" )
birth_year = input(" Write your yyyy:")
age = 2020 - int(birth_year)

print("My name is " + first_name.capitalize() + " " + last_name.capitalize())
print(" I was born on",  birth_date, birth_year, " , and I am " , age , " years old" ) 

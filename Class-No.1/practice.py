
#* First Example in Python Language

# print("Hello world") #* Hello world

#? Complete python introduction
pythonIntroduction = """
What is Python:
Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

web development (server-side),
software development,
mathematics,
system scripting.
"""

#? Python Indentation

#* Example 1

# if 5 > 2:
# print("5 is greater than 2") #* it'll give you indentation error 

#* correct syntax is to indent the print function 
#* The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

# if 5 < 2:
#     print("5 is greater than 2") #* R = 5 is greater than 2
# else:
#     print("No!")    


#* You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

# if 10 < 11:
#     print("10 is les than 11")
#      print("11 is greater than 10")  #* so here the the in second print function have one more space than first 

#? COMMENTS IN PYTHON HAVE NO SPECIFIC SYNTAX

"""
  you can comments in python with two ways 
  1) #
  2) """ """ using for long descriptive comments way mostly using in AI, Machine leaning etc , 
 
  i can also print this current comment in which i'm working
"""

#? CREATING VARIABLES IN PYTHON
#* In Python, variables are created when you assign a value to it:

#* Example

# x = 10
# y = "Muhammad Usman"

# print(x) #* 10 (integer)
# print(y) #* Name (string)

#* you can specify

# x = str("hello") #* it will print string "hello"
# y = int(4)   #* it will print integer 4
# z = float(3)  #* it will print float value 3.0

# print(x, y, z) #* it will print "hello 4 3.0"

#? Get the Type
#* You can get the data type of a variable with the type() function.


# print(type(x))        #* it'll show you what type of data is this like here it'll showing you "integer" (10)

#! Note: variables can be declare either with double QUOTES OR SINGLE QUOTES and variables are case sensitive

#* Example

# a = 10
# A = 20  

#*   A variable will not overwrite on (small) a variable because Large A is not same as small a

#* Example No.2

a = 13
a = 12
print(a) #* now  second a will overWrite on first because now they're same Result = 12


#? Variable Names

#! Note:

#*  A variable name must start with a letter or the underscore character
#*  A variable name cannot start with a number
#*  A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#*  Variable names are case-sensitive (age, Age and AGE are three different variables)
#*  A variable name cannot be any of the Python keywords.

#* Example (Legal)
myvar = "Muhammad Usman"
my_var = "Muhammad Usman"
_my_var = "Muhammad Usman"
myVar = "Muhammad Usman"
MYVAR = "Muhammad Usman"
myvar2 = "Muhammad Usman"

#* But the most efficient is two way

#* Example with these two ways the error chances would less

my_var = "Muhammad Usman"
myVar = "Muhammad Usman"


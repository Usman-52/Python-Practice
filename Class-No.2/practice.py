
#? Global Variables
#* Variables that are created outside of a function are known as global variables.
#* Global variables can be used by everyone, both inside of functions and outside.

# my_first_name = "Muhammad"
# my_last_name = "Usman"

# def myName():
#     print(my_first_name, my_last_name)

# myName()

#* If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
#* The global variable with the same name will remain as it was, global and with the original value.

# x = 20
# def addition():
#     x = 30
#     print(x)

# addition()
# print(x)

#? The global Keyword
#* Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#* To create a global variable inside a function, you can use the "global" keyword.


# def habit():
#     global good_habit, A10
#     good_habit = "Praying 5 time prayer on time"
#     A10 = 20

# habit()
# print(good_habit)

#* Also, use the "global" keyword if you want to change a global variable inside a function.
#* refer to global variable through "global" keyword if you wanna change that variable inside the function
#! Note: if once wherever you changed the global variable value it would change everywhere wether you changed inside function

# x = 30 + 30

# def subtraction():
#     global x
#     x = 30 - 20
#     print(x)

# subtraction()
# print(x) #* 10 because we change the x value inside the function
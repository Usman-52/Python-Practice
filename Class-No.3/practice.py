#
#? BUILT-IN DATA TYPES:
#* In programming, data type is an important concept.
#* Variables can store data of different types, and different types can do different things.
#* Python has the following data types built-in by default, in these categories:

#* Mapping Type:	dict
#* Set Types:	set, frozenset
#* Boolean Type:	bool
#* Binary Types:	bytes, bytearray, memoryview
#* None Type:	NoneType

#* Text Type: "str"
# name = "Muhammad Usman"
# print(type(name)) #* String.

#* Numeric Types:	int, float, complex
# x = 10
# print(type(x)) #* Int
# y = 10.4
# print(type(y)) #* float

#! Note complex data types are used to represent complex numbers. A complex number consists of two parts:
#* A real part (a float)
#* An imaginary part (also a float)
#? syntax
#* complex_number = real_part + imaginary_part * 1j

# z = 3 + 1j
# print(type(z)) #* complex
# print(z.real)
# print(z.imag)

#? Sequence Types:	list, tuple, range
#* range

#* In Python, range() is a built-in function that generates a sequence of numbers, often used in loops. 
#* It doesn't return a list but rather a special range object that generates numbers on demand, which makes it memory-efficient.
#? syntax
#* range(start, stop, step)

#? Parameters:
#* start (optional): The starting number of the sequence. By default, it starts at 0.
#* stop: The number at which the sequence ends (but this number is not included in the sequence).
#* step (optional): The difference between each number in the sequence. By default, the step is 1.

#? Example:
# for i in range(5):      #* Basic usage with one argument (stop)
#     print(i)            #* it would generate numbers from 0-4


# for i in range(1, 10):      #* Basic usage with one argument (start) = 1 and (stop) 10
#     print(i)            #* it would generate numbers from 1-9


# for i in range(1, 30, 7):      #* Basic usage with one argument start = 1 , stop = 30 and difference = 3
#     print(i)            #* it would generate numbers from 0-30 with difference 3






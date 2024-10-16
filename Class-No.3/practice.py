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

#! range

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

#! LIST

#* In Python, a list is a built-in data structure used to store a collection of items.
#* Lists are ordered, mutable (modifiable), and can contain elements of different data types.
#? Key Features of Lists:
#* Ordered: The elements have a defined order, and this order will not change unless explicitly changed.
#* Mutable: Elements can be added, removed, or modified after the list is created.
#* Heterogeneous: Lists can contain elements of different data types, such as integers, strings, and floats.

#? Example 
# my_list_of_items = ["Banana", 3, 2+3, "mango", "orange", 4.3]
# print(my_list_of_items)

fruit_list = ["🍌", "🥭", "🍇", "🍈", "🍉", "🍊", "🍋"]
print(fruit_list)

#? Accessing Elements: Lists are zero-indexed, so you can access individual elements using their index.

# print(fruit_list[2])     #* 🍇
# print(fruit_list[-1])   #* it can be accessing "🍋" because -1 means that the indexing would be starting from back side of the list

#? Modifying Elements:

# fruit_list[3] = "🍎" #* it will replace 🍎 on index 3 (🍈)
# print(fruit_list)

#? Slicing Lists: You can extract a portion of a list using slicing.

# sliced_Elements = fruit_list[2:6] #* this will sliced the elements from index 2 to index 6 but index 6 (🍋) will be  exclude (always exclude last element)
# print(sliced_Elements)            #* it will print = ['🍇', '🍈', '🍉', '🍊']

#? Adding Elements:
#* Append: append is an method which can Adds an item to the end of the list

# fruit_list.append("🍊")        #* 🍊 will be adding it the end of the list
# print(fruit_list)                 #* it'll print = ['🍌', '🥭', '🍇', '🍈', '🍉', '🍊', '🍋', '🍊']

# ? Insert: insert() is a method which can Inserts an item at a specific position.

# fruit_list.insert(2, "🍎") #* here the 🍎 will come into index 2 position and the 🍇 will move to index 3 ....
# print(fruit_list) 

#* Before: ["🍌", "🥭", "🍇", "🍈", "🍉", "🍊", "🍋"]
#* After:  ['🍌', '🥭', '🍎', '🍇', '🍈', '🍉', '🍊', '🍋']

#? Removing Elements:
#*Remove: Removes the first occurrence of the item

# fruit_list.remove("🍇") #* it will remove 🍇 from the list , same you can remove elements by directly targeting them
# print(fruit_list)

#* Before: ['🍌', '🥭', '🍇', '🍈', '🍉', '🍊', '🍋']
#* After:  ['🍌', '🥭', '🍈', '🍉', '🍊', '🍋']

#? Pop: Removes and returns the item at the specified index (default is the last item)

# fruit_list.pop() #* it will remove the last element of the list(🍋)
# print(fruit_list)

#* Before: ['🍌', '🥭', '🍇', '🍈', '🍉', '🍊', '🍋']
#* After:  ['🍌', '🥭', '🍇', '🍈', '🍉', '🍊']


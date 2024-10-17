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

# fruit_list = ["🍌", "🥭", "🍇", "🍈", "🍉", "🍊", "🍋"]
# print(fruit_list)

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

#?============================ Remove Method ============================#

#* Removing Elements:
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

#?========================== Extend Method =============================#

#* The extend() method in Python is used to add all elements from one iterable (like a list, tuple, or string) to the end of an existing list. 
#* This method modifies the original list in place by appending each item from the iterable.

# fruit_list.extend(["🍏", "🍎"]) #* it will extend the fruit list and add 🍏 and 🍎 at the end of the list
# print(fruit_list) 

#? OR
#? Example 1: Extending a List with Another List
list1 = [1, 2, 3]
list2 = [4, 5, 6, 2, 8, 2, 0, 2,]

# list1.extend(list2) #* it'll merge (combine) list2 into list1 
# print(list1)        #* [1, 2, 3, 4, 5, 6]

#?================ reverse(), count() ,index() ========================#


#* sort():

# list1.sort(reverse=False) #* reverse = False means that the list is in Ascending order, if it's True then its means it's in descending order
# print(list1)

# list10 = [100, 50, 65, 82, 23]
# list10.sort()
# print(list10)

#*======================== reverse(): ==========================*#

# list2.reverse() #* The method reverse just reverse the elements in the list not sorting
# print(list2)

#*============================ count(): =========================*#

#* The count() method in Python is used to count how many times a specific element appears in a list. 
#* However, it requires one argument, which is the element you want to count.

# tows_in_list2 =list2.count(2) #* it'll count twos (2) in the list
# print(tows_in_list2)  #* 3


#*========================== index() =============================*#

# index_of_10 = list2.index(10)
# print(index_of_10)

#!================================ Key Points: ================================#

#* sort(): Sorts the list in ascending (or descending) order.
#* reverse(): Reverses the order of the elements in the list.
#* count(): Returns how many times a specific element appears in the list.
#* index(): Returns the position of the first occurrence of a specific element.



#?====================================== Loop List ===============================#
#? Loop Through a List
#* Print all items in the list, one by one:

fruit_list2 = ["banana", "mango", "kiwi", "orange", "apple"]
# for i in fruit_list2:
#     print(i)
    
#* OR
# i = 0
# while i < len(fruit_list2):
#     print(fruit_list2[i])
#     i = i + 1

#?=================================== Copy list ==================================#

#* there are 3 ways to copy list:

#?================================ copy() method ==============================#
#* using copy() (method) you can easily copy any list

# fruit_list3 = fruit_list2.copy()
# print(fruit_list3)

#?============================ list constructor method ============================#

# fruit_list4 = list(fruit_list2)
# print(fruit_list4)

#?==================================slice method ===================================#

# fruit_list5 = fruit_list2[:]
# print(fruit_list5)

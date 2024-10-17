
#?=========================================== TUPLE =================================================#
#* Tuple is the built-in data structure which can store ordered , immutable and heterogenous data 
#* Key points:
#* Ordered: the data would be in sequence
#* Immutable: you can't change, modify the data after creating the tuple.
#* Heterogenous: means the tuple items (elements) can be string, float, boolean value, emojis etc

# hetero_tuple = ("abc", 1, 2.3, True)
# print(hetero_tuple)

# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)

#* Tuple Items:
#* Tuple items are ordered, unchangeable, and allow duplicate values.
#* Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#* Ordered:
#* When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#* Unchangeable:
#* Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


#* Allow Duplicates:
#* Since tuples are indexed, they can have items with the same value.
# emojis_tuple = ("😊", "😂", "🤣", "👌", "👌", "😒")
# print(emojis_tuple)

#?============================ Tuple Length using len() method ================================#
#* To determine how many items a tuple has, use the len() function:

# emojis_tuple = ("😊", "😂", "🤣", "👌", "👌", "😒")
# number_of_elements = len(emojis_tuple)
# print(number_of_elements) #* 6

#?============================== check type using type() method ==============================#
# emojis_tuple = ("😊", "😂", "🤣", "👌", "👌", "😒")
# print(type(emojis_tuple)) #* <class 'tuple'>

#?======================= Access specific Tuple Items using indexing =========================#
#* You can access tuple items by referring to the index number, inside square brackets:
# emojis_tuple = ("😊", "😂", "🤣", "👌", "👌", "😒")
# print(emojis_tuple[4]) #* 👌
# print(emojis_tuple[2]) #* 🤣

#?===================================== Negative Indexing ================================#
#* Negative indexing means start from the end.

# emojis_tuple = ("😊", "😂", "🤣", "😍", "👌", "😒")
# print(emojis_tuple[-3])           #* counting will start from end of the tuple , result = 😍

#?=================================== Range of Indexes ==================================#
#* You can specify a range of indexes by specifying where to start and where to end the range.
#* When specifying a range, the return value will be a new tuple with the specified items.

# list_of_fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(list_of_fruits[2:5]) #* ('cherry', 'orange', 'kiwi')

#? By leaving out the start value, the range will start at the first item:

#*=============================== Example =======================================#
#* This example returns the items from the beginning to, but NOT included, "kiwi":
list_of_fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(list_of_fruits[:4]) #* ('apple', 'banana', 'cherry', 'orange')

#? By leaving out the end value, the range will go on to the end of the tuple:
#* This example returns the items from "cherry" and to the end:

list_of_fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(list_of_fruits[2:]) #* ('cherry', 'orange', 'kiwi', 'melon', 'mango')

#?============================ Range of Negative Indexes =======================#
#* Specify negative indexes if you want to start the search from the end of the tuple:
#* This example returns the items from index -4 (included) to index -1 (excluded)

list_of_fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(list_of_fruits[-4:-1])

#! the first (starting) number of the index would be smaller then the end index like here starting is -4 and end is -1


# :: List :-

# - A List in python is a collection of items(elements) that are oredered , changable(mutable) , and allow duplicate elements.

# - List are one of the most versatile data structures in python and are used to store multiple items in a single variable.

# Example:

# fruits = ["Apple" , "Orange" , "Cherry" , "Apple"]
# print(fruits)
# Output :- ["Apple" , "Orange" , "Cherry" , "Apple"]




# ___________________________________________________________________________




# :: Create List in python :


# - You can create lists in python by placing comma-seperated values between square brackets[]. Lists can contain elements of different data types , including other lists.

# :- Syntax:  list_name = [element1 , element2  , element3 , .....]


# Example: lists of strings.
# colors = ["red","green","blue"]
# print(colors)  # Output: ["red", "green", "blue"]


# Example: list of integers.
# numbers = [1,2,3,5,6]
# print(numbers)  # Output: [1, 2, 3, 5,


# Example : Lists of data types.
# mixed = [1, "hello", 3.14, True]
# print(mixed)  # Output: [1, 'hello', 3.14, True]


# Example : Nested list.
# nested = [1,[2,3],[4,5,6]]
# print(nested) #output : [1, [2, 3], [4, 5, 6]]




# :: Accessing List Elements - [ List Indexing ] :-


# -You can Access elements in a list by referring to their index. Python uses zero-based Indexing , meaning the first elements has an index of 0.

# :- Syntax:  list_name[index]


# Example :  

# fruits =    ["Apple" , "orange" , "Cherry" , "apple" , "Mango"]

            #    0          1          2          3         4
# index:-->
            #   -5         -4         -3         -2        -1


#Access first element:
# print(fruits[0])  #output : apple


#Access third element
# print(fruits[2])  #output : cherry


# [IMPORTANT] : 
#Accessing last element using negative index
# print(fruits[-1]) #Output : mango



# print(type(fruits))  #output : <class 'list'>




# ___________________________________________________________________________





# :: Accessing List Elements - [ List Slicing ] :-

# - Slicing allow You to Access a range of elements in a list. You can specify the start , stop , step indices , and Python returns a new list containing the specified elements.

# :-Syntax : list_name[ start : stop : step ]

# Example :  numbers = [  10 , 20 , 30 , 40 , 50 , 60 ]
                        # 0     1    2    3    4    5
#   Index ---->          -6    -5   -4   -3   -2   -1


# print(numbers[1:4]) # Slice from index 1 to 3
# Output: [20 , 30 , 40]


# print(numbers[:3])  # Slice from start to index 2
# Output : [10,20,30]


# print(numbers[0::2]) # Slice all alternate elements
# Output : [10,30,50]


# print(numbers[-4:-1]) # Slice with negative indices
# Output : [30 ,40, 50]


# print(numbers[::-1])  # Reverse list
# Output : [60,50,40,30,20,10]


# NOTE:
# - start is inclusive , default is 0.
# - stop is exclusive , default is -1 / last index value.




# :: Modifying List :
# - Lists are mutable  , meaning you can change their content after creation. You can add , remove , or change elements in a list.

# :Initial list: 
# fruits = ["apple" , "banana" , "cherry"]


# Changing an Element : 

# fruits[1] = "blueberry"
# print(fruits) # Output :  ['apple' , 'blueberry', 'cherry']


# Adding an Element :

# fruits.append("mango")
# print(fruits)  # Output :  ['apple' , 'blueberry', 'cherry' , 'mango']


# Removing an Element :

# fruits.remove("cherry")
# print(fruits)  # Output : ['apple' , 'blueberry' , 'mango']



# ___________________________________________________________________________





# :: List Methods : 

# - Python provides sevreral built - in - methods to modify and operate on lists.





# 1. append() : Adds a single element to the end of the list.
# Ex:

# fruits = ["apple" , "banana" , "cherry"]
# fruits.append('2')
# fruits.append('bannana')
# print(fruits) # Output  : ['apple', 'banana', 'cherry', '2', 'bannana']







# 2. extend() : add multiple elements(from another iterable) to the end of the list.
# Ex:


# fruits = ["apple" , "mango" , "cherry"]

# # fruits.extend(['2','bannana'])
# print(fruits)
# # Output : ['apple', 'mango', 'cherry', '2', 'bannana']

# more_fruits = ["orange", "papaya"]
# fruits.extend(more_fruits)
# print(fruits)
# # output : ['apple', 'mango', 'cherry', 'orange', 'papaya']
 









# 3. insert() : Insert an element at a specified position.
# EX:

# fruits = ["apple" , "mango" , "cherry"]
# fruits.insert(3,"blueberry")
# print(fruits)  # Output : ['apple', 'mango', 'cherry', 'blueberry']










# 4. remove(): removes the first occurrence of a specified element.
# EX:

# fruits = ["apple" , "bananna" , "orange" , "bananna"]
# fruits.remove("bananna")
# print(fruits) # Output : ['apple', 'orange', 'bananna']









# 5. clear()  : Removes all elements from the list , resulting in an empty list.
# EX:

# fruits  = ["apple" , "orange"]
# fruits.clear()  #empty list
# print(fruits)  # Output : []











# 6. index() : Returns the index of the first occurrence of a specified element.
# Ex:

# fruits = ["apple" , "bananna" , "orange" , "bananna"]
# print(fruits.index("bananna")) # Output : 1

# NOTE: finding index - within a range
# index = fruits.index("bananna" , 2)
# print(index)  # Output : 3









# 7.  count() : Returns the number of occurrences of a specified element.
# Ex:

# fruits = ["apple" , "bananna" , "orange" , "bananna"]
# count = fruits.count("bananna")
# print(count) # output: 2







# 8. reverse() : Reverse the elements of the list in place.
# Ex:

# fruits = ["apple" , "bananna" , "orange" , "bananna"]
# fruits.reverse()
# print(fruits) # Output :  ['bananna', 'orange', 'bananna', 'apple']








# 9. sort() : sorts the list in ascending order by default. You can also sort in descending order by specifying custom sorting criteria.


# NOTE:
# - default sort : ascending order.
# - for descending order : give parameter as sort(reverse = True).

# Ex: 1
# numbers = [40,10,30,20]
# numbers.sort()
# print(numbers) # Output:  [10, 20, 30, 40] 

# EX : 2
# Sorting list in descending order:

# numbers.sort(reverse=True)
# print(numbers) #output :  [40, 30, 20, 10]

# Ex : 3
# Sorting with a key:

# fruits = ["apple" , "bananna" , "orange" , "bananna"]
# fruits.sort(key=len)  #sort based on length
# print(fruits)  # Output : ['apple', 'orange', 'bananna', 'bananna']








# 10. pop() : Remove and returns an element at a specified index. If no index is specified , it removes and returns the last element.

# Ex:1 Pop with index value

# numbers = [10,20,30,40]
# popped = numbers.pop(2)
# print(popped)   # Output : 30
# print(numbers)  # Output : 10,20,40


# Ex :2 Pop With default

# last = numbers.pop()
# print(last)  # Output : 40
# print(numbers)  # Output : [10, 20, 30]



# 11. copy() : Returns a shallow copy of the list.

# Ex:


# fruits = ["apple" , "bananna" , "orange" , "bananna"]
# copy_fruits = fruits.copy() # -->  Shallow copy
# print(copy_fruits) # Output : ["apple" , "bananna" , "orange" , "bananna"]

# # NOTE: modifying rhe copy list does not affect the actual list.
# copy_fruits.append("mango")
# print(copy_fruits)  # Output : ['apple', 'bananna', 'orange', 'bananna', 'mango']
# print(fruits)  # Output : ['apple', 'bananna', 'orange', 'bananna']






# ___________________________________________________________________________





# ::Join Lists : -



# -There are several ways to join  , or concatenate , two or more lists in python.

# list1 = [1,2,3]
# list2 = ["a","b"]



# # :Method - 1 :  using '+' operator.
# final_list = list1 + list2
# print(final_list)  # Output : [1,2,'a','b']




# :Method - 2 : using append() method with for loop.
# for x in list2:
#     list1.append(x)
# print(list1)  # Output : [1, 2, 3, 'a', 'b']



# :Method - 3 : using extend Method.

# list1.extend(list2)
# print(list1)  # Output : [1, 2, 3, 'a', 'b']




# ___________________________________________________________________________




# ::List Comprehensions : 

# - List Comprehensions provide a Concise way to create lists. They consist of brackets containing an expression followed by a for clause , and optionally if clause.

# : Syntax : # [expression for element in iterable if condition]

# Ex:

# new_list = [expression for item in interable if condition]


# # Creating a list of squares:

# squares = [x**2 for x in range(1,6)]
# print(squares)  #Output : [1,4,9,16,25]


# # Filtering Even Number :

# even_numbers = [x for x in range(1,11) if x%2 == 0]
# print(even_numbers) # Output : [2, 4, 6, 8, 10]


# # Applying a function to each element :

# fruits = ["apple" , "banana" , "cherry"]
# uppercase_fruits = [fruit.upper() for fruit in fruits]
# print(uppercase_fruits) # Output : ['APPLE', 'BANANA', 'CHERRY']


# # Flatten(simple list mai convert karna hai) a nested list using list comprehensions:

# nested_list = [[1,2],[3,4],[5,6]]

# result = [item for sublist in nested_list for item in sublist]
# print(result) # Output : [1, 2, 3, 4, 5, 6]


# def Flatten_list(list):
#     return [item for sublist in nested_list for item in sublist]

# final_list = Flatten_list(nested_list)
# print(final_list)
# Output : [1, 2, 3, 4, 5, 6]


# ___________________________________________________________________________


# :: Iterating Over Lists :

# Iterating allows you to traverse each element in a list , typically using loops

# Ex:

# fruits = ["apple" , "banana" , "cherry"]

# # Using for loop : 

# for fruit in fruits:
#     print(fruit)  # Output : ["apple" , "banana" , "cherry"]

# # Using while loop :

# index = 0

# while index < len(fruits):
#     print(fruits[index])  # Output : ["apple" , "banana" , "cherry"]
#     index += 1
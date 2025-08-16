# :: List :-

# - A List in python is a collection of items(elements) that are oredered , changable(mutable) , and allow duplicate elements.

# - List are one of the most versatile data structures in python and are used to store multiple items in a single variable.

# Example:

# fruits = ["Apple" , "Orange" , "Cherry" , "Apple"]
# print(fruits)
# Output :- ["Apple" , "Orange" , "Cherry" , "Apple"]



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




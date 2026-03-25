
                       # TOPIC :  Tuples in Python








# :: Tuple :-  ( )

# - A Tuple is a collection of items in Python that is ordered , unchangable(immutable) and allow duplicate values.

# - Tuples are used to store multiple items in a single variable.

# NOTE: Ordered - Tuple items have a defined order , but that order will not change.

# Example : 

# fruits = ('apple' , 'orange' , 'cherry' , 'apple')
# print(fruits) # Output : ('apple', 'orange', 'cherry', 'apple')


# ___________________________________________________________________________



# :: Create Tuple in Python :



# 1. Using Parantheses () :

# colors = ("green" , "blue" , "yellow" , "pink")
# print(colors) # Output : ('green', 'blue', 'yellow', 'pink')  

# numbers = (1,2,3,4,6)
# print(numbers)  # Output : (1, 2, 3, 4, 6)

# mixed = ( 1, "hello" , 3.14 , True )
# print(mixed)  # Output : (1, 'hello', 3.14, True)

# nested = (1,[2,3],(4,5,6))
# print(nested) # Output : (1, [2, 3], (4, 5, 6))







# 2. Without Parantheses ( Comma-Seperated ) : 

# also_numbers = 1 , 2 , 3 , 4 , 5
# print(also_numbers)  # Output  : (1, 2, 3, 4, 5)
# print(type(also_numbers)) # Output : <class 'tuple'>









# 3. Using the tuple() Constructor : 

# -  Must use double brackets
# new_tuple = tuple(("apple" , "banana" , "cherry")) 
# print(new_tuple)

# list_items = ["x","y","z"]
# tuple_items = tuple(list_items)
# print(tuple_items)  # Output : ('x', 'y', 'z')








# 4. Single-Item Tuple : 
# ye iske (" ") bad mai ',' lagana jaruri hai, agar nahi lagaya toh tuple nahi banega , as a string samjh lega .

# tuple_single = ("only")
# print(tuple_single)  # Output : only
# print(type(tuple_single))  # Output : <class 'str'>


# tuple_single = ("only",)
# print(tuple_single)  # Output : ('only',)
# print(type(tuple_single)) # Output : <class 'tuple'>


# ____________________________________________________________________




# :: Accessing Tuple Elements - Indexing : 

# - You can access elements in a tuple by referring to their index. Python uses zero-based indexing , meaning the first element has an index of 0.

# Syntax : tuple_name[index]

# Example : fruits = ("apple" , "orange" , "cherry" , "apple", "mango")
                    #   0         1           2         3       4
#       index -->
                    #  -5        -4          -3        -2      -1


# Access first element :
# print(fruits[0])  # Output : apple


# # Access third element : 
# print(fruits[2]) # Output : cherry


# # Access last element using negative index
# print(fruits[-1])  # Output : mango



# ____________________________________________________________________



# :: Tuple Slicing : 



# - Slicing allows you to access a range of elements in a tuple. You can specify the start and stop indices , and Python returns a new tuple containing the specified elements.

# Syntax : tuple_name[start : stop : step]

# Example : numbers = ( 10 , 20 , 30 , 40 , 50 , 60 ) 
                    #  0    1    2    3    4    5
    #  index -- >
                    # -6   -5   -4   -3   -2   -1

# Slice from index 1 to 3 :
# print(numbers[1:4])  # Output : (20,30,40)


# Slice from start to index 2 : 
# print(numbers[:3]) # Output : (10,20,30)


# Slice all alternate elements : 
# print(numbers[0::2]) # Output : (10,30,50)


# Slice with negative indices :
# print(numbers[-4:-1])  # Output : (30,40,50)


# NOTE:  Reverse list

# print(numbers[::-1])  # Output : (60,50,40,30,20,10)



# ____________________________________________________________________




# :: Tuple Operation : 





# 1. concatenation : 

#- You can join two or more tuples using the + operator.

# Ex:

# tuple1 = (1,2,3)
# tuple2 = (4,5)
# combined = tuple1 + tuple2
# print(combined)  # Output : (1,2,3,4,5)




# 2.  Repetition : 
# - You can repeat a tuple multiple times using + operator.
# tuple3 = ("hello",) * 3
# print(tuple3)  # Output : ('hello','hello','hello')



# 3. Checking for an Item : 
# - Use the in keyword to check if an item exists in a tuple.
# numbers = (10,20,30,40)
# print(20 in numbers) # Output : True





# ____________________________________________________________________





# :: Iterating Over Tuple :

# - Iterating allows you to traverse each element in a tuple , using loops.

# Ex:  fruits = ("apple" , "mango" , "cherry")






# :: Using for loop :

# for fruit in fruits:
#     print(fruit)   # Output : ("apple" , "mango" , "cherry")






# :: Using while loop : 

# i = 0

# while i < len(fruits):
#     print(fruits[i])   # Output : ("apple" , "mango" , "cherry")
#     index += 1





# _________________________________________________________________________



# :: Tuple Methods : 

# - Python provides two built-in-methods to use on tuples.



# 1. count() : 
# - Returns the number of times a specified value occurs in a tuple.

# Ex : 

# colors = ("red" , "green" , "blue" , "green")
# print(colors.count("green"))  # Output : 2




# 2. index()  :
# - Searches in the tuple for a specified value and return the position of where it was found.


# Ex:

# colors = ("red" , "green" , "blue" , "green")
# print(colors.index("blue"))  # Output : 2



# ____________________________________________________________________




# :: Tuple Functions : 

# - Python provides several built-in-functions to use on tuples.





# 1. len() :
# - Returns the number of items in a tuple.

# Ex:

# numbers = (2,3,1,4)
# print(len(numbers))  # Output : 4







# 2. sorted() : [method to convert a given tuple into an list and then sort and again convert it into the tuple.].

# - Returns a new "List" from the items in the tuple.

# Ex:
# numbers = (2,3,1,4)
# sorted_num = sorted(numbers)
# print(sorted_num)  # Output : [1,2,3,4]

# # NOTE: convert a list again into an tuple :

# a = tuple(sorted_num)
# print(a)  # Output :  (1, 2, 3, 4)









# 3.  Sum() :
# - Return up all the numeric items in the tuple.

# Ex:

# numbers = (2,3,1,4)
# print(sum(numbers))  # Output : 10










# 4. min() , max() :
# - Return the smallest and largest items in the tuple , respectively.

# Ex:

# # numbers = (2,3,1,4)
# print(min(numbers))   # Output : 1
# print(max(numbers))   # Output : 4







# ____________________________________________________________________


# :: Packing and Unpacking Tuples : 



# 1. Packing : is the process of putting multiple values into a single tuple.

# Ex : 

# name = "Anubhav"
# age = 20
# profession = "Cloud_Engineer"
# pack_tuple = name , age , profession
# print(pack_tuple)   # Output : ('Anubhav', 20, 'Cloud_Engineer')










# 2. Un-Packing :  is the process of extracting the values from a tuple into seprated variables.

# Ex:

# name , age , profession = person   # Unpacking a tuple
# print(name)  # Output : Madhav
# print(age)  # Output : 21
# print(profession)  # Output : Engineer




# ____________________________________________________________________


# :: Modifying Tuple  -  [Immutable] : 

# Once a tuple is created , you can not modify its elements.This means you cannot add , remove , or change items.


# --> Ex:

# # Creating a tuple : 
# numbers = (1,2,3)


# # Attempting to change an item : 
# numbers[0] = 10   ----> This will raise an error.




# SOLUTION TO THIS PROBLEM : 

# - simply convert tuple into list then perform operation and than after performing all operation , convert the list into an tuple.

# Ex : 

# tuple_numbers = 1,2,3,4

# converting_list = list(tuple_numbers)   # Converting tuple into an list. 

# print(converting_list)   # Output : [1, 2, 3, 4]
# print(type(converting_list))  # Output : <class 'list'>

# converting_list[0] = 100   # performing operation

# print(converting_list)  # Output : [100, 2, 3, 4]

# converting_tuple = tuple(converting_list)  # Converting list into an tuple.

# print(converting_tuple)  # Output : (100, 2, 3, 4)




# ____________________________________________________________________


# :: Usecases of Tuple : 


# 1. Storing Fixed Data ( Immutable Data ) : 

# - Example : 
# -Storing geographic coordinates(latitute,longitude) or RGB color values , where the values should not be changed after assignment.

# coordinates = (40.7128, -74.0060)  # Latitude and longitude for NYC
# rgn_color = (255,0,0) # RGB value for red




# 2. Using Tuples as keys in Dictonaries : 
# - Since tuples are immutable and hashable , they can be used as keys in Dictonaries unlike lists.

# location_data = {
#     (40.7128 , -74.0060) : "New York City",
#     (34.0522 , -118.2437) : "Los Angeles"
# }

# print(location_data[40.7128,-74.0060]) # Output : New York City
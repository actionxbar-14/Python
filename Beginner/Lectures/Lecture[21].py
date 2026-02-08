
                                      # TOPIC : Sets in Python

# 1. What is a Set.
# 2. Create Sets.
# 3. Set Operations.
# 4. Set Methods.
# 5. Set Iteration.
# 6. Set Comprehensions.







# ::  Sets in Python : 

# - A Set is a Collection of unique items in Python. Sets do not allow duplicate items and do not maintain any particular order so it can't be indexed.


# : Characterstics in Python : 

# ---> Unordered : Elements have no defined order. You cannot access element by index.
# ---> Unique Elements : No duplicate allowed. Each element must be distinct.
# ---> Mutable : You can add or remove elements after creation.
# ---> Immutable Elements : Individual elements insidee a set cannot be modified / replaced

# Ex:

# vowels = {'a', 'e' , 'i' , 'o' , 'u'}




# _____________________________________________________________________________________





# :: Create Set in Python : 

# - There are twoo primary ways to create a set in Python :





# 1. Using Curly Braces {} :

# my_set = {1,2,3,4,5}
# print(my_set)  # Output : {1,2,3,4,5}







# 2. Using the set() Constructor : 

# my_set = set([1,2,3,4,5])
# print(my_set)   # Output : {1,2,3,4,5}






# :: NOTE :  An empty set can not be created using empty curly braces {} as it creates an empty dictionary. use set() method to create empty set.


# empty_set = {}   #---> This will create a empty dictonary

# empty_set = set()
# print(empty_set)  # Output : set()



# _____________________________________________________________________________________



# :: Set Operations : 


# 1.  Adding Elements : Use the add() method to add a single element to a set.
# fruits = {'apple', 'banana'}
# fruits.add('cherry')
# print(fruits)   # Output : {'apple', 'banana', 'cherry'}






# 2. Removing Elements : Use the remove() or discard() methods to remove elements.

# --> remove() : raised an error if the element is not found.
# --> discard() : does not raise an error if the element is missing.


# fruits = {'apple' , 'banana' , 'cherry'}


# # Using remove() :
# fruits.remove('banana')   # it give error if the 'banana' is not present in the set.
# print(fruits)   # Output : {'apple','cherry'}



# # Using discard() :
# fruits.discard('orange')    # No error if 'orange' is not present in the set.
# print(fruits)   # Output : {'apple' , 'cherry'}






# ____________________________________________________________________________________________________________



# ::  Set Methods : 




# 1. Union : Combines elements from two sets , removing duplicates.

# Ex:

# set_a = {1,2,3}
# set_b = {3,4,5}

# union_set = set_a.union(set_b)
# union_Set =   set_a  | set_b
# print(union_set)     # Output : { 1,2,3,4,5 }


# :NOTE  Alternative Syntax : union_Set =   set_a  | set_b






# 2. Intersection : Includes only elements present in both sets.

# Ex: 

# set_a = {1,2,3}
# set_b = {2,3,4}

# intersection_set = set_a.intersection(set_b)
# intersection_set = set_a & set_b 
# print(intersection_set)   # OUtput : {2,3}







# 3. Difference : Elements present in the first set but not in the second set.

# Ex: 

# set_a = {1,2,3,4}
# set_b = {3,4,5}

# difference_set =  set_a.difference(set_b)
# print(difference_set)   #Output : {1,2}


# # NOTE : Alternative Syntax : difference_set = set_a - set_b







# 4. Symmetric Difference : Elements in either set  , but not in the both.

# Ex:

# set_a = {1,2,3}
# set_b = {3,4,5}

# symm_diff_set = set_a.symmetric_difference(set_b)
# print(sym_diff_set)   # Output :  {1,2,4,5}

# # NOTE : Alternative Syntax : sym_diff_set = set_a  ^  set_b







# ____________________________________________________________________________________________________________



# :: Set Iteration :

# - You Can use a for loop to go through each element  in a Set.






#  Using for loop :  Printing each number from a set.

# Ex:

# numbers = {1,2,3,4,5}
# for number  in numbers:
#     print(number)       # Output : {1,2,3,4,5}







# Using While loop :  we can not directly use while loop in set because while loop consisits of indexing and  set does not support index , so we first convert set to a list then use while loop and the again converts it into set.

# Ex:

# numbers = {1,2,3,4,5}


# index = 0
# while index < len(numbers):
#      print(numbers[index], end = " ")  # Produces an error
#      index+=1




# numbers = {1,2,3,4,5}

# numbers_list = list(numbers)
# print(numbers_list)   #output : [1, 2, 3, 4, 5]


# index = 0 

# while index < len(numbers_list) :
#     print(numbers_list[index])
#     index += 1








# ____________________________________________________________________________________________________________



# :: Set Comprehensions :

# - Set Comprehensions allow concise and readable creation of sets. similar to list comprehensions but for sets.


# Syntax : { expression for item in iterable if condition }.


# Example :

# squares =   { x**2 for x in range(1,6)}
# print(squares)  # Output : {1,4,9,16,25}




# :: Youtube Playlist Content : 

# --> lecture-95  :  Set in Python. 
# --> lecture-96  :  Adding & Removing items from set.
# --> lecture-97  :  Union & Intersection of sets. 
# --> lecture-98  :  Difference & symmetric difference in set. 
# --> lecture-99  :  All about frozenset. 
# --> lecture-100 :  Python Assignment Question. 


# ____________________________________________________________________________________________________________________________________



# :: Set in Python :
# - A set is an unordered collection of items of different types enclosed in curly braces. 
# - Ex : 

# my_set = {101 , 'shantanu' , 'pass ' , 98.2}

# print(my_set)






# :--> Creation of Set : 
# - There are two ways of creating set :

# 1.) Using curly braces { } :
# - Syntax : set_name = {element1 , element2 , element3 , element4 .....}

# - Ex : 

# my_set = {101 , 'shantanu' , 'pass ' , 98.2}

# print(my_set)




# 2.) Using set() function :
# - Syntax : set_name = set(iterable)

# - Ex : 

# list_of_element =   101 , 'shantanu' , 'pass' , True , 98.2
# my_set = set(list_of_element)

# print(my_set) 

# print(type(my_set))  # --> <class 'set'>
# print(type(list_of_element))  # -->  <class 'tuple'>




# - Ex :  

# my_set = set("Hello")

# print(my_set) # output : {'H', 'o', 'l', 'e'}





# NOTE :  


# 1.) No duplicates are allowed. 

# Ex:  

# my_set = {10 , 20, 20,  30 , 40 , 50 , 30}
 
# print(my_set)  # output : {50, 20, 40, 10, 30}







# 2.) Elements are not in particular order. 

# - Ex : 

# my_set = {20 , 20 , 10 , 10 , 20 , 30 , 20}

# print(my_set)  # output : {10, 20, 30} / {20 , 10 , 30} / {30 , 10 , 20} .... 








# 3.) Indexing and slicing can't be applied on set. 
# # - Ex : 

# my_set = {10 , 20 , 10 , 10 , 20 ,30 , 20}
# print(my_set[1])

#     print(my_set[1])
#           ~~~~~~^^^
# TypeError: 'set' object is not subscriptable







# 4.) Set is mutable . 
# - We can add an element anywhere in the set using .add() method. 
# - Ex : 

# my_set = {10, 20 , 10 , 10 , 20 , 30}

# my_set.add(100)

# print(my_set)  # output : {100, 10, 20, 30}






# 5.) Element in set must be immutable . 
# NOTE : We can not write mutable things(like : list) inside the set. 
# NOTE: nested set is also not allowed , beacuse we can't write mutable things inside set. 
# NOTE: iteration of set is not possible , beacuse it does not follow indexing method. 

# - Ex : 

# my_set = {10 , 20 , 10 , 10 , [10 ,20 , 30]}
# print(my_set)

# # output :     my_set = {10 , 20 , 10 , 10 , [10 ,20 , 30]}
# #              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # TypeError: unhashable type: 'list'



# - Ex : 

# my_set = {10 , 20 , 10 , 10 , {10 ,20 , 30}}
# print(my_set)

# # Output :  my_set = {10 , 20 , 10 , 10 , {10 ,20 , 30}}
# #              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # TypeError: unhashable type: 'set'


















# :--> Creation of Empty set : 

# - Syntax : set_name = set()
# - Ex : 

# set_name = set()
# print(set_name)  # output : set()










# ____________________________________________________________________________________________________________________________________



# :: Built-in methoda of Python Set : 


# 1.) add() method  
# 2.) update() method 
# 3.) remove() method 
# 4.) discard() method 
# 5.) pop() method 
# 6.) clear() method








# 1.) add() method : 
# - Add single item to set at random position. 
# - Syntax :  set_name.add(item)

# - Ex : 

# my_set = {10 , 20 , 40}

# my_set.add(50)

# print(my_set)  # output : {40, 10, 20, 50}













# 2.) update() method : 
# - Add multiple items to set at random positions. 
# - Syntax :  set_name.update([item1 , item2])

# - Ex : 


# w_days = {'monday' , 'friday' , 'saturday'}

# w_days.update(['sunday' , 'tuesday', 'wednesday' , 'thrusday'])

# print(w_days)  # output : {'friday', 'tuesday', 'sunday', 'wednesday', 'thrusday', 'monday', 'saturday'}













# 3.) remove() method : 
# - Remove single item .
# - Syntax :  set_name.remove(item)


# - Ex : 



# w_days = {'monday' , 'friday' , 'saturday'}

# print(w_days.remove('monday'))  # output:     w_days.remove('monday')
# # KeyError: 'monday'

# w_days.remove('monday')
# print(w_days)  # output : {'friday', 'saturday'}



# NOTE :  .remove() method gives an error if item is not present in the set. 













# 4.) discard() method :
# -  Remove single item. 
# - Syntax : se_name.remove(item)


# - Ex : 




# w_days = {'monday' , 'friday' , 'saturday'}

# print(w_days.discard('monday'))    # output : None

# w_days.discard('monday')
# print(w_days)  # output : {'friday', 'saturday'}




# NOTE :  .discard() method doen not gives an error if item is not present in the set. 
















# 5.) pop() method : 
# - Remove sinle item randomly. 
# - Syntax : set_name.pop()

# - Ex : 




# w_days = {'monday' , 'friday' , 'saturday' , 'sunday'}

# # w_days.pop()

# print(w_days.pop())  # output : monday
# print(w_days)  # output : {'saturday', 'sunday', 'friday'}



# NOTE : It returns the removed value.









# 6. clear() : 

# - clear() method clear all the item present in the set.  
# - Syntax: my_set.clear()

# - Ex : 



# w_days = {'monday' , 'friday' , 'saturday' , 'sunday'} 
# print(w_days)  # output : {'saturday', 'sunday', 'friday', 'monday'}

# w_days.clear()

# print(w_days)  # output : set()





# 7. del method : 
# - It is used to delete the complete set from the memory. 
# - Syntax : del set_name 

# - Ex : 


# w_days = {'monday' , 'friday' , 'saturday' , 'sunday'} 

# del w_days
# print(w_days)  # output :     print(w_days)
#           ^^^^^^
# NameError: name 'w_days' is not defined











# ____________________________________________________________________________________________________________________________________





# :: Set Operations in Python : 
# - There are total of 5 Set Opeartions  :-

# 1.) Union of sets. 
# 2.) Intersetion of sets 
# 3.) Difference of sets 
# 4.) Symmetric difference 
# 5.) Comparing sets 










# 1.) Union of sets : 
# - Union of two sets is the smallest set which contains all the elements of both the sets.
# - It creates a new set and does not affect the actual set.  
# - Syntax : x.union(y)  and  x | y . 
# - Ex : 

# A = {2 , 4 , 5, 6 }
# B = {4 , 6, 7 , 8 }


# print( A | B)      # Output : { 2, 4, 5, 6, 7, 8}

# print(A.union(B))  # output : {2, 4, 5, 6, 7, 8}













# 2.) Intersection of sets : 
# - Intersection of two given sets is the largest set which contains all the elements that are common to both the sets. 
# - Syntax : set1 & set2  and  set1.intersection(set2)
# - Ex : 

# A = {2 , 4, 5 ,6}
# B = {4 , 6 , 7, 8}

# print( A & B)  # output : {4, 6}

# print(A.intersection(B))  # output :   {4, 6}










# 3.)  Difference of sets : 
# - The difference between the two sets in Python is equal to the difference between the number of elements in two sets. 
# - Syntax :   set1 - set2  and  set1.difference(set2)

# - Ex : 

# A = { 2, 4, 5, 6 }
# B = { 4, 6, 7, 8 }


# print(A-B)  # output : {2, 5}
# print(B-A)  # output : {8, 7}


# print(A.difference(B))  # output (A-B) :  {2, 5}
# print(B.difference(A))  # output (B-A) :  {8, 7}














# 4.) Symmetric Difference of sets : 
# - The symmetric difference of two sets is a set of elements that are in either set , but not in their intersection. 

# - Syntax :   A ^ B  and  A.symmetric_difference(B)


# - Ex : 



# A = { 2, 4, 5, 6 }
# B = { 4, 6, 7, 8 }

# print(A^B)  #  output : {2, 5, 7, 8}
# print(B^A)  #  output : {2, 5, 7, 8}





# print(A.symmetric_difference(B))  #  output : {2, 5, 7, 8}
# print(B.symmetric_difference(A))  #  output : {2, 5, 7, 8}
















# 5.) Comparion of sets : 
# - i.)  superset
# - ii.)  subset



# - Ex : 

# s1 = {10 , 20 , 30 , 40 , 50}
# s2 = {20 , 40} 

# print(s1 > s2)  # output : True
# print(s1 < s2)  # Output : False


# # - Ex : 

# A = {10 , 20}
# B = {10 , 20}
# print(s1 == s2) # output : False







# ________________________________________________________________________________________________________________________________




# :: Frozenset in Python : 
# - Frozenset is an immutable version of Python set. ( Frozen ---> unchangable )
# - While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. 
# - There is no methods like add , update , remove for frozenset like set. 




# :--> How to Create Frozenset : 
# - By using frozenset() inbuilt function. 
# - Syntax : forzenset(iterable) , where iterable is an optional argument , iterable can be list , string , tuple ,set , dict. 



# - Ex : 


# vowels = {'a' , 'e' , 'i' , 'o' , 'u'}

# f_set  = frozenset(vowels)

# print(f_set)  # output : frozenset({'e', 'o', 'a', 'u', 'i'})




# - Ex : using dictionary 

# my_dict = { 'one' : 1 , 'two' : 2}

# f_set = frozenset(my_dict)

# print(f_set)  # output : frozenset({'two', 'one'})





# # - Ex : using string 

# my_str = 'anubhav'

# f_set = frozenset(my_str)

# print(f_set)  # output  : frozenset({'n', 'b', 'a', 'v', 'h', 'u'})





# NOTE : We can perform Set operations ( union , intersection , difference , symmetric difference) on frozenset. 







# ________________________________________________________________________________________________________________________________





# :: Python Assignment Questions : 




# Question 1 :  print output 

# print(type({}) is set)  # output ; False





# Question 2 : print output 

# nums = set([11 , 11 , 22 , 22 , 22 , 33 , 33 , 4 ,4 ,4])

# print(len(nums))  # output : 4




# Question 3 : print output 

# print({1,2,3} + {4 ,5 ,6})  # output :     print({1,2,3} + {4 ,5 ,6})
#           ~~~~~~~~^~~~~~~~~~~
# TypeError: unsupported operand type(s) for +: 'set' and 'set'





# Question 4 : what is the output ?

# set1 = {10 , 20 , 30 , 40}
# set2 = {50  , 20 , "10" , 60}
# set3 = set1.union(set2)

# print(set3)  # output : {'10', 40, 10, 50, 20, 60, 30}






# Question 5 : what is output

# set1 = {10 , 20  , 30 , 40 , 50}
# set2 = {60 , 70  , 10  , 30 , 40  , 80 , 20  , 50 }

# print(set1.issubset(set2))   # output : True
# print(set2.issuperset(set1)) # output : False






# # Question 6 : what is output : 

# set1 = {1 ,2 , 3}
# set2 = {4 , 5 ,6}

# print(len(set1 + set2))  # output :   print(len(set1 + set2))
#               ~~~~~^~~~~~
# TypeError: unsupported operand type(s) for +: 'set' and 'set'





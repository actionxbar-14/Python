# :: Youtube Playlist Content : 

# --> lecture-131 : Chaining In Python.
# --> lecture-132 : Dictionary / Set comprehension. 
# --> lecture-133 : Can we use "if-elif" in list comprehension. 
# --> lecture-134 : Deep copy v/s Shallow copy - 1. 
# --> lecture-135 : Deep copy v/s Shallow copy - 2. 


# _______________________________________________________________________________________________________________________________________



# :: Chaining in Python : 
# - Chaining is used in Python where we have to use multiple condition like (if-elif else) in the List comprehension. 
# - We can use 'if-elif-else' in List comprehensiin by using the chaining concept. 
# - For using chaining if and elif and else block must contain only one statement. 

# # (Syntax without chaining) :

# if condition_1:
#     code_1
# elif condition_2:
#     code_2 
# elif condition_3:
#     code_3 
# else:
#     code_4 




# ( Syntax with chaining ) :

# code_1 if condition_1 else code_2 if condition_2 else code_3 if condition_3 else code_4  






# - Ex : ( Implementation without chaining )


# num = int(input("Enter a number :"))

# if num > 0 :
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")
    




# - Ex : ( Implementation with chaining )


# num = int(input("Enter a number :"))

# print("Positive" if num > 0 else "negative" if num < 0 else "zero")

    





# :--> Using chaining with list comprehension :

# # - Ex : ( without list comprehension )

# nums = [90.0 , -34 , 33 ,-21 , 20 ]
# status = []

# for num in nums:
#     if num > 0:
#         status.append("positive")
#     elif num < 0:
#         status.append("negative")
#     else:
#         status.append("zero")
        
        
# print(status)  # output : ['positive', 'negative', 'positive', 'negative', 'positive']
    
    
    
    


# - Ex : ( with list comprehension )

# nums = [90.0 , -34 , 33 ,-21 , 20 ]
# status = []
# print(["Positive" if num > 0 else "negative" if num < 0 else "Zero" for num in nums]) # output : ['Positive', 'negative', 'Positive', 'negative', 'Positive']







# _______________________________________________________________________________________________________________________________________





# :: Dictionary Comprehension :

# - Syntax : { key : value for (key , value) in iterable }. 



# - Ex_1 : ( without dictionary comprehension )

# nums = [1, 2 ,3 ,4 ,5]
# my_dict = {}

# for num in nums:
#     my_dict[num] = num**2
    

# print(my_dict)  # output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}




# - Ex_1 :  ( with dictionary comprehension )

# nums = [1, 2 ,3 ,4 ,5]

# my_dict = {num : num**2 for num in nums}

# print(my_dict)  # output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}






















# - Ex_2 : (without dictionary comprehension [using if condition])


# nums = [1, 2 ,3 ,4 ,5]
# my_dict = {}

# for num in nums:
#     if num%2 == 0:
#         my_dict[num] = num**2
 
# print(my_dict)  # output : {2: 4, 4: 16}





# - Ex_2 : ( with dictionary comprehension [using if condition] ). 



# nums = [1, 2 ,3 ,4 ,5]

# my_dict = {num : num**2 for num in nums if num%2==0}

# print(my_dict)  # output : {2: 4, 4: 16}














# - Ex_3 :  ( without dict comprehension )

# str1 = "cOding"
# my_dict = {}
# for char in str1:
#     my_dict[char.upper()] = (ord(char) , ord(char.swapcase()))
# print(my_dict)  # output : {'C': (99, 67), 'O': (79, 111), 'D': (100, 68), 'I': (105, 73), 'N': (110, 78), 'G': (103, 71)}





# - Ex_3 : ( with dict comprehension )


# str1 = "cOding"
# my_dict = {(char.upper()) : (ord(char) , ord(char.swapcase())) for char in str1}

# print(my_dict)  # output : {'C': (99, 67), 'O': (79, 111), 'D': (100, 68), 'I': (105, 73), 'N': (110, 78), 'G': (103, 71)}














# _______________________________________________________________________________________________________________________________________



# :: Set Comprehension : 

# - Ex : 


# nums = [1 , 2 , 3 , 4]

# set_nums = {n**2 for n in nums}

# print(set_nums)  # output : {16, 1, 4, 9}







# NOTE : When to use Comprehension :-

# - When we want a new data structure with new elements. 










# _______________________________________________________________________________________________________________________________________


# :: Can we use "if-elif" in list comprehension : ( using chaining method )

# - we have to follow this syntax  for converting into chaining : 

# for var in iterable:
#     if cond1:
#         exp_1 
#     else:
#         if cond2:
#             exp2 
#         else:
#             if cond3:
#                 exp3 
#             else:
#                 #code


# - Ex: ( without chaining ) 

# results = []
# marks = [89 , 91 , 56 , 34 , 70  , 71 , 81 , 12 ]

# for m in marks:
#     if m >= 80 and m <= 100:
#         results.append("A")
#     elif m >= 60 and m < 80:
#         results.append("B")
#     elif m >= 35 and m < 60:
#         results.append("C")
#     else:
#         results.append("Failed or Invalid marks")
        
# print(results) 






# - Ex: ( with chaining ) 



# marks = [89 , 91 , 56 , 34 , 70  , 71 , 81 , 12 ]


# results = ["A" if (m >= 80) and (m <= 100) else "B" if (m >= 60) and (m < 80) else "C" if (m >= 35) and (m < 60) else "Failed or Invalid makrs" for m in marks]


# print(results)   # output : ['A', 'A', 'C', 'Failed or Invalid makrs', 'B', 'B', 'A', 'Failed or Invalid makrs']







# _______________________________________________________________________________________________________________________________________




# NOTE : Assignment operator does not copy the objects it just take the refrence of previously present object , so we don't use assignment (=) operator for the copy of object . 

# Ex : 


# my_list = [[1,2,3] , [4,5,6], [7,8,'a']]
# print("id of mylist :" , id(my_list)) # Output : id of mylist : 1792446163072

# print("id of first element :" , id(my_list[0]))  # output : id of first element : 1792446003456
# print("id of second element :" , id(my_list[1])) # output : id of second element : 1792446163008
# print("id of third element :" , id(my_list[2])) # output : id of third element : 1792446004352


# print("-" * 50)


# new_list = my_list 
# print("id of new_list :" , id(new_list))   # output : id of new_list : 1792446163072



# print("id of first element :" , id(new_list[0]))  # output : id of first element : 1792446003456
# print("id of second element :" , id(new_list[1]))  # output : id of second element : 1792446163008
# print("id of third element :" , id(new_list[2]))  # output : id of third element : 1792446004352














# :: Deep and Shallow Copy - 1 : 

# - Sometime you may want to have the original values unchanged and only modify the new values or vice versa. In Python , there are two ways to create copies :

# 1.)  Deep Copy 
# 2.)  Shallow Copy 

# - To make these copy work , we use the copy module.  











# 1.) Shallow Copy : 
# - Shallow copy mai changes in original object does gives effect in the copied object. Iska use tab kiya jata hai jab hame object ko memory mai save karna hai and dono object mai sath sath changes chaiye. 

# - Ex : 

# import copy

# my_list = [[1,2,3] , [4,5,6], [7,8,'a']]
# print("id of mylist :" , id(my_list)) # Output : id of mylist : 2252339670464

# print("id of first element :" , id(my_list[0]))  # output : id of first element : 1792446003456
# print("id of second element :" , id(my_list[1])) # output : id of second element : 1792446163008
# print("id of third element :" , id(my_list[2])) # output : id of third element : 1792446004352


# print("-" * 50)


# new_list = copy.copy(my_list) 
# print("id of new_list :" , id(new_list))   # output : id of new_list : 2252339670528



# print("id of first element :" , id(new_list[0]))  # output : id of first element : 1792446003456
# print("id of second element :" , id(new_list[1]))  # output : id of second element : 1792446163008
# print("id of third element :" , id(new_list[2]))  # output : id of third element : 1792446004352













# 2.) Deep Copy : 
# - Deep copy mai changes in original object does not gives effect in the copied object. Iska use tab kiya jata hai jab hame object ko memory mai save karna hai and original object mai change krne se new_copied object mai kuch change na ho. 



# - Ex : 



# import copy

# my_list = [[1,2,3] , [4,5,6], [7,8,'a']]
# print("id of mylist :" , id(my_list)) # Output : id of mylist : 2363412508160

# print("id of first element :" , id(my_list[0]))  # output : id of first element : 2363412696768
# print("id of second element :" , id(my_list[1])) # output : id of second element :2363412508096
# print("id of third element :" , id(my_list[2])) # output : id of third element : 2363412506944


# print("-" * 50)


# new_list = copy.deepcopy(my_list) 
# print("id of new_list :" , id(new_list))   # output : id of new_list :  2363412508224



# print("id of first element :" , id(new_list[0]))  # output : id of first element : 2363412508288
# print("id of second element :" , id(new_list[1]))  # output : id of second element : 2363412510464
# print("id of third element :" , id(new_list[2]))  # output : id of third element :2363412510784

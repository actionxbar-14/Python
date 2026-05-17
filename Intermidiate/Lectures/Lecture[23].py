
# :: Youtube Playlist Content : 


# --> lecture-117 : set default method. 
# --> lecture-118 : Nested dictionary in Python. 
# --> lecture-119 : Accessing Nested dictionary. 
# --> lecture-120 : dictionary as a input. 


# _______________________________________________________________________________________________________________________ 



# :: setdefault() method : 
# - In Python dictionary , setdefault() method returns value of specified key if key exist. 
# - If key is not exists then it simple create a key and take the default value parameter as the value of key. 
# - Syntax : dict_name.setdefault( key , default_val ) 



# - Ex :  if key exists

# student = {'anmol' : 12000 , 'raj' : 13000 , 'jay' : 14000}
# fee = student.setdefault('raj')
# print(fee)   # output : 13000 


# - Ex : if key is not exists 


# student = {'anmol' : 12000 , 'raj' : 13000 , 'jay' : 14000}
# fee = student.setdefault('raja' , 15000)

# print(student)  # output : {'anmol': 12000, 'raj': 13000, 'jay': 14000, 'raja': 15000}
# print(fee)  # output : 15000





# _______________________________________________________________________________________________________________________ 



# ::  Nested dictionary :  
# - A dictionary within another dictionary is called as nested dictionary. 
# - Syntax : 

# nested_dict = { 'dict_A ' : {'key1' : 'val1'} , 
#                 'dict_B'  : {'key2' : 'val2'} 
#                }


#- Ex: 

# students = {'amar' : {'age': 21 , 'gender' : 'male' , 'fees' : 12000},
#             'rakesh' : {'age': 22 , 'gender' : 'male' , 'fees' : 14000},
#              'jay' : 12000
#            }

# print(students) # output  : {'amar': {'age': 21, 'gender': 'male', 'fees': 12000}, 'rakesh': {'age': 22, 'gender': 'male', 'fees': 14000}, 'jay': 12000}








# NOTE:
# - We can't use dictionary as key. 
# - We can use dictionary as value. 


# - Ex : 

# my_dict = { {'one' : 1} : 'first'}

# print(my_dict)  # output :    my_dict = { {'one' : 1} : 'first'}
#               ^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'dict'






# _______________________________________________________________________________________________________________________ 




# :: Accessing Nested dictionary items : 

# - Ex : 

# student = {'jay' : {'age' : 22 , 'marks' : {'one': 1}} , 'raj' : {'age' : 23 , 'marks' : 98}}

# print(student)  # output : {'jay': {'age': 22, 'marks': {'one': 1}}, 'raj': {'age': 23, 'marks': 98}}

# print(student['jay'])  # output : {'age': 22, 'marks': {'one': 1}}


# print(student['jay']['marks'])  # output : {'one': 1}

# print(student['jay']['marks']['one'])  # output:  1





# _______________________________________________________________________________________________________________________ 



# :: Dictionary as a input : 

# - Ex : using for loop

# student = {}   # empty dictionary 

# n = int(input('How many students :'))

# for i in range(n):
    
#     name =  input("Enter name of student :")
#     fee  =  float(input("Enter fees of student : "))
#     student[name] = fee
    
# print(student)





# - Ex : using while loop




# student = {}   # empty dictionary 


# while True:
    
#     name =  input("Enter name of student :")
#     fee  =  float(input("Enter fees of student : "))
#     student[name] = fee
#     ans = input('Do you want to continue(y/n) : ')
#     if ans != 'y':
#         break
    
# print(student)



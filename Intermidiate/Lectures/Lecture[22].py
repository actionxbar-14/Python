
# :: Youtube Playlist Content : 

# --> lecture-111 : Shallow Copy of dictionary.
# --> lecture-112 : Iteration on dictonary. 
# --> lecture-113 : zip() function / zipping iterables. 
# --> lecture-114 : keys() method / Fetching all keys. 
# --> lecture-115 : values() method / Fetching all values.
# --> lecture-116 : items() method / fetching all items. 


# _______________________________________________________________________________________________________________________ 


# :: Shallow copy of dictionary : 
# - shallow copy can be created by two methods :-

# 1.) Using copy() method.
# 2.) Using assignment(=) operator. 




# 1.)  Using copy() method : 
# - Creates new copy of dictionary and returns it. 
# - Syntax :   dict_name.copy()  
# - It doen not take any argument.
# - Id alag - alag hai iska matlab ak alag object bana hai new_student ke liye. 


# - Ex : 

# old_student = { 'karan' : 12000 , 'jesan' : 30000 , 'john' : 14000}

# new_student = old_student.copy()


# print(new_student)   # output : {'karan': 12000, 'jesan': 30000, 'john': 14000}
# print(id(new_student))  # output : 2415301786048

# print(old_student)   # output : {'karan': 12000, 'jesan': 30000, 'john': 14000}
# print(id(old_student)) # output :  2415300333696















# 2.) Using assignment(=) operator :
# - ye naya object nahi banata bss identifier ko point kara deta hai uss memory location se jaha pahle value store hoti hai. 
# - id agar same hai matlab koi naya object nahi bana hai. 
# NOTE:  isliye agar ham old_student prr clear() method lagayenge toh new_student bhi clear ho jayega. 

# - Ex : 

# old_student = { 'karan' : 12000 , 'jesan' : 30000 , 'john' : 14000}

# new_student = old_student 

# print(new_student)   # output : {'karan': 12000, 'jesan': 30000, 'john': 14000}
# print(id(new_student))  # output : 2694040473728

# print(old_student)   # output : {'karan': 12000, 'jesan': 30000, 'john': 14000}
# print(id(old_student)) # output : 2694040473728







# _______________________________________________________________________________________________________________________ 


# :: Iteration on dictionary : 

# - Using for loop.
# - Ex: 

# student = {'raj' : 10000 , 'jay' : 12000 , 'shantanu' : 14000}

# for item in student:
#     print(item , student[item], sep = ' : ')
    
# output : 
# raj : 10000
# jay : 12000
# shantanu : 14000















# :--> Assignment dictionary Question :   ( my approach )

# Question : we have given a thre dictionary containing marks and subject name of the three students jay , raj , shantanu. we have to calculate the total percentage of three students and add it into an list and display it.

# jay = {
#     'java' : 80,
#     'python' : 100,
#     'OOP' : 91 ,
#     'Computer Networks': 80
# }

# raj = {
#     'java' : 78,
#     'python' : 96,
#     'OOP' : 94 ,
#     'Computer Networks': 88
# }

# shantanu = {
#     'java' : 85,
#     'python' : 98,
#     'OOP' : 97 ,
#     'Computer Networks': 80
# }


# jay_percentage = (jay['java'] + jay['python'] + jay['OOP'] + jay['Computer Networks'] ) / 400  * 100

# # print(jay_percentage , "%")


# raj_percentage = (raj['java'] + raj['python'] + raj['OOP'] + raj['Computer Networks'] ) / 400  * 100

# # print(jay_percentage , "%")



# shantanu_percentage = (shantanu['java'] + shantanu['python'] + shantanu['OOP'] + jay['Computer Networks'] ) / 400  * 100

# print(jay_percentage , "%")
# print(raj_percentage , "%")
# print(shantanu_percentage , "%")



# students_results = [jay_percentage , raj_percentage , shantanu_percentage]

# print(students_results)














# :--> Assignment dictionary Question :   ( Actual method )



# Question : we have given a thre dictionary containing marks and subject name of the three students jay , raj , shantanu. we have to calculate the total percentage of three students and add it into an list and display it.



# jay = {
#     'java' : 80,
#     'python' : 100,
#     'OOP' : 91 ,
#     'Computer Networks': 80
# }

# raj = {
#     'java' : 78,
#     'python' : 96,
#     'OOP' : 94 ,
#     'Computer Networks': 88
# }

# shantanu = {
#     'java' : 85,
#     'python' : 98,
#     'OOP' : 97 ,
#     'Computer Networks': 80
# }



# marks = []

# student_list = [jay , raj , shantanu]

# for student in student_list:
#     sum1 = 0
#     for item in student:
#         sum1 = sum1 + student[item]
        
#     percentage = sum1 / len(student)
#     marks.append(percentage)
    
# print(marks)   # output : [87.75, 89.0, 90.0]






# _______________________________________________________________________________________________________________________ 



# :: Zipping and unzipping in Python using zip() Function : 

# -  zip() function used for aggregates elements from two or more iterables. 
# -  You can map elements from two or more containers using index. 
# - iterable can be list , set , tuple , dict.
# -  Syntax :  zip(iterable1 , iterable2 , iterable3 .....)

# NOTE: zip() function can give output only once and we can consume the output of zip function at once. 


# :--> Uses of zip() function :-

# 1.) For data aggregation and mapping elements. 
# 2.) Parallel iterations. 
# 3.) Creating dictionaries. 





# - Ex : 

# students = ['Rohan' , 'Shantanu' , 'Raj' , 'Sneha']
# roll = [101 , 102  , 103, 104]
# marks = [90 , 88 , 87 , 91]

# zipped_object = zip(students  , roll , marks)

# for element in zipped_object:
#     print(element) 
# # output : 
# # ('Rohan', 101, 90)
# # ('Shantanu', 102, 88)
# # ('Raj', 103, 87)
# # ('Sneha', 104, 91)

# print(zip(students , roll))  # output : <zip object at 0x00000257D088E5C0>






# - Ex :




# students = ['Rohan' , 'Shantanu' , 'Raj' , 'Sneha']
# roll = {101 , 102  , 103, 104}
# marks = (90 , 88 , 87 , 91)

# zipped_object = zip(students  , roll , marks)

# for element in zipped_object:
#     print(element) 
# # output : 
# # ('Rohan', 101, 90)
# # ('Shantanu', 102, 88)
# # ('Raj', 103, 87)
# # ('Sneha', 104, 91)

# print(zip(students , roll))  # output : <zip object at 0x00000257D088E5C0>





# - Ex :  parallel iteration using zip() function 



# students = ['Rohan' , 'Shantanu' , 'Raj' , 'Sneha']
# roll = [101 , 102  , 103, 104]


# zipped_object = zip(students , roll)

# for name , roll in zipped_object:
#     print(name , roll , sep = ':')
    
# output : 
# Rohan:101
# Shantanu:102
# Raj:103
# Sneha:104












# - Ex : dictionary creation 



# students = ['Rohan' , 'Shantanu' , 'Raj' , 'Sneha']
# roll = [101 , 102  , 103, 104]


# zipped_object = zip(students , roll)


# print(dict(zipped_object)) # output : {'Rohan': 101, 'Shantanu': 102, 'Raj': 103, 'Sneha': 104}



# NOTE:  for dictionary creation only take two iteration 



# students = ['Rohan' , 'Shantanu' , 'Raj' , 'Sneha']
# roll = [101 , 102  , 103, 104]
# xyz = [1]

# zipped_object = zip(students , roll, xyz)


# print(dict(zipped_object)) # output : print(dict(zipped_object)) # output :
#           ^^^^^^^^^^^^^^^^^^^
# ValueError: dictionary update sequence element #0 has length 3; 2 is required











# - Ex : unzipping using zip() function. 



# students = ['Rohan' , 'Shantanu' , 'Raj' , 'Sneha']
# roll = [101 , 102  , 103, 104]


# zipped_object = zip(students , roll)

# result_unzip = list(zipped_object)

# abc , xyz = zip(*result_unzip)
# print(abc)  # output: ('Rohan', 'Shantanu', 'Raj', 'Sneha')
# print(xyz)  # output: (101, 102, 103, 104)






# _______________________________________________________________________________________________________________________ 



# :: View objects of dictionary : 

# - Three views we can create :- 


# 1.) view of keys :- using keys() method. 
# 2.) view of values :- using values() method. 
# 3.) view of key-value pairs :- using items() method. 













# 1.) view of keys using keys() method :
# - Python Keys() method is used to fetch all the keys from the dictionary. 
# - There are no parameters. 
# - Syntax : dict.keys()


# - Ex : 


# fees = {'karan' : 12000 , 'jeson' : 30000 , 'john' : 14000}
# keys_view = fees.keys()
# print(keys_view)  # output : dict_keys(['karan', 'jeson', 'john'])

# print(type(keys_view)) # output : <class 'dict_keys'>



# - Ex : Fetching into an list



# fees = {'karan' : 12000 , 'jeson' : 30000 , 'john' : 14000}
# keys_view = list(fees.keys())

# print(keys_view)  # output : ['karan', 'jeson', 'john']
# print(type(keys_view)) # output : <class 'list'>






# - Ex : Actual implementation 

# fees = {'karan' : 12000 , 'jeson' : 13000 , 'john' : 14000}
# act_fees = 15000 
# keys_list = list(fees.keys())

# for key in keys_list:
#     print(f" student {key} has got discount of rs :" , act_fees - fees[key])



# output :
#  student karan has got discount of rs : 3000
#  student jeson has got discount of rs : 2000
#  student john has got discount of rs : 1000















# 2. view of values using values() method :
# - Python values() method is used to fetch all the values from the dictionary. 
# - There are no parameters. 
# - Syntax : dict.values()



# - Ex : 


# fees = {'karan' : 12000 , 'jeson' : 13000 , 'john' : 14000}
# fees_list = list(fees.values())

# print(fees_list)  # output : [12000, 13000, 14000]
# print(type(fees_list))  # output :  <class 'list'>




# - Ex : 

# my_cart = { 'mobile' : 14000 , 'earphone' : 1500 , 'watch' : 4000 , 'laptop' : 60000}

# price_cart = list(fees.values())

# print(f"total amount to pay for your cart : {sum(price_cart)}") # output : total amount to pay for your cart : 39000













# 3.) view of key-value pairs using items() method : 
# - In Python Dictionary ,  items() method is used to return the list with all dictionary keys with value. 
# - There is no parameters. 
# - Syntax : dict.items()


# - Ex : 



# fees = {'karan' : 12000 , 'jeson' : 30000 , 'john' : 14000}
# print('dictionary items are :')

# fees_view = list(fees.items()) 
# print(fees_view)  # output : [('karan', 12000), ('jeson', 30000), ('john', 14000)]

# print(type(fees_view))  # output :   <class 'list'>






# - Ex : 


# fees = {'karan' : 12000 , 'jeson' : 30000 , 'john' : 14000}
# print('dictionary items are :')

# fees_view = list(fees.items()) 



# for element in fees_view:
#     print(f"student {element[0]} has fees {element[1]}")
    
# output :
    
# student karan has fees 12000
# student jeson has fees 30000
# student john has fees 14000









# :: Youtube Playlist Content : 

# --> lecture-101 : Dictionary in Python.
# --> lecture-102 : Length of Dictionary. 
# --> lecture-103 : Accessing Dictionary items in Python. 
# --> lecture-104 : modifying Dictionary items. 
# --> lecture-105 : Access items using get(). 


# _______________________________________________________________________________________________________________________ 



# :: Dictionary in Python : 
# - Python dictionary is an unordered collection of key-value pairs. 
# - Ex :

# emp_data = { 'name' : 'jay' , 'age' : 21 , 'salary'  : 18000 }

# print(emp_data)









# :--> Creating dictionary :
# - There are basically two ways :


# 1.) Using curly braces :- 
# - Ex : 

# dict_name = { key1 : val1 , key2 : val2 , key3 : val3 }





# 2.) Using dict() function :-
# - Ex : 

# dict_name = dict([ (key1 , val1) ,(key2 , val2) , (key3 , val3) ])
# print(dict_name) 









# :--> Characteristics of dictionary :


# 1.) Keys must be immutable items( string , tuple .... etc) , list as a key is not allowed. 

# - Ex : 

# student = { [1,2,3]:'hello' , 'name' : 'anubhav'}
# print(student)   # output :     student = { [1,2,3]:'hello' , 'name' : 'anubhav'}
#               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'




# 2.)  Values can be any datatype. 


# 3.) duplicates of key is not allowed. 

# - Ex : 

# employee = {'salary' : 10000 , 'name' : 'ram' , 'salary' : 12000}
# print(employee)  # output : {'salary': 12000, 'name': 'ram'}




# 4.) Dictionary is mutable. 


# 5.) empty dictionary : 
# - Ex : 

# student = {}
# print(student)  # output : {}
# print(type(student))  # output : <class 'dict'>







# _______________________________________________________________________________________________________________________ 


# :: NOTE :-

# 1.) dictionary is unordered. 



# 2.) Keys can't be duplicated but values can be duplicated. 

# - Ex : 

# employee  = { 'suraj' : 12000 , 'karan' : 70000 , 'suraj'  : 70000}

# print(employee)  # output : {'suraj': 70000, 'karan': 70000}





# 3.) Keys are case-sensitive. 

# - Ex :  

# employee  = { 'suraj' : 12000 , 'karan' : 70000 , 'Suraj'  : 70000}

# print(employee)  # output : {'suraj': 12000, 'karan': 70000, 'Suraj': 70000}












# :--> Length of dictionary : 

# 1.) by len() function : 
# - Ex : 

# employee  = { 'suraj' : 12000 , 'karan' : 70000 , 'Suraj'  : 70000}
# print(len(employee))  # output : 3



# 2.) by manually : 
# - Ex : 


# employee  = { 'suraj' : 12000 , 'karan' : 70000 , 'Suraj'  : 70000}
# count = 0
# for key in employee:
#     count+=1

# print(count)  # output : 3






# _______________________________________________________________________________________________________________________ 





# :: Accessing the item of dictionary : 

# - We can't use indexing and slicing on dictionary. 
# - Syntax :  dict_name[key]

# - Ex:  


# employee  = { 'suraj' : 12000 , 'karan' : 70000 , 'Suraj'  : 70000}
# print(employee['karan'])  # output : 70000




# - Ex : 

# employee  = { 'suraj' : 12000 , 'karan' : 70000 , 'suraj'  : 70000}

# print(employee['suraj']) # output : 70000







# _______________________________________________________________________________________________________________________ 




# ::  How to modify dictionary : 

# - Dictionary is mutable. 
# - We can modify value using following syntax : dict_name[key] = new_value 





# - Ex : 

# fees = { 'sachin' : 20000 , 'virat' : 19000 , 'saurav' : 21000}
# print("before modification : ", fees)  # output : before modification :  {'sachin': 20000, 'virat': 19000, 'saurav': 21000}
# print(id(fees))   # output : 1847496495232


# fees['virat'] = 22000

# print("after modidfication : ", fees)  # output : after modidfication :  {'sachin': 20000, 'virat': 22000, 'saurav': 21000}   
# print(id(fees))  # output : 1847496495232







# - Ex: 
 
# - agar key is not present then a new key is generated of same given name and a value is assign to that key. 



# fees = { 'sachin' : 20000 , 'virat' : 19000 , 'saurav' : 21000}
# print("before modification : ", fees)  # output : before modification :  {'sachin': 20000, 'virat': 19000, 'saurav': 21000}
# print(id(fees))   # output : 1847496495232



# fees['dhoni'] = 22000

# print("after modidfication : ", fees)  # output : after modidfication :  {'sachin': 20000, 'virat': 19000, 'saurav': 21000, 'dhoni': 22000} 
# print(id(fees))  # output : 1847496495232






# _______________________________________________________________________________________________________________________ 



# :: Access items using get() method : 

# - This method returns the value of specified key. 
# - If key not found , default value is printed. 
# - Syntax : dict_name.get(key , default_value)

# - Ex : 

# Employee = { 'name'  : 'raj' , 'age' : 22 , 'salary' : 50000}
# print(Employee.get('salary' , 'not found'))

# print('100 statements')


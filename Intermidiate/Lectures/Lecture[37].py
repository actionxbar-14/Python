

# :: Youtube Playlist Content : 

# --> lecture-186 : if __name__ == '__main__ | __main__ Usase in Python.
# --> lecture-187 : 5 - Common mistakes in Python. 
# --> lecture-188 : Python Interview Questions. 
# --> lecture-189 : Revision. 
# --> lecture-190 : Revision. 


# _____________________________________________________________________________________________________________________________________________________




# :: __main__ Usase in Python : 
# - imported code / script dusre file mai directly execute ho jati hai uss file ko run krne prr , jab ham imported code /script ko file run krne prr execute nahi krna chahte hai tb ham __main__ ka use krte hai
# - jab hame particular code/script ko uski parent file mai hi execute karana ho tbb bhii ham __main__ ka use krte hai. 
# - if we want to access the code that is written under __main__ then we have to give refrence like :

# - Ex :

# import name_main


# print(name_main1.add(2,5))


# NOTE: --> Go to module_practice to check the exact implimentation.





# :--> Why we use it :

# - if __name__ == "main" : is used to execute some code only if the file was run directly , and not imported. 
# - To keep information which code is executing. 








# _____________________________________________________________________________________________________________________________________________________





# :: 5 - Common mistakes in Python : 




# :--> mistake_1 : naming python files with built-in names. 












# :--> mistake_2 : Over_riding imported contents. 


# - Ex : 


# from math import sqrt 

# sqrt = sqrt(25)

# print(sqrt)  # output :  5.0


# print(sqrt(49))  # output :     print(sqrt(49))
#           ^^^^^^^^
# TypeError: 'float' object is not callable

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# :--> mistake_3 : Problem of default argument. 
# - jab bhi ham default value ko use krte hai toh default value ko first time hi use kiya jata hai , subsequent calls mai default value jaise jaise modify hoga uska modified version use kiya jayega.

# - Ex : 

# students = ['karan' , 'arjun']

# def add_students(name , students):
#     students.append(name)
#     print(students)
    
    
# add_students("Thakur" , students)  # output : ['karan', 'arjun', 'Thakur']
    
    
    
# - Ex : assigning default value

# students = ['karan' , 'arjun']

# def add_students(name , students = []):
#     students.append(name)
#     print(students)
    
    
# add_students("Thakur")  # output : ['Thakur']

# add_students("Jay" )   # output : ['Thakur', 'Jay']

# add_students("anubhav")  # output : ['Thakur', 'Jay', 'anubhav']
    
    
    
    
# - Ex : without default value

# import time 

# from datetime import datetime 

# def display_time():
#     time = datetime.now()
#     print(time)
    

# display_time()
# time.sleep(5)
# display_time()

    
    
# - Ex : with default value  


# import time 
# from datetime import datetime 

# def display_time(time = datetime.now()):
#     print(time)
    
    

# display_time()  # output : 2026-06-04 20:04:39.002124
# time.sleep(5)
# display_time()  # output : 2026-06-04 20:04:39.002124
# display_time()  # output : 2026-06-04 20:04:39.002124

















# :--> mistake_4 :  mistakes while using higher order functions. 

# - Ex : 

# data = [89 , 90 , 56 ,67 ,82 ,87]

# def logic(ele):
#     if ele % 2 == 0:
#         return True 
    

# filtered_object = filter(logic , data)

# print(filtered_object)  # output : <filter object at 0x000001A7AF6EAB60>


# print(list(filtered_object))# output : [90, 56, 82]
 
 
# for ele in filtered_object:
#     print(ele)    #--> ye output isliye nahi diye kyuki higher order function(filter , map , zip) unka output ak hi bar print hota hai .
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# :--> mistake_5 : mistake while copying the data. 


# - Ex : 

# data = [10 , 20 , [1,2,3]]

# data_copy = data

# print(data) # output :  [10, 20, [1, 2, 3]]
# print(data_copy) # output :  [10, 20, [1, 2, 3]]



# data_copy[1] = "shantanu"


# print(data) # output :   [10, 'shantanu', [1, 2, 3]]
# print(data_copy) # output :   [10, 'shantanu', [1, 2, 3]]





# - Ex : rightway_1 of copying data  ( shallow copy ) 



# import copy
# data = [10 , 20 , [1,2,3]]

# data_copy = copy.copy(data)

# print(data) # output :  [10, 20, [1, 2, 3]]
# print(data_copy) # output :  [10, 20, [1, 2, 3]]



# data_copy[1] = "shantanu"


# print(data) # output :   [10, 'shantanu', [1, 2, 3]]
# print(data_copy) # output :   [10, 'shantanu', [1, 2, 3]]









# NOTE : shallow copy nested element ke liye dhang se copy nahi krr pata , isliye ham nested datasets ke liye deep copy ka use krte hai.


# - Ex : shallow copy


# import copy
# data = [10 , 20 , [1,2,3]]

# data_copy = copy.copy(data)

# print(data) # output :  [10, 20, [1, 2, 3]]
# print(data_copy) # output :  [10, 20, [1, 2, 3]]



# data_copy[2][1] = "shantanu"


# print(data)      # output :  [10, 20, [1, 'shantanu', 3]]
# print(data_copy) # output :  [10, 20, [1, 'shantanu', 3]]





# - Ex : deep copy  



# import copy
# data = [10 , 20 , [1,2,3]]

# data_copy = copy.deepcopy(data)

# print(data) # output :  [10, 20, [1, 2, 3]]
# print(data_copy) # output :  [10, 20, [1, 2, 3]]



# data_copy[2][1] = "shantanu"


# print(data)      # output :  [10, 20, [1, 2, 3]]
# print(data_copy) # output :  [10, 20, [1, 'shantanu', 3]]











# _____________________________________________________________________________________________________________________________________________________




# :: Python Interview Question : 

# - Question : write a Python Program for following requirements : 

# --> If inputs 2 and 512 then ,
# --> output : 8

# Explanation : 2 * 2 = 4 ,  4 * 2 = 8 ,  8 * 2 = 16 ,  16 * 2 = 32 ,  32 * 2 = 64 ,   64 * 2 = 128 ,  128 * 2 = 256 ,  256 * 2 = 512. 

# --> result = 512
# --> count = 8 



# Answer :  

# var = input("Input :")

# var = var.split()

# num1 , num2 = var 

# result = 2
# count = 0

# while True:
#    result = result * 2
#    count += 1
#    if result == int(num2):
#        break 
   
# print(count)
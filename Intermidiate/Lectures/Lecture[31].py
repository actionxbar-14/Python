
# :: Youtube Playlist Content : 

# --> lecture-156 : Lambda with 'if-elif-else' & List Comprehension Python.
# --> lecture-157 : Implementing IIFE Function in Python. 
# --> lecture-158 : First class Function in Python. 
# --> lecture-159 : Function as parameter / Arguments. 
# --> lecture-160 : Returning Function from Function.


# _______________________________________________________________________________________________________________________ 


# :: Python Lambda Function with if-else :- 



# :-> short-hand if else : 

# - Ex : 

# num1 = 10 
# num2 = 20 

# if num1 >= num2:
#     print(num1)
# else:
#     print(num2)
    
# print(10 if num1 >= num2 else 20)  # output : 20





# :--> Lambda Function with if-else: 

# - Ex :

# num1 = 10 
# num2 = 20 

# max1 = lambda n1 , n2 : n1 if n1>=n2 else n2 
# print(max1(num1 , num2))  # output : 20





# :--> using List comprehension with lambda function :

# Ex: 

# nums = [3 , 5 ,6 ,7]
# squares = lambda date: [i*i for i in nums]
# print(squares(nums))  # output : [9, 25, 36, 49]



# _______________________________________________________________________________________________________________________ 


# :: Implementing IIFE Function in Python :
# - IIFE : Immediately Invoked Function Expression
# - Kisi bhi function ko only one time execute krne ke liye iska use hota hai
# - function ka defination and call ak sath hota hai.

# -> In Javascript :  
# - Ex : 

# (function(a , b){
#     var result = a + b;
#     console.log(result);
    
# }) (5,7);  # output :- 12




# -> In Python : we can implement IIFE Function using Lambda Function. 

# - Ex :  

# result = (lambda a, b : a + b) (5,7)

# print(result)  # output : 12


# - Ex : 

# result = (lambda num : num + 1)(int(input("Enter the num :")))
# print(result)



# _______________________________________________________________________________________________________________________ 




# :: First class Function/objects in Python :


# :--> First class Function/objects in Programming :-

# - They are instance of some class. 
# - They can be stored in data structures. 
# - They can be assigned to variabels. 
# - They can perform operations on these objects. 
# - They can be passed as arguments to functions.
# - They can be returned as values from functions. 







# _______________________________________________________________________________________________________________________ 

# NOTE : 
# - We can pass any valid Python object as an argument to the function. 
# - Since, functions are valid Python objects so we can pass Function as parameter / arguments. 



# :: Function as parameter / Arguments :

# - Ex : 

# def get_name():
#     nm = input("Enter the first name :")
#     last_nm = input("Enter the last name : ")
#     return nm + " "+ last_nm   

# def display(func):
#     print(func())

# display(get_name)




# _______________________________________________________________________________________________________________________ 




# :: Returning Function from Function : 


# - Ex :

# def display():
#     print("hello")
#     def printer():
#         print("Welcome!")
#     return printer  #--> display() function inner function printer() ke output ko return krega. 

# display()  # output : hello  









# :: Youtube Playlist Content : 

# --> lecture-141 : Function in Python.
# --> lecture-142 : Scope in functional programming. 
# --> lecture-143 : Global Variables in Python. 
# --> lecture-144 : Everything About Global keyword. 
# --> lecture-145 : return statement.


# _______________________________________________________________________________________________________________________ 


#NOTE : Problems with Procedural Programming approach :-
# - Procedural Programming mai ham code ko resuse krne ke liye uss same logic ko baar baar likhte hai jisse :

# 1.) Large size of Program and less efficiency. 
# 2.) Difficulty in code management. 
# 3.) You can't migrate code to other project. 
# 4.) Problems when requirement increased. 

# - To solve these Problems we use Functional Programming and Object Oriented Programming. 






# :: What is a Function : 

# - Function is an organized block of resuable code. 
# - Functions can be called any number of times. 
# - Function contains a set of instructions which perform specific tasks. Ex : addition in above example.  




# :--> Other reasons of using functions :

# 1.) Testing and Debugging :- 
# - Functions make it easier to test and debug specific parts of your code. 
# - You can isolate and focus on individual functions without dealing with the entire program's complexity. 
# - In testing , we can debug individual components. 


# 2.) Improved readability .

# 3.) Efficient code management . 

# 4.) Functional Programming Provides concepts like recursion , higher order functions , decorators which are helpful for solving complex problems using programming. 










# :--> Types of Functions :
# - There are two types of functions:- 

# 1.) Built-in Functions. 
# 2.) User-defined. 



# NOTE : Parameter's in the User-defined functions are optional and they are enclosed in the square brackets , 
# and anything which is enclosed in square brackets in Functions are optional . 





# :--> Calculation of Simple Interest : 

# def simple_interest(p , n , r):
#     print("Principle amount is :", p)
#     print("number of years is :", n)
#     print("Rate of Interest is :", r)
#     si = (p*n*r)/100
    
#     print("Simple interest is  : ", si)
    
    
# simple_interest(2,5 ,7)  # output : Simple interest is  :  0.7












# _______________________________________________________________________________________________________________________ 



# :: Scope in Functional Programming : 
# - In Programming , the term "scope" refers to the region of the code where an identifier can be accessed. 



# :: What is an identifier : 
# - an identifier is a name using which we can identify a particular object. Objects can ve variable, function name , class name etc. 

# - In Functional Programming, there are four types of identifiers. 

# 1.) Local identifiers 
# 2.) Global identifiers 
# 3.) Non-local identifiers 
# 4.) Built-in identifiers 





# 1.) Local identifiers :- 

# - Jo bhi identifiers ham function ke ander banate hai , unhe ham kahte hai Local identifiers. 
# - Variables defined inside the function are called local variables. 
# - Scope : local to the function. 

# - Ex : 

# def display(name):
#     age = 22    # age is local identifier [ local variables ]
#     print(f'{name} has age {age}')
#     print(age) 
    
# display("shantanu")  

# print(age)   # output :    print(age)
#           ^^^
# NameError: name 'age' is not defined
    
    
    
    
    
    
# NOTE : locals() function is used to list out all the local variables in the scope. It returs a dictionary of locals variables and there assign values. 

# - Ex  

# def display(name):
#     age = 22    # age is local identifier [ local variables ]
#     print(f'{name} has age {age}')
#     print(locals())  # output : {'name': 'shantanu', 'age': 22}
#     local_variables = print(len(locals())) 
#     print(local_variables)  # output : 2 
#     print(age)  # output : 22
    
# display("shantanu")  





# - Ex: Checkin if a local variable present in the given scope of function or not. 



    
# def display(name):
    
#     x = 20 
#     local_variable = locals()
#     print(local_variable['x'])  # output : 20
      
# display("shantanu")  


# print('-' * 50)
    
    
    
# def display(name):
    
#     # x = 20 
#     local_variable = locals()
#     print(local_variable['x'])  # output : 20
      
# display("shantanu")   # output :    print(local_variable['x'])  # output : 20
#           ~~~~~~~~~~~~~~^^^^^
# KeyError: 'x'
  

    


# _______________________________________________________________________________________________________________________ 




# 1.) Global identifiers :- 

# - Jo bhi identifiers ham function or class/block ke bahar banate hai , unhe ham kahte hai Global identifiers. 
# - Variables defined Outside the function and class/blocl are called Global variables. 
# - Scope : global to the Program after the decleration of varibale/identifier. 



# - Ex : 

# country = 'india'    # global variable 

# def display():
#     name = 'jay'     # local variable
#     print(name)
    
    
# display() 


# NOTE : We can access global variable anywhere in the program is not completely true. 


# NOTE : What if we have same local and global variable :

# num = 10    # global variable 

# def display():
#     num = 20 # local variable 
#     print("Inside :" , num)
    
# display()
# print("Outside :", num)


# output  :
# Inside : 20
# Outside : 10




# NOTE : globals() function is used to print all the global function present in thr program and it retuns an dictionary of global variables. and we can use this function anywere in the program. 

# - Ex : 

# name = 'shantanu'   # global variable

# def display():
#     age = 22 # local variable 
#     # print(globals())
    
# display()
# print(globals())  # output : {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001F80DD65490>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\hp\\OneDrive\\Desktop\\Python\\Intermidiate\\Lectures\\Lecture[28].py', '__cached__': None, 'name': 'shantanu', 'display': <function display at 0x000001F80DF19940>}








# _______________________________________________________________________________________________________________________ 



# NOTE : When we try to manipulate the global variable inside the block and function where it is globaly accessed then interpreter gives unboundLocalError. 

# num = 10   # global variable

# def display():
#     num = num + 5    # --> UnboundLocalError
#     num = 20   # local variable
#     print('Inside :', num)
    
# display()
# print("Outside :", num)

# output :    num = num + 5
#           ^^^
# UnboundLocalError: cannot access local variable 'num' where it is not associated with a value









# :--> How to resolve UnboundLocalError : 

# - By using global keyword. 

# - Ex : 


# num = 10   # global variable

# def display():
#     global num
#     num = num + 5    # --> UnboundLocalError
#     # num = 20   # local variable
#     print('Inside :', num)
    
# display()
# print("Outside :", num)

# output :  

# Inside : 15
# Outside : 15










# _______________________________________________________________________________________________________________________ 




# :: return statements : 

# - return statement is used to print the statement which is given as output by the function of block.  

# NOTE: 

# 1.) any code written after return statement does not execute. 

# - Ex : 

# name = "anubhav"

# def display():
#     return name
#     print(name)  # no exection
    

# result = display()
# print(result)  # output : anubhav







# 2.) You can return any type of python object. 

# - Ex :  

# def display():
#     return 'shantanu'

# print(display())  # output : shantanu



# - Ex : 

# def display():
#     return [19 , 10.2 , "shantanu"]

# print(display())  # output : [19, 10.2, 'shantanu']






# 3.) You can return multiple values , but return statement return as an tuple : 

# - Ex:  

# def calci(a,b):
#     add = a + b
#     sub = a - b
    
#     return add , sub


# result = calci(10 ,20)
# print(result)   # output : (30, -10)

# # :--> punpacking :

# n1 , n2 = calci(10 ,20)

# print(f"n1 : {n1} , n2 : {n2}")  # output :- n1 : 30 , n2 : -10






# 4.) You can use return keyword to stop execution of function. 

# - Ex : 


# def calci( a , b):
#     if a < 0: 
#         print("if exection end")  #-->  yaha pr agar a negative hua toh function execution end ho jayega
#         return
#     add = a + b
#     sub = a - b
#     return add , 10.3
#     print("shantanu")
    
    
# calci(10 , 20)


# 5.) Default return type is None. 

# - Ex : 

# def display():
#     print("hello world")
    
# print(None)
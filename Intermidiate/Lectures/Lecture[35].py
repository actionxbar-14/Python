
# :: Youtube Playlist Content : 

# --> lecture-176 : Decorators in Python.
# --> lecture-177 : Multiple decorators in Python. 
# --> lecture-178 : Decorator Examples in Python. 
# --> lecture-179 : Smart Division Using Decorator. 
# --> lecture-180 : globals() in Python. 


# _________________________________________________________________________________________________________________________________________________________________


 
 
# :: Decorators in Python : 
# - Functions which takes other functions as input , add additional functionalities and returns it. 
# - It is a callable Python object which modifies other functions/class. 

# - Ex :  syntax_1

# def decor(func):
#     def inner():
#         func()  #--> existing functionality 
#         print("Welcome!")
#     return inner 
   


# def printer():
#     print("Welcome!")
#     print("Welcome!")
    
    
# printer = decor(printer)
# printer()




# - Ex :  syntax_2

# def decor(func):
#     def inner():
#         func()  #--> existing functionality 
#         print("Welcome!")
#     return inner 
   
# @decor

# def printer():
#     print("Welcome!")
#     print("Welcome!")
    
    
# printer()




# - Ex :  implementation


# def decor(addition):
#     def inner():
#         result = addition()
#         num3 = int(input("Enter num3 :"))
        
#         result += num3 
        
#         print(result)
        
#     return inner
    


# @decor  
    
    
# def addition():
#     num1 = int(input("Enter num1 :"))
#     num2 = int(input("Enter num2 :"))
    
#     result = num1 + num2 
    
#     return result 



# addition()









# _________________________________________________________________________________________________________________________________________________________________




# :: Multiple decorators On One Function in Python : 


# - Ex : syntax_1

# def decor1(func):
#     def inner():
#         return func().upper()
        
#     return inner




# def decor2(func):
#     def inner():
#         return func().split()
        
#     return inner
       
    

# def get_name():
#     name = input("Enter first name :")
#     sur_name = input("Enter surname :")
#     full_name  = name + " " + sur_name 
#     return full_name 



# get_name = decor2(decor1(get_name))

# print(get_name())
















# # - Ex : syntax_2

# def decor1(func):
#     def inner():
#         return func().upper()
        
#     return inner




# def decor2(func):
#     def inner():
#         return func().split()
        
#     return inner
       
# @decor1
# @decor2   

# def get_name():
#     name = input("Enter first name :")
#     sur_name = input("Enter surname :")
#     full_name  = name + " " + sur_name 
#     return full_name 



# print(get_name())








# _________________________________________________________________________________________________________________________________________________________________




# :: One decorators On multiple functions in Python : 

# - Ex : 


# def decor(func):
#     def inner(*args):    #_-> (0 ,10 ,5)
#         for num in args[1:]:
#             if num == 0:
#                 return "can't divide by zero"
            
#         return func(*args)      
#     return inner 





# @decor
# def div1(a ,b):
#     return a/b 

# @decor
# def div2(a , b , c):
#     return a/b/c 



# print(div1(10 , 5))  #--> 2.0
# print(div1(10 , 0))  #--> can't divide by zero
# print(div2(0 , 10 , 5))  #--> 0.0






# _________________________________________________________________________________________________________________________________________________________________




# :: Smart Division Using Decorator : 


# def smart_divider(func):
#     def inner(num1 , num2):
#         if num2 == 0:
#             print("can't divide by zero")
#             return 
        
#         func(num1 , num2)
    
#     return inner

# @smart_divider
# def Division(num1 , num2):
#     print("Division is :" , num1/num2)

  
# Division(10 , 0)

# print("other program runs even if zerodivision error comes!!")




# _________________________________________________________________________________________________________________________________________________________________




# :: globals() and locals() in Python : 


# --> Symbol table :-
# - It is a data structure which contains all necessary information about global scope of the program. 
# - This symbol table is accessed using globals() function. 



# --> Globals()  and locals() Function :- 
# - globals() function returns a dictionary of current global symbol table. 
# - locals() function returns a dictionary of current global symbol table. 
# - Syntax : globals() / locals()

# - Ex :   globals()

# a = 10 


# def demo():
#     print("hello")
#     globals()['a'] = 200   #--> changin the value of variable assigned globaly.

       
# print(globals())  # output : {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000015F89065690>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\hp\\OneDrive\\Desktop\\Python\\Intermidiate\\Lectures\\Lecture[35].py', '__cached__': None, 'a': 10, 'demo': <function demo at 0x0000015F891F99E0>}


# print(globals()['a'])  # output : 10 





# - Ex :  locals()

# a = 10 


# def demo():
#     b = 20
#     print("hello")
#     locals()['b'] = 200 #--> assigning the value of variable that is locally identified.

       
# print(globals())  # output : {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000015F89065690>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\hp\\OneDrive\\Desktop\\Python\\Intermidiate\\Lectures\\Lecture[35].py', '__cached__': None, 'a': 10, 'demo': <function demo at 0x0000015F891F99E0>}


# print(globals()['b'])  # output : 20 







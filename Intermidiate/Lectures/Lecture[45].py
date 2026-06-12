
# :: Youtube Playlist Content : 

# --> lecture-226 : OOPS-36.
# --> lecture-227 : OOPS-37. 
# --> lecture-228 : OOPS-38. 
# --> lecture-229 : OOPS-39. 
# --> lecture-230 : OOPS-40. 


# _____________________________________________________________________________________________________________________________________




# :: Types of decorators : 
 

# 1.) Function decorator
# 2.) Class decorator 




# 2.) -->  class Decorator : 

# - class decorator inculedes the use of callable methods ,  agar kisi class ke ander callable method hai toh uss class ke objects ko ham call krr skte hai. 

# - Ex : 

# class Decorator(object):
#     def __init__(self , func):
#         self.function = func

#     def __call__(self , a , b):     #--> __Call__ magic method is responsible for takinf obj as callable method. 
#         result =  self.function(a , b) # original functnality
#         return result ** 2 # square (additional functnality) 



# @Decorator
# def add(a , b):
#     return a + b

# print(add(1 , 2))   #-->  9    [  add.__call__(a , b)  ]














# :-->  Explanation : 




# 1. Class Decorator ka concept :

# Python mein agar kisi class ke andar __call__ method define ho, toh us class ke objects ko function ki tarah call kar sakte ho. Matlab object ko () ke saath use karoge toh __call__ method execute hoga.








# 2. Code Explanation :


# class Decorator(object):

#     def __init__(self , func):
#         self.function = func   # yeh original function ko store kar raha hai


#     def __call__(self , a , b):   # jab object ko call karenge toh yeh chalega
#         result = self.function(a , b)   # original function ko call kiya
#         return result ** 2              # aur uske result ka square return kiya



# __init__: jab decorator banega, usme original function (add) store ho jayega.

# __call__: jab object ko call karenge, toh pehle original function execute hoga, phir uske result ka square return hoga.








# 3. Decorator ka use : 




# @Decorator
# def add(a , b):
#     return a + b
# Yeh line ka matlab hai: add = Decorator(add)

# Matlab add ab ek Decorator class ka object ban gaya hai, jisme original add function store hai.








# 4. Execution :



# print(add(1 , 2))
# Jab add(1,2) call karte ho, toh actually Decorator class ka __call__ method run hota hai.

# self.function(a,b) → add(1,2) → 3

# return result ** 2 → 3 ** 2 = 9

# Output: 9






# 5. Summary :



# __call__ method ek object ko function ki tarah callable banata hai.

# Decorator class original function ko wrap karta hai aur uske result par extra functionality add karta hai (yaha square).

# Isliye add(1,2) ka result 9 aaya, na ki 3.











# _____________________________________________________________________________________________________________________________________




# ::   Class Decorator Example : 

# - Ex : 


# def add(*args):
#     sum1 = 0 
#     for num in args:
#         sum1 = sum1 + num 
#     return sum1 


# print(add(10 , 20 ,30))


# print(add(10 , '20' , 30))   # output : print(add(10 , '20' , 30))
#           ~~~^^^^^^^^^^^^^^^^
#   File "c:\Users\ANUBHAV\Program_Folders\Python\Intermidiate\Lectures\Lecture[45].py", line 172, in add
#     sum1 = sum1 + num
#            ~~~~~^~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'





# NOTE :  we see that execution has stopped beacuse of unsupported operand , now we have to use class decorator to modify the function and make the program as simple as that it continue the flow of execution and just give an error and does not break the flow of execution. 

# - Ex : 



# class Decorator(object):
#     def __init__(self , func):
#         self.function = func

#     def __call__(self , *args):
#         try:
#             if any([isinstance(i , str) for i in args]):  #--> [False , True , False]
#                 raise TypeError("Cannot pass string as arguments")
#             else:
#                 self.function(*args)
#         except Exception as obj:
#             return obj

        



# @Decorator   # --> it is equal to  : add = Decorator()
# def add(*args):
#     sum1 = 0 
#     for num in args:
#         sum1 = sum1 + num 
#     return sum1 


# print(add(10 , 20 ,30))


# print(add(10 , '20' , 30))
# output : 
# None
# Cannot pass string as arguments
# None
# Cannot pass string as arguments


# add(10 , '20' , 30)    #--> add.__call__()















# _____________________________________________________________________________________________________________________________________







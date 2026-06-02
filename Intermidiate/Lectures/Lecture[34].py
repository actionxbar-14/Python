
# :: Youtube Playlist Content : 

# --> lecture-171 : fibonacci Series using Python.
# --> lecture-172 : Recursion v/s Iteration Which is better?. 
# --> lecture-173 : Namespace in Python. 
# --> lecture-174 : Non Local Variables / keyword in Python. 
# --> lecture-175 : Closure in Python. 


# ________________________________________________________________________________________________________________________________



# :: fiboonacii Series using Python Recursion :  

# num = int(input("Enter the value of num :"))

# def fibonacii(num):
#     if num == 1:
#         return 0  
#     if num == 2:
#         return 1
    
# for i in range(1 , num+1):
#     print(fibonacii(i))
    
    
    







# :: Advantages of Recursion :  

# 1. Recursive Programs are more elegant.  
# 2. Recursive Programs requires few lines.  







# ________________________________________________________________________________________________________________________________




# :: Recursion v/s Iteration Which is better : 




# :- Advantages of Using Recursione over Iteration :
# - Recursive Programs takes less no. of code written than iteration.


# - Ex : ( using Recursion )

# num = int(input("Enter num : "))

# def fact(n):
#     if n==0:
#         return 1
    
#     return n * fact(n-1)

# result_fact = fact(num)
# print(result_fact)
 
 
 
 
# - Ex :  ( using iteration )

# result = 1
# n = 4

# for i in range(n, 1 , -1):
#     result = result * i


# print(result)  # output : 24








# :- DisAdvantages of Using Recursione over Iteration :
 
# - Recursive Programs requires more space / space complexity than iterative programs. ( because of the stack calls during each function call). 
# - Iterative calls does not require the stack calls & space that's why it is more memory efficient. 



# NOTE : 

# - Time complexity is also a problem when multiple recursive calls. 
# --> For one recursive call:  big O(n)
# --> For two recursive call:  big O(2^n)
# --> For three recursive call:  big O(3^n)

# - Ex : (using recursion)

# def fact(n):
#     if n==0:
#         return 1
    
#     return n * fact(n-1)


# - Ex :  ( using iteration )

# result = 1 
# n = 4 

# for i in range(n , 1 , -1):
#     result  = result * i 
    

# print(result)







# NOTE :  

# --> Infinite recursion :- Crash the system.  
# --> Infinite iteration :- Stops the application.


# :-> USECASE SCENERIO : 

# - Recursive way :- Less & elegant code. 
# - Iterative way :- time & space complexity. 








# ________________________________________________________________________________________________________________________________



# :: Namespace in Python : 

# --> Names :
# - These are equivalent to the idetifiers. 
# - Names and identifiers are same things.
# Ex : 

# a = 20  # [ a is the names for this program ]

# print(id(20))  # output : 140708335576456
# print(id(a))   # output : 140708335576456



# --> Namespace : 
# - Namespace are nothing but just collection of names or identifiers. 
# - It looks like an mapping between names and their value , it contain property like an dictionary because it takes only unique Names(key) - Values(value) pairs. 
# - Ex : 

# a = 10 
# b = 20 
# c = 30 
# d = 40 







# :: Types of Namespaces : 

# 1.) Built-in namespace. 
# 2.) Module level / global namespace. 
# 3.) Local namespace. 
# 4.) Enclosed Namespace.  








# 1.) Built-in namespace : 
# - Built-in namespace are that which are in-built by the python and we can see all the built-in namespace by dir() function.
# - Built-in namespace tabb create hote hai jab ham interpreter ko start krte hai. 
 
# - Ex : 

# print(dir())  # output : ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']









# 2.) Module level / global namespace : 
# - Global namespace ak aisa module hai jo particular module ke liye seperate create kiya jata hai. 
# - global namespace tab create hote hai jab ham Python Program ko run krte hai. 


# - Ex :  [ In example.py ]

# a = 100
# def diplay():
#     print(a)

# - Ex :  [ In example1.py ] 

# a = 20
# def display():
#     print(a)


# - Ex : [ In main.py ]

# import example , example1 
 
 
# example.display(a)    # output : 100
# example1.display(a)   # output : 20















# 3.) local namespace :  
# - local namespace ak aisa module hai jo particular function ya progrma ke liye seperate create kiya jata hai.
# - Ex : 

# a = 50 

# def func1():
#     a = 10
    
#     def func2():
#         b = 100 
#         print(dir())
#     print(dir())   # output :  ['a', 'func2']
    
 
    
    
# def func2():
#     a = 20
#     print(dir())  # output : ['a']
    
# print(dir())   # output : ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'func1', 'func2']



# func1()
# func2()








# 4.)  Enclosed Namespace : 
# -  This is the namespace that is enclosed inside the nested function. 
# - Ex: 

# a = 50 

# def func1():
#     a = 10
    
#     def func2(): #--> Enclosed namespace
#         b = 100 
#         print(dir())
#     print(dir())   # output :  ['a', 'func2']
    
    
    
    





# ____________________________________________________________________________________________________________________________________________




# ::  Non Local Variables / keyword in Python :  


# :--> LEGB RULE : [ Local , Enclosed  , Global , Built-in ]

# - It is responsible of deciding what value is going to print according to the scope. 
# - it first checks what is the current scope for the variable. 
# - Priority : Built-in > global > Enclosed > local. 


# - Ex :

# x = 100 

# def outer():
#     x = 10 
#     def inner():
#         x = 1000
#         print(x)
        
#     inner()
    
    
# outer()  







# # - Ex : 

# x = 100   # global variable 

# def outer():
#     x = 20    #--> non-local variable
    
#     def inner():
#         nonlocal x
#         x = x + 20
        
#         x = 200  #--> local variable
#         print(x)
        
#     inner()
#     print(x)  # --> LEGB RULE ke accrding value print hogi    
# outer()









# ____________________________________________________________________________________________________________________________________________


# :: Closures in Python :  

# - Closure is a technique by which data gets attached to the code. 
# - closures are function objects that remembers values in the enclosing scope even if they are not present in the memory.
# NOTE :  

# - Ex : 
 
def outer():
    
    def inner():
        print("hello")
        
    return inner 


inner = outer()

inner

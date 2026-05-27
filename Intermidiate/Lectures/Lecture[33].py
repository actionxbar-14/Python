
# :: Youtube Playlist Content : 

# --> lecture-166 : reduce() function in Python.
# --> lecture-167 : Partial Function in Python. 
# --> lecture-168 : Recursion in Python. 
# --> lecture-169 : Direct recursion in Python. 
# --> lecture-170 : factorial Program using recursion. 


# _______________________________________________________________________________________________________________________ 



# :: reduce() function in Python : 

# - This is built-in higher order function defined in functools module. 
# - For Using this function we have to first import functools module. 
# - It doesn't return another iterable but returns a single reduced value. 
# - it take necessary two parameter for iteration. 
 
# - Syntax :  functools.reduce(function_name , iterable)



# - Ex : 

# import functools

# nums = [5 , 8 ,2 , 10 , 9] 

# def func(a , b):
#     return a + b

# print(functools.reduce(func , nums))  # output : 34





# - Ex : Using lambda Function : 

# import functools

# nums = [5 , 8 , 2 , 10 , 9]
# print(functools.reduce(lambda a , b: a + b, nums))  # output: 34




# - Ex : find the maximum num present in the list

# import functools 

# nums = [5 , 8 , 2 ,10 , 9]

# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b 
    
    
# print(functools.reduce(max , nums))  # output :  10







# _______________________________________________________________________________________________________________________ 




# :: Partial Function in Python : 

# - Partial Function allows us to fix a certain number of arguments of a function and generate a new function. 
# - It is also exist in the functools module. 
# - always use keyword argument while using the Partial Function in Python. 
# - Syntax : partial(func , arg_1 , arg_2 , .... arg_n)


# - Ex :

# from functools import partial 

# def add(n1 , n2 , n3 , n4):
#     return n1 + n2 + n3 + n4  

# add = partial(add , n1 = 2 , n2 = 3)

# print(add( n3 = 5 , n4 =  10)) 
# output :  20 [ 2 + 3 ( fixed ) + two variable argument ( 5 , 10) =   2 + 3   +    5 + 10 ]









# _______________________________________________________________________________________________________________________ 




# :: Recursion in Python : 

# - When a function calls itself , then that function is called as recursive function and process is called as recursion. 



# - Syntax :  

# def func():
#     base cond:
#         return 
#     # code
#     return [recursive_call]









# - Ex : 
# i = 0
# def demo():
#     global i
#     print("hello" , i)
#     i += 1
    
   
#     demo()  #--> This will print "hello" many times (1000 approx) after that it gives an recursion error. 
   

# demo()




# NOTE : Changing the limit of recursion error ( 1000 ) :

# import sys 

# print(sys.getrecursionlimit())   # output : 1000

# sys.setrecursionlimit(200)



# i = 0
# def demo():
#     global i
#     print("hello" , i)
#     i += 1
    
#     demo()  # yaha prr "hello" only (200) bar hi print hoga!
    
    
# demo()









# :-> Advantages of recursion : 

# 1.) Clean Code 
# 2.) Complex problems can be solved. 


# :-> Disadvantages of recusrion : 

# 1.) Hard to debug 
# 2.) Not memory efficient






# _______________________________________________________________________________________________________________________ 


# :: Types of Recursion :  

# 1.) Direct Recursion. 
# 2.) Indirect Recursion. 






# 1.) Direct Recursion : 

# - When a function calls itself.  

# - Ex : Python Program for printing n to 1 sequence 

# n = int(input("Enter the value of n :"))

# def natural(n): 
#     if n==0:
#         return   #--> ye ak stopping condition hai jissse recurion function call ko break/stop krta hai
#     print(n)

    
#     return natural(n-1)
    
# natural(n)













# 2.) Indirect Recursion :- 

# - A function calls another function which then calls the first function again.  

# - Ex : 

# def num(n):
#     if n <= 0:
#         return 
    
#     print(n , end = " ")
#     num1(n-1)


# def num1(n):
#     print(n , end = " ")
#     num(n-1)
     
     
     
# num(10)  # output : 10 9 8 7 6 5 4 3 2 1







# _______________________________________________________________________________________________________________________ 



# :: Write a Python Program for factorial of a number using recursion : 

# - Syntax : 

# num = int(input("Enter num :")) 

# def fact(num):
#     if cond:
#         return 
    
#     return [ recursive_call ]

# fact(num)





# - Program :  



# num = int(input("Enter num :")) 

# def fact(num):
#     if num == 0:
#         return 1
    
#     return num * fact( num - 1)

# print(f"the factorial of {num} is : {fact(num)}")
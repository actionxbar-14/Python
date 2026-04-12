
# :: Youtube Playlist Content : 

# --> lecture-41 : When to Use for and while loop.
# --> lecture-42 : Match case in Python. 
# --> lecture-43 : Flowcharts in Programming and How to Draw Flowcharts. 
# --> lecture-44 : Ternary Operator in Python. 
# --> lecture-45 : Walrus Operator in Python.


# ___________________________________________________________________________________________________________________________________________




# :: When to use for and while loop : 


# 1. for loop :
# -> when you know starting point & ending point. 
# -> when you know number of iterations/fixed. 
# -> when you want to iterate through iterable(list , string , tuple , dictionary). 
# NOTE: There are some collections which do not support indexing ( set , dictionary etc) , so here we can only use for loop with respecting to while loop. 








# Ex: 1 

# Python Program for printing first 5 integer numbers. 

# for i in range(1,5) :
#     print(i)





# Ex : 2

# Write a python program for printing even numbers from Data. 


# data = [23, 45, 12 , 8 , 9 , 14 , 17 ,11 , 16 ,32]

# for i in data:
#     if i%2 == 0:
#         print(i)





















# 2. While loop : (in while loop we access the item using indexing method).

# -> If you don't know the number of iteration.
# -> When indexing is important for us.

# Ex: 

# Execute code untill user enters yes. 
# Generate random numbers untill you get 15. 
# Selection sort. 
# Merging two lists. 











# ___________________________________________________________________________________________________________________________________________





# :: Match case in Python :

# --> match enables you to match a value or an expression against a series of patterns and execute corrosponding block of code for the first matching pattern encountered. 
# --> It is an alternative of switch case beacuse python does not have a switch case. 
# --> In each case we don't have to write break statement again and again beacause match case statement consist inner break statement at each case itself.  

# --> Syntax : 

# match expression/value :
#     case value 1 :
#         # code
#     case value 2 :
#         # code
#     . 
#     . 
#     . 
#     . 
#     .
#     case value n: 
#         # code 
#     case _:
#         # code   
    
    
    
    
    
# Ex :

# status code 404 :- page not found 
# status code 500 :- internal server error 
# status code 200 :- success 


# status_code = 404

# match status_code:
#     case 200:
#         print("succuss")
#     case 404:
#         print("page not found")
#     case 500:
#         print("internal server error")
#     case _:
#         print("Invalid status code")
        
        
        
        
        
# ___________________________________________________________________________________________________________________________________________



# :: Flowchart in Python :

# --> Go to the written notebook for the revision. 

# ___________________________________________________________________________________________________________________________________________




# :: Ternary Operators :  (short hand if-else)


# --> Syntax :

# value_if_true if condition else value_if_false. 

# Ex: 

# age = 18

# is_adult = print("adult") if age >= 18 else print("not adult")

# print(is_adult)



# ___________________________________________________________________________________________________________________________________________




# :: Walrus operator :  ( := )

# - You can assign a value within an expression. 
# - always use inside the parenthesis. 

# Ex: 

# a = 100

# print(a = 100 + 1) #Output : TypeError: 'a' is an invalid keyword argument for print()

# print((a = 100) + 1)

#    print((a = 100) + 1)
#            ^^^^^^^
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?



# Ex :

# a = 100

# print((a := 100))   #--> 100
# print((a := 100 + 1 ))  #--> 101
# print((a := 100) + 1 )  #--> 101








# :--> Actual implementation :






# Ex : 1

# :--> without walrus operator :

# data = [10 , 20 , 30 , 40 , 50 , 60]

# n = len(data)  
# i = 0
# while i<n:
#     print(data[i])
#     i += 1
    

# :--> with walrus operator :

# data = [10 , 20 , 30 , 40 , 50 , 60]
# i = -1
# while (i := i+1) < (n := len(data)):
#     print(data[i])
# else:
#     print("all element is printed")












# Ex : 2


# :--> without walrus operator :

# data = [10 , 20 , 30 , 40 , 50 , 60]
# n = len(data)
# while n>0:
#     print(data.pop())
#     n -= 1
# print(data)



# :--> with walrus operator :

# data = [10 , 20 , 30 , 40 , 50 , 60]
# while (n := len(data)) > 0:
#     print(data.pop())
#     n -= 1
# print(data) 










# Ex : 3


# :--> without walrus operator :

# while True:
#     ans = input("Do You want to continue(y/n) :").lower()
#     if ans!= 'y':
#         print("terminate the process")
#         break 
#     print("process the request")

    




# :--> with walrus operator :


# while (ans := input("Do You want to continue(y/n) :").lower()) == 'y':
#     print("process the request") 
    
# else:
#     print('terminate the process')
    
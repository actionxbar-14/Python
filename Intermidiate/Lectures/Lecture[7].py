
# :: Youtube Playlist Content : 

# --> lecture-36 : While loop in Python.
# --> lecture-37 : While else in Python / nested while loop in Python. 
# --> lecture-38 : range() function. 
# --> lecture-39 : For loop / for else in Python. 
# --> lecture-40 : Break and Continue in Python.



# ____________________________________________________________________________________________________________________


# :: Loops in Python : 
# - Loops are used in Programming to repeat a specific block of Code. 
# - In Python we have two types of loops :-
#  1. While loop
#  2. For loop 







# 1. While loop :- 
# -  While loop is used to iterate over a block of code as long as condition is True. 
# -  In the while loop , condition is checked first. If condition is True , body of while is executed. 
# -  Syntax :

# While condition:
#     block of code


# :--> Steps: 
#     1. Initializtion : Giving initial value to variable. 
#     2. Condition checking : condition ahead of while is checked. 
#     3. Increment/decrement : updating counter variable. 




# Ex : 

# i = 1
# while i <= 10:
#     print("code-yug")
#     i = i + 1
    
    
# Ex: table of num that is given by the user as input.

# num = int(input("Enter the value of num :"))


# def table_input(num):
#     i = 1
#     while i <= 10:
#         print(f"{num} x {i} = {i*num}")
#         i += 1
    
    
    
# table_input(num)
    
    
    
    
    
# Ex:  None --> False 

# i = 1
# while None:
#     print(i)
#     i += 1



# ____________________________________________________________________________________________________________________




# :: While loop with else :
# - The else block is executed if the condtion in the while loop evaluates to False. 
# - Syntax :

# while condition:
    # body of while loop 
    
# else:
    # body of else 


# rest of statements 


# Ex : 

# count = 1

# while count <= 4:
#     print("while wala part chala")
#     count += 1
   
    
# else:
#     print("else wala part chala")
 




# NOTE : If you terminate while loop by using 'break' keyword  , else part is ignored. 

# Ex: 

# count = 1
# while count <= 5:
#     print("inside while loop")
#     count += 1
#     if count == 3:
#         print(f"count: {count} , loop is terminating.")
#         break 
    
# else:
#     print("else wala part chala")
    


   
    
    
    
    
    
    
    
    
    
    
    
# :: nested while loop :

# -> syntax : 

# while expression:
#     statement 
#     while expression:
#         statement  
        

# rest of statements 
    


# Ex :

# i = 1
# while i <= 3 :
#     print("Outer loop")
    
#     j = 1
#     while j <= 3:
#         print("inner loop")
#         j += 1
        
#     i += 1
#     print()
    
    
    
# Output : 

# Outer loop
# inner loop
# inner loop
# inner loop

# Outer loop
# inner loop
# inner loop
# inner loop

# Outer loop
# inner loop
# inner loop
# inner loop
    
    
    
    
    
    
    

# ____________________________________________________________________________________________________________________


# ::  range() function :

# - range() function returns an immutable sequence of number between the given start and stop integer. 
# - Syntax :

# range(start, stop , step) 

# --> start : starting position. starting integer of range sequence. 
# --> stop : ending position. sequence ends at stop - 1. 
# --> step : increment between each integer in sequence. 



# NOTE :

# 1. start is optional , it's default value is 0. 
# 2. step is optional , it's default value is 1. 
# 3. stop is mendatory , sequence stops at stop - 1. 
# 4. start , stop , step can't be float , complex values. 
# 5. step can not be 0 . 




# Ex : 1

# range(5 , 1) ----> []

# Ex : 2

# range() -----> Type-Error 


# Ex :  3


# num = range(10 , 20 , 2)  # --> 10 , 12 , 14 , 16 , 18. 
# print(num[0]) # --> 10
# print(num[1]) # --> 12
# print(num[2]) # --> 14
# print(num[3]) # --> 16 
# print(num[4]) # --> 18


# # Ex :  4

# print(range(10,20,2))   #  output : range(10,20,2)

# print(list(range(10,20,2)))   # --> [10 , 12 , 14 , 16 , 18] 



# Ex : 5

# print(range()) --> TypeError  





# NOTE: 

# 1. range() function does not store all values in a memory. It would be inefficient. So , it remembers the start , stop , step and generate next numbers on the go. 


# 2. Since , it is not an iterator. But , it supports all operations made for iterator. 


# ____________________________________________________________________________________________________________________



# ::  For loop :

# - for loop is used to iterate over a sequence ( list , tuple , string , or other iterable objects). 
# - Syntax :

# for var in sequence:
    #   statement 1 
    #   statement 2
    #         . 
    #         .
    #         .
    #   statement n
    
    
# Rest of the code. 






# Ex :  print table of 1 using for loop 

# num = 5
# for val in range (1 , 11) :
#     print(f"{num} * {val} = {num * val}")















# :: for loop with else :

# Ex :

# digits = [0,1,5]
# for i in digits:
#     print(i)
# else:
#     print("no items left")
    
    
# Output : 
# 0
# 1
# 5
# no items left



# NOTE : break statement in for else loop.

# digits = [0,1,5]
# for i in digits:
#     print(i)
#     if i == 5:
#           break
# else:
#     print("no items left")
    
# Output : 
    
# 0
# 1
# 5





# ____________________________________________________________________________________________________________________




# :: Python break statement :

# - In Python , break statement used to alter the flow of program. 
# - When break occurs , control of program flows to statements immediately after body of loop. 


# - Syntax :  ( for loop )

# for var in sequence:
#     # code inside for loop
#     if condition:
#         break 
    # code inside loop 
    
# rest of statements 




# - Syntax :  ( while loop )

# while condition:
#     # code inside while loop
#     if condition:
#         break 
    # codes inside while loop 
    
# rest of statements 





# Ex : 

# # name = input("enter name  :")  #--> anubhav

# # for char in name :
# #     if char == 'h':
# #         break  
# #     print(char , end = " ")
    
# output : a n u b 











# :: Python continue :

# - In Python , continue used to bring control at beginning of loop. 
# - Skips remaining lines of code and continue with next iteration. 

# :: Syntax : ( for loop )

# for var in sequence:
#     # code inside for loop
#     if condition:
#         continue 
#     # code inside loop 
#     # rest of statements



# :: Syntax : ( while loop )

# while condition:
    # # code inside while loop
    # if condition:
    #     continue 
    # codes inside while loop 
    
# rest of statements 




# Ex :


# name = input("enter name  :")  #--> anubhav

# for char in name :
#     if char == 'h':
#         continue  
#     print(char , end = " ")
    
# # output :  a n u b a v 



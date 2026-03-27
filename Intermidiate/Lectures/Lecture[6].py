
# :: Youtube Playlist Content : 

# --> lecture-31 : Indentation in Python.
# --> lecture-32 : If statement in Python. 
# --> lecture-33 : If-else statement in Python. 
# --> lecture-34 : nested If-else in Python / Short hand if's. 
# --> lecture-35 : if-elif-else in Python / multiple conditions.




# ______________________________________________________________________________________________________________________


# :: Indentation in Python :

# - a whitespace for defining the syntax and overall structure of Python.  
# - Indentation refers to the spaces and tabs that are present at the beginning of statement. 
# - Python have default indentation of 4 spaces. 
# - if we do not give proper indentation then python simply throws an indentation error ,because python is not a free form language. 
# - the statement which does not belong to any block of code has indentation value = 0. 


# Ex : 

# age = 20  ( indentation = 0 )
# if age >= 18:
#     print("hello")
#     print("you can vote") 
    
    

# ______________________________________________________________________________________________________________________

# :: Decision making in Python :-

# - Sometimes , Python programs has to take decisions using certain conditions. 
# - Ex :  Number is even or odd , Voting age. 





# :: if statement :-

# - If statement is used for decision making. 
# - In if statement , we check a condition which is depending on truth value of condition , decision will be taken. 
# - Written using 'if' keyword. 


# - Syntax :

# if condition / test_expression:
#     statement 1
#     statement 2 
    
# rest of statements



# --> Ex :

# if True:
#     print("This is true")
   
# print("my name is Anubhav")



# if False: print("this is also true")
# else: print("false hai")


# NOTE :
# --> Non-zero : True 
# --> Zero : False 
# --> None : False


















# :: if-else statement :-


# - The if-else statement provides an else block combined with if block which is executed in the False case of condition. 
# - only one block is executed at one time. 
# - For one if we can use only 1 else at a time. 
# - True : if block 
# - False : else block



# - Syntax :

# if test_expression:
#     body of if 
    
# else:
#     body of else



# - Ex : 

# Program to check number is even or odd. 

# num = int(input("Enter a number :"))

# if num % 2 == 0:
#     print("number is even")
    
# else:
#     print("number is odd")

# else: --> error
#     print("num is odd , second vala else chala")
    



















# :: Nested if in Python :-

# - We can have a if-else statements inside another if-else statement. This is called nesting of if's. 

# - Any number of these statements can be nested into one another. 

# - Indentation is the only way to figure out the level of nesting. 

# - Confusing , so avoid it.  




# - Syntax : 
 
# if condition:
#     statement
#     statement 
#     if condition:
#         statement
#         statement 
#     else:
#         statement 
#         statement 
        
# else:
#     statement 
  
 
#rest of code 


# - Ex :

#Program for positive and negative numbers. 

# num = float(input("Enter a num :"))

# if num >= 0:
#     if num == 0:
#         print("number is zero")
        
#     else:
#         print("number is positive")
        
    
# else:
#     print("number is negative")



# NOTE : shorthand if-else 

# a = 2 
# b = 10 

# print("hello") if a>b else print("bye") --> bye

























# :: if-elif-else  in Python :-

# - The if-elif-else statement enables us to check multiple conditions and executes a specific block of statements depending upon True among them. 

# - syntax :

# if test_expression1 :
#     #block of statements 
    
# elif test_expression2:
#     #block of statements 
    
# elif test_expression3:
#     #block of statements 
    
# else:
#     #block of statements 
    
    


# - Ex: 

# num = int(input("Enter a number :"))

# if num == 10:
#     print("number is 10")
    
# elif num == 20:
#     print("number is 20")
    
# elif num == 50:
#     print("number is 50")
    
# else:
#     print("other than 10 , 20 , 50")
    
    
    
    
    
# :--> Question: Write a program for grading according to marks. user will be asked to enter marks by keyboard. Print grade on output window according to marks. marks and grades are as follows. 
# 1) Between 86 to 100 (both including) :- Grade A 
# 2) Between 61 to 85 (both including) :- Grade B 
# 3) Between 41 to 60 (both including) :- Grade C
# 4) Less than or equal to 40 ( both including ) : Fail  


# marks = int(input("Enter the marks :"))

# if marks <= 40:
#     print("fail")
    
# elif marks >= 41 and marks <= 60 :
#     print("Grade C")
    

# elif marks >= 61 and marks <= 85 :
#     print("Grade B")
    

# elif marks >= 86 and marks <= 100 :
#     print("Grade A")
       
    
# else:
#     print("Invalid input")
    
 
    
    
    
    
    
    
    
    
    
    
    





































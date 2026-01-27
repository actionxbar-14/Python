
                         # TOPIC :    Loops in Python
                     #              [ For & While Loop ]




# Loops :

# - Loops enable you to perform repetitive tasks efficiently without writting redundant code.
# They iterate over a sequence(like a list , tuple , string , or range) or execute a block of code as long as a specific condition is met.

# Types of Loops :

# 1.While Loops.
# 2 For Loops.
# 3.Nested Loops



# ::While Loop :

# -The while loop repeatedly executes a block of code as long as a given condition remains True. It checks the condition before each iteration.

# Syntax:    while condition:
                   #code block to execute

# Example : Print numbers from 0 to 3.

# count = 0

# while count < 4:
#     print(count)
#     count+=1
# else:
#     print("While loop ended")
# #output : 
# 0
# 1
# 2
# 3
# While loop ended


# While True:
#     print("ye to always chlega")
# else:
#     print("bhai while ke agge false likha tha kya?")







# :: For Loop:-

# - The for loop in python is used to iterate over a sequence(such as a list , tuple , dictionary , set or string) and execute a block of code for each element in that sequence.

# syntax : 

# for variable in sequence:
    # code block to execute


# Example: iterate over each character in language.

# language = 'Python'  #Sequence

# for x in language:
#     print(x)

# # output : 
# P
# Y 
# T 
# H 
# O 
# N


# ::NOTE:  RANGE FUNCTION :-

# # only one value inside range function:
# range(stop) - Excluding stop value

# # only two value inside range function:
# range(start , stop) - Excluding stop value

# # only three value inside range function:
# range(start , stop , step) - Excluding stop value



# Ex:

# for i in range(5):  -[range(stop)]
#     print(i)

# #output :
# 0 
# 1 
# 2
# 3
# 4



# Ex:

# for i in range(1,5): -[range(start,stop)]
#     print(i)

# #output :
# 1
# 2
# 3
# 4


# Ex:


# for i in range(1,10,2): -[range(start,stop,step)]
#     print(i)

# # output:
# 1
# 3
# 5
# 7
# 9



# Ex:

# for i in range(5):
#     print(i)
# else:
#     print("for loop ended")

# # output:
# 0
# 1
# 2
# 3
# 4
# for loop ended


# -->Note:

# While loop VS for loop :

# :-While loop :
# - A while loop keeps running as long as a condition is true.
# - It is generally used when you don't know how many iterations will be needed beforehand , and loop continues based on a condition.

# :-for loop :
# - A for loop iterates over a sequence(like a string , list , tuple or range) and runs the loop for each item in that sequence.
# - It is used when you know in advance how many times you want to repeat a block of code.












# Loop Control Statements : 

# -Loop control Statements allow you to alter the normal flow of a loop.
# python supports 3 clauses within loops:

# 1. Pass Statement.
# 2. Break Statement.
# 3. Continue Statement.


# 1. Pass Statement : 
# - The pass Statement is used as a placeholder (it does nothing) for the future code , and runs entire code without causing any syntax error.

# Ex:

# for i in range(5):
#     # code to be updated
#     pass

# Above example , the loop executes without error using pass statement.

# Ex: while Loop

# count = 5
# while count>0:
#     if count == 3:
#         pass
#     else:
#         print(count)
#     count-=1


# #output:
# 5
# 4
# 2
# 1




# 2.Break Statement :
# - The break statement terminates the loop entirely , exiting from it immediately

# - the loop terminated when condition met true for i == 3.

# Ex:

# for i in range(5):
#     if i == 3:
#         break
#     print(i)

# output : 
# 0
# 1
# 2





# 3. Continue Statement :
# - The continue statement skips the current iteration and moves to the next one.

# Ex:

# for i in range(5):
#     if i==3:
#         continue
#     print(i)

# # output:
# 0
# 1
# 2
# 4





# Example 1:

# count = 5
# while count > 0:
#     # print(count)
#     if count == 3:
#         pass
#     else:
#         print(count)
#     count-=1

# output : 
# 5
# 4
# 2
# 1


# Example 2:  gives infinite loop!!!! [ because continue pure iteration ko hi skip krr deta hai.]

# count = 5
# while count > 0:
#     print(count)
#     if count == 3:
#         continue
#     else:
#         print(count)
#     count-=1

# :Another example:

# while True:
#     user_input = input("Enter 'exit' to STOP : ")
#     if user_input == 'exit':
#         print("congrats! You guessed it right")
#         break
#     print("sorry! , you entered", user_input)
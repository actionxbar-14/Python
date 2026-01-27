
                          # TOPIC : Nested Loops








# Nested Loop : Loops inside another loop.

# - Loop inside another loop is nested loop. This means that for every single time the outer loop runs , the inner loop runs all of its iteration.
# - [Iska Matlab jab paheli bar outer loop chlega tab , inner loop ki sari iteration chlne ke baad outer loop dusri baar chlega , aise krte krte jitni bar outer loop chlega utni baar inner loop ki saari iteration chalti hai.]


# Why Use Nested loops ?

# - Handling Multi-Dimensional Data Such as matrices , grids or lists of lists.
# - Complex iterations : Operations depend on multiple variables or dimensions.
# - Pattern Generation : Creating patterns , such as in graphics or games.



# ::Syntax : 

# Outer_loop:
#     inner_loop:
#         #[Code block to execute - innner loop ]
# [Code block to execute - outer loop ]
    

# ::Example:

# Ex: 1. Print Numbers from 1 to 3 for three times:

# for i in range(3):
#     print(f" iteration of outer loop:",i)
#     for j in range(1,4):
#          print(j)
#     print(" ")

# # output :
#  iteration of outer loop: 0
# 1
# 2
# 3

#  iteration of outer loop: 1
# 1
# 2
# 3

#  iteration of outer loop: 2
# 1
# 2
# 3
    




# Ex:2. using while and for loop print number 1 to 3.

#i = 1 #(initialising the starting point for outer loop[while loop])

# while(i < 4): # ----> outer loop. 
#     print(f'loops run for outer loop',i) 
#     for j in range(1,4): # -----> inner loop.
#         print(j)
#     print(" ___________ ")
#     i+=1  #(incriment of iteration of outer loop i by +1).



# Ex: 3.  Print prime numbers between range of 2 and 10 using nested loops.

# for i in range(2,20):
#     # print(f"::Outer loops runs after {i} iteration:-")
#     print(" ")
    
#     for num in range(2,i):
#         # print(f"::innner loops runs for {num} values:-")
#         print(" ")
#         if i % num == 0:
#             print(f"{i} is divisible by {num} , hence it is not prime number.")
#             break
#     else:
#         print(f"{i} is a prime number.")






# HW: write a program to take to numbers a , b from user and find the all prime numbers between that two numbers.

# Ans :

# name = input("Hello , Plese Enter Your Name :")
# # print(f"Hii {name} , You can Give two numbers and i am going to give you the all prime numbers in between that two numbers : ")


# def Find_prime():
#     a = int(input(f"{name} Plese Enter Value of a :"))
#     b = int(input(f"{name} Plese Enter Value of b :"))
#     # print(a)
#     for i in range(a,b):
#         for num in range(a,i):
#             if i%num == 0:
#                 # print(f"{i} is divisible by {num} , hence it is not prime number.")
#                 break
#         else:
#             result = i
#             print(result)

# Find_prime()
# result_prime = Find_prime()
# print()


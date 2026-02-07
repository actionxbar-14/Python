
                        # TOPIC  : Assignment - 5







# Questions :

# 1. Print the while loop output in same line.
# 2. Print star pattern - using loops.
# 3. Write a program to find the factorial of a given number.
# 4. Count the number of vowels in a string.
# 5. Find the longest word in a sentence using a for loop.
# 6. "do while" loop in python - how to do it?
# 7. Write a program to print first N numbers in the Fibonacci series using a while loop.













# Syntax of Print Statement :
# print(object(s), sep=separator, end=end, file=file, flush=flush)

# :: Print statement consist of basically 4 type of argument mention below:

# - object(s)	: Any object, and as many as you like. Will be converted to string before printed.

# - Separator : sep='separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '.

# - End : end='end'	Optional. Specify what to print at the end. Default is '\n' (line feed).

# - file : 	Optional. An object with a write method. Default is sys.stdout.

# - flush	Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False.



# Ex:1
 
# print("Hello")
# print("Anubhav")

# ::Output :
# Hello
# Anubhav




#Ex:2

# print("Hello", end = " ")
# print("Anubhav")

# ::Output :
# Hello Anubhav




# Ex:3

# print("Hello" , end = " * ")
# print("Anubhav")

# :: Output : 
# Hello * Anubhav



# Ex:4

# print("Hello" , sep = "*" , end = " * ")
# print("Anubhav")

# :: Output : 
# Hello * Anubhav 



# Ex:5

# print("Hello" , "Anubhav", sep = "-" , end = " * ")
# print("This was a great time with you")


# :: Output :
# Hello - Anubhav * This was a great time with you




# Ex:6

# print("Hello" , "Anubhav", sep = "&" , end = " * ")
# print("This was a great time with you")

# :: Output :
# Hello&Anubhav * This was a great time with you




# ___________________________________________________________________________





# Question:1
# Print the while loop output in same line.

# Solution:
# i = 1
# while i < 5:
#     print(i, end = " ")
#     i+=1

# Output :
# 1 2 3 4 



# ___________________________________________________________________________





# Question:2
# Print star pattern - using loops.


# Pattern - 1 [Right Angle Triangle]:
#  * 
#  *  *
#  *  *  *
#  *  *  *  *
#  *  *  *  *  *



# :--> Method : 1

# n = 5

# for i in range(1, n+1):  
#     for j in range(1, i+1):
#         print("*", end = " ")
#     print()


# Output : 
#  * 
#  *  *
#  *  *  *
#  *  *  *  *
#  *  *  *  *  *





#  :--> Method : 2


# print(" * " * 5)
# output : *  *  *  *  * 


# n = int(input("Enter n:"))
# for i in range(1,n+1):
#     print(" * " * i)


# Output : 
#  * 
#  *  *
#  *  *  *
#  *  *  *  *
#  *  *  *  *  *







# Pattern - 2 [Inverted Triangle] :


# --> Method - 1:
# n = 5

# for i in range(n , 0 , -1):
#     for j in range(1 , i+1):
#         print("*", end = " ")
#     print()

# Output: 

# * * * * * 
# * * * *   
# * * *     
# * *       
# *  


#  --> Method - 2:

# n = int(input("Enter n:"))
# for i in range(n,0,-1):
#      print(" * " * i)

# Output : 

#  *  *  *  *  * 
#  *  *  *  * 
#  *  *  * 
#  *  * 
#  *



# Pattern - 3 [Equilateral (Pyramid) Triangle] :

# n = 5


# for i in range(1, n+1):
#     print(" "  *  (n-i), end = "" )
#     print("*" * (2*i - 1))   # 2*i - 1 : 2n-1 = 1,3,5,7...
     
# Output :

#     *
#    ***
#   *****
#  *******
# *********



# ___________________________________________________________________________


# Question : 3 Write a program to find the factorial of a given number.

# def factorial(n):
#     result = 1
#     while n > 0 :
#         result *= n   # 5 * 1 , 5 * 4 , 20 * 3 , 60 * 2 
#         n -= 1
#     return result

# print(f"The factorial of  5 is  {factorial(5)}")

# Output : 
# The factorial of  5 is  120

# ___________________________________________________________________________


# Question : 4 Count vowles in a string.

# my_string = "My Name is Anubhav Pathak"
# vowels = "aeiou"
# count = 0

# for char in my_string:
#     if char.lower() in vowels:
#         count += 1
# print("Number of vowels are : ",count)

# # Output : 
# # Number of vowels are :  8


# ___________________________________________________________________________


# Question : 5 Find the longest word in a sentence using a for loop.

# sentence = "My name is Anubhav Pathak"
# words = sentence.split()  #--> ['My', 'name', 'is', 'Anubhav', 'Pathak']
# print(words)
# longest_word = ""

# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word

# print("The longest word is :", longest_word)

# Output : 

# The longest word is : Anubhav


# ___________________________________________________________________________


# Question :  6 "do while" loop in python - how to do it?

# Do - while Loop : 

# - A do-while loop in other languages(such as a C , C++, or Java) ensures that the loop body executes at least once before checking the condition. In Python , you can achieve the same behaviour by using a while loop with a break condition.

# Syntax : 

# while True:
#     # Loop body
#     # Execute this block at least once

#     if not condition:
#         break


# # Example :

# while True:
#     num = int(input("Enter a num greater than 10:"))

#     if num > 10:
#         print(f"valid number entered:{num}")
#         break # Exit the loop when condition is satisfied
#     else:
#         print("Number is not greater than 10, try again!")



# ___________________________________________________________________________



# Question : 7 Write a program to print first N numbers in the Fibonacci series using a while loop.

# :- Fibonacci Sequnce : 
# # Each number is equal to the sum of the preceding two numbers : 0,1,1,2,3,5,8......


# def Fibonacci(n):
#     a , b = 0 , 1
#     count = 0
#     while count < n:
#         print(a)   # 0 1 1 2 3 5 8 ......
#         a , b = b , a + b
#         count += 1

# Fibonacci(10)
# Output : 0 1 1 2 3 5 8 13










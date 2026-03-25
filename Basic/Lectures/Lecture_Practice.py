


# * * * *
# * * * *
# * * * *
# * * * *

# m = int(input("Enter m:"))
# n = int(input("Enter n:"))

# for i in range(m):
#     for j in range(n):
#         print("*",end=" ")
#     print(" ")






# * 
# * * 
# * * * 
# * * * *



# m = int(input("Enter m:"))
# n = int(input("Enter n:"))

# for i in range(m):
    # for j in range(i+1):
    #     print("*",end=" ")
#     print(" ")









# * * * * *
# * * * *
# * * *
# * *
# *



# n = int(input("enter n:"))

# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()


# n = int(input("enter n:"))

# for i in range(1,n):
#     print(" * " * (i))



# n = int(input("enter n:"))

# for i in range(n , 0 , -1):
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print()
   

# n = int(input("enter n:"))

# for i in range(n , 0 , -1):
#      print("* " * i+1)






         
#         *
#       * *
#     * * *
#   * * * *



# n = 5  # no. of rows

# n = int(input("enter n:"))

# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print("*",end=" ")

#     for k in range(i+1):
#         print("*",end=" ")

#     print()

        











    



# n = int(input("Enter n:"))

# for i in range(1,n+1):
#     print(" " * (n-i) ,end = "")
#     print("*" * (2*i - 1))

# print()







# My_aim = "Anubhav is a brilian infrastructure engineer"

# Split_aim = My_aim.split()

# # print(Split_aim)


# Longest_word = ""


# for word in Split_aim:
#     if len(word) > len(Longest_word):
#         Longest_word = word 

# print(f"The Longest word in {My_aim} is \"{Longest_word}\" ")






# def Fibonacci(n):
#     a,b = 0,1
#     count = 0

#     while count < n:
#         print(a)
#         a,b = b , a+b 
#         count += 1

# Fibonacci(10)






# a = "anubhav"
# print(type(a))

# a = 30
# print(type(float(a)))

# a = 20
# b = 20.0

# add = a + b 
# print(type(add))




# a=True
# b=10.5
# c=a+b

# print (c);   output : 11.5

# print(type(a))


# age = int(input("Enter Your age:"))

# if age < 18 :
#     print(f"Since Your age is {age}  , so You can not vote!")


# elif age > 18 and age < 25:
#     print(f"you are a middle age guy you must have to vote") 



# elif age > 35 and age < 55:
#     print(f"you are a senior citizen aged guy you have to decide wisey to vote") 


# # elif age < 18:
# #     print(f"Since Your age is {age}  , so You can not vote!")


# else:
#     print(f"age : {age} ke liye maine koi option nhi banaya hai")





# number = int(input("Enter Your number:"))

# if number > 0:

#     if number % 2 == 0:
#         print(f"{number} is positive and even")

#     else:
#         print(f"{number} is positive and odd")


# elif number < 0:
#     if number % 2 == 0:
#         print(f"{number} is negative and even")

#     else:
#         print(f"{number} is negative and odd")


# else:
#     print("the number is zero")









# if (year % 4 == 0 or year % 100 == 0) and (year % 400 == 0):
    

# 
# year = int(input("Enter the year:"))

# if year % 400 == 0:
#     print(f"{year} is a leap year!")

# elif year % 4 == 0 and year % 100 != 0:
#     print(f"{year} is a leap year!")

# else:
#     print(f"{year} is not a leap year!")





# result_leap_year = print(f"{year} is a leap year!") if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else print(f"{year} is not a leap year!")

# print(result_leap_year)



# print("____Welcome to the Password Strenght Checker____")


# def check_password_strength(password):

#     if password.len() < 8:
#         return "Weak : Password must have 8 character"

#     elif

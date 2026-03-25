                   
                            # Assignment - 3






# Question : 1

#  Write a program to determine if a given year is a leap year using input.
# :: condition for leap year : 
# - if an year is divisible by 4 or 100 and divisible by 400 then it is a leap year.
# - leap year occours once every four years

# Answer : 1

# print("Here You can get if the given Year is Leap year or not:")

# year = int(input("enter the year:"))
# leap_year = f"{year} is a leap year" if year % 4 == 0 or year % 100 == 0 and year%400==0 else f"{year}is not an leap year"


# print(leap_year)











# Question : 2 Login Authentication using conditional statement.


# Assume you have a predefined username and password.
# write a program that prompts the user to enter a username:
# Both username and password are correct.
# username is correct but password is incorrect.
# username is incorrect.




# Answer : 2

# print("Login Authentication!!!!")
# username_key = "admin"
# password_key = "1234"

# input_username = input("Enter Username :")
# # print(input_username == username)
# input_password = input("Enter Password : ")

# if input_username == username_key:
#     if input_password == password_key:
#         print(f"Login Successfull!!!! ,{username} and {password} is correct")
#     else:
#         print("Password is incorrect")
# else:
#     print("Username is incorrect")








# Question : 3 Admission Eligibility
# - A university has the following Eligibility criteria for admission:
# - Marks in Mathematics >= 65
# - Marks in  Physics >= 55
# - Marks in Chemistry >= 50
# - Total marks in all three subjects >= 180 OR total marks in Mathematics and Physics >= 140.
# Write a program that takes marks in three subjects as input and prints whether the student is eligible for admission.



# Answer : 3

# print("Admission Eligibility :")

# Mathematics_marks = int(input("Enter Marks in Mathematics:"))
# Physics_marks = int(input("Enter Marks in Physics:"))
# Chemistry_marks = int(input("Enter Marks in Chemistry:"))
# total_marks  = Physics_marks+Mathematics_marks+Chemistry_marks
# Mathematics_marks_and_Physics_marks = Mathematics_marks + Physics_marks


# eligible_student = "You are eligible" if ( Mathematics_marks >= 65 and Physics_marks >= 55 and Chemistry_marks >= 50 ) or (Mathematics_marks_and_Physics_marks >= 140) else "You are not eligible"

# print(eligible_student)






# print("LEAP YEAR PROGRAM : ")

# leap_year = int(input("Enter a Year : "))

# if leap_year % 4 == 0 :
#     print(f"{leap_year} is an leap year.")

# elif (leap_year % 400 == 0 & leap_year % 100 != 0):
#     print(f"{leap_year} is an leap year")


# else :
#     print(f"{leap_year} is not an leap year.")
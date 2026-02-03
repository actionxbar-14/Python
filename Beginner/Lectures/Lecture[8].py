
                             # TOPIC : Conditional Statements
                                    #    [if - elif - else]


# Conditional statements : 
# 1. 'if' statement 
# 2. 'if-else' statement
# 3. 'if-elif-else' statement
# 4.  Nested 'if else' statement
# 5.  Conditional Expressions(Ternary Operator)





# 1. if : 

# ::syntax : 

# if condition :
   #code to execude if the condition is true.


# Ex : 
# a = 25
# b = 108
# if b > a :
#     print("b is greater than a")

# age = int(input("enter your age:"))
# if age > 19:
#     print("you are adult") 

#output : gives statement inside print statement if the age is greater than 19. / the statement inside if statement is true.

# print(10>100) #output : False










# 2. if-else : 
# ::syntax : if condition:
#              # code to execute if the condition is true.
#            else:
#              # code to execute if the condition is false.

# ex:

# temperature = int(input("enter the temperature :"))
# if temperature > 30:
#    print("its hot today") #output : gives the statement inside print statement if the condition inside if statemnet is true.
# else:
#     print("the day is normal")  #output : gives the statement inside print statement if the condition inside if statemnet is false.












# 3. if-elif-else :
# ::syntax : if condition1:
#              # code to execute if the condition1 is true.
#            elif condition2:
#              # code to execute if the condition1 is false and condition2 is true.
#            else:
#              # code to execute if both condition1 and condition2 are false.

# ex:

# marks = int(input("enter the marks of student :"))

# if marks > 90:
#     print("you are getting an goverment college")
# elif marks > 75 and marks < 90:
#     print("you are getting an semi-goverment college")
# else:
#     print("you are getting an private college")












# 4. Nested if-else:
# ::syntax : if condition1:
#              # code to execute if the condition1 is true.
#              if condition2:
#                  # code to execute if the condition2 is true.
#              else:
#                  # code to execute if the condition2 is false.
#            else:
#              # code to execute if the condition1 is false.
            
# ex:

# marks = int(input("enter your marks:"))
# if marks>90:
#     if(marks>95):
#         print(f"you are getting a scholarship , because you got {marks}%")
#     else:
#         print(f"you are getting a prize because you scored {marks}%")
# elif marks > 75 and marks < 90:
#     print(f"you are getting 2nd devision result because you scored {marks}%")

# else:
#     print(f"you scored only {marks}%!")



# print("Here you can get details about an integer number :")
# number = int(input("enter your number:"))

# if number > 0:
#     if number % 2 == 0:
#         print(f"{number} is an positive even integer")
#     else:
#         print(f"{number} is an positive odd integer")
# elif number < 0:
#     if number % 2 == 0:
#         print(f"{number} is an negative even integer")
#     else:
#         print(f"{number} is an negative odd integer")
# else:
#     print(f"{number} is not an positive neither negative integer")












# 5.  Conditional Expressions(Ternary Operator) :
# ::syntax : value = condition/expression if true else false

# ex:

# age = int(input("enter age:"))
# status = f"{age} is under Adult catogery" if age >= 18 else f"{age} is under Minor catogery"
# print(status)


#HW :

# a = None
# print(a) #output : None
# print(type(a))  #output : <class 'NoneType'>

# if a:
#     print("chal gya mtlb a true(1) hai")
# else:
#     print("nhi chala mtlb a false(0) hai")



# value = None  # ---> Here None equals to False
# value = (input("enter the value:")) ----> Here Input value equals to True

# if value:
#     print("Value is True")
# else:
#     print("Value is False")  #output : Value is False

# # NOTE: Assign kiya value ka to else chala , or input se liya to true diya.




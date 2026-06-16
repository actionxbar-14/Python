

# :: Youtube Playlist Content : 

# --> lecture-241 : EH-5( part - 2 ).
# --> lecture-242 : EH-6. 
# --> lecture-243 : EH-7. 
# --> lecture-244 : EH-8. 
# --> lecture-245 : EH-9. 


# _______________________________________________________________________________________________________________________________________ 



# :: Python raise keyword : 

# - An exception can be raised forcefully by using the raise clause in Python. 
# - raise statement is used when we want to throw exception for particular condition. 

# - Syntax : raise ExceptionName("exception message")


# - Ex_1 :  

# try:
#     age = int(input("Enter your age :")) 
#     if age < 0:
#         raise ValueError
#     print("Your age is :" , age)

# except ValueError:
#     print("Enter valid age :")



# print("rest of code")










# - Ex_2 :  

# try:
#     age = int(input("Enter your age :")) 
#     if age < 0:
#         raise ValueError("invalid age")
#     print("Your age is :" , age)

# except ValueError as var:
#     print(var)

# print("rest of code")








# _______________________________________________________________________________________________________________________________________ 


# :: Creating User-defined Exceptions : 

# - Steps :- 

# 1.) Create exception class and inherit it from Base Exception class. i.e : Exception  

# - Ex :  

# class InvalidAge(Exception):
#     pass 





# 2.) Raise InvalidAge exception for particular condition (age < 0) inside try block. 

# - Ex :   

# try:
#     if age < 0:
#         raise InvalidAge("message")




# 3.) Handle the exception using except block. 

# - Ex :  

# except Exception as obj:
#       print(obj)









# - Ex_1 :  write a python program for FiveDivisionError Exception. 

# class FiveDivisionError(Exception):
#     "This is Exception class called when five division error happens"
#     pass 


# try:
#     n1 = int(input("Enter first number :"))
#     n2 = int(input("Enter second number :"))
#     if n2 == 5 :
#         raise FiveDivisionError("can not divide by five")
#     div = n1 / n2 
#     print("division is :", div)

# except (FiveDivisionError , ZeroDivisionError) as var:
#     print(var) 



# print("rest of code")














# # - Ex_2 : (using __init__ method)

# class FiveDivisionError(Exception):
#     "This is Exception class called when five division error happens"
#     def __init__(self):
#         print("can not divide by five")


# try:
#     n1 = int(input("Enter first number :"))
#     n2 = int(input("Enter second number :"))
#     if n2 == 5 :
#         raise FiveDivisionError
#     div = n1 / n2 
#     print("division is :", div)

# except (FiveDivisionError , ZeroDivisionError) as var:
#     print(var) 



# print("rest of code")











# _______________________________________________________________________________________________________________________________________ 



# ::  Example of Exception handelling : 


# :--> Requirements : 

## Withdraw money from bank :
# - Balance in bank should not be less than 1000. 
# - User account will be blocked for an hour if user put 3 times wrong pin. 

# import time


# class BalanceExceptionError(Exception):
#     pass 


# class AttemptExceptionError(Exception):
#     pass


# attempts = 3

# def withdraw():
#     global attempts
#     saved_pin = 1234     #hard-coded
#     balance = 10000      #hard-coded
#     pin = int(input("Enter the PIN :"))
#     if pin == saved_pin:
#         try:
#             amount = float(input("Enter amount to withdraw :"))
#             temp_bal = balance - amount
#             if temp_bal < 1000:
#                 raise BalanceExceptionError("Insufficient balance")
#             else:
#                balance =  balance - amount
#                print("Remaining balance is:" , balance)
        
            
#         except Exception as e:
#             print(e)
    
#     else:
#         print(f"You entered wrong pin!! , you left {attempts} attempt! ")
#         ans = input("Do you want to continue (y/n) :")

#         if ans.lower() == 'y':
#             attempts -= 1
#             try:
#                 if attempts == 0:
#                     raise AttemptExceptionError("Too many attempts , you account is blocked for an hour")
#             except Exception as e:
#                 print(e)  
#                 time.sleep(3600)    
#             else:
#                 withdraw()



#         else:
#             print("Thank you!")
#             return 


# withdraw()







# _______________________________________________________________________________________________________________________________________ 




# :: How to use Exception Handelling in File Handelling and PDBC ( Python Database Conncetivity ) :



# --> Go to the Lecture_Practice folder / Others for practical.






# :-> How to use Execption_Handelling in File_Handelling  :


# - Ex : 



# f =  open(r"C:\Users\ANUBHAV\Program_Folders\Python\Intermidiate\Lectures\Lecture_Practice\Module_Practice\Exception_Handelling\leetcode.txt" , mode = 'r')

# #--> operation : 

# f.close()
# print("rest of code")   # it runs succussfully











# # - Ex :



# f =  open(r"C:\Users\ANUBHAV\Program_Folders\Python\Intermidiate\Lectures\Lecture_Practice\Module_Practice\Exception_Handelling\leet-code.txt" , mode = 'r')

# #--> operation : 

# f.close()
# print("rest of code")   # output :     f =  open(r"C:\Users\ANUBHAV\Program_Folders\Python\Intermidiate\Lectures\Lecture_Practice\Module_Practice\Exception_Handelling\leet-code.txt" , mode = 'r')
# FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\ANUBHAV\\Program_Folders\\Python\\Intermidiate\\Lectures\\Lecture_Practice\\Module_Practice\\Exception_Handelling\\leet-code.txt'


# NOTE: by entering wrong file name error occurs and flow of execution is stopped. So we have to use Exception handelling. 






# _______________________________________________________________________________________________________________________________________ 





# :--> How to use Exceptional Handelling in PDBC : 

# import mysql.connector 

# try:
#     mysql.connector.connect(
#     user = 'root',
#     password = 'shantanu@1234'
#     host = 'localhost'
#     port = 3305
#     database = 'student'


# )
    

# except:
#     print("can not connect")







# _______________________________________________________________________________________________________________________________________ 


# NOTE : Jab ham kisi program ko exception handelling ke method se handle nahii krte toh Python interpreter internally kaise work krta hai :

# -> The interpreter calls sys.excepthook() with three arguments:

# 1.) The exception class.    [ Ex :  TypeError ]
# 2.) exception instance/value [ Ex : Traceback(most recent call last) : ]
# 3.) a Traceback object.   [ Ex : full error jo terminal prr print hota hai as an object. ]


# - This function prints out a given traceback and exception to sys.stderr. 


# -Ex :  

# def adder():
#     print(100 + 'hello')

# adder() #output : 

# Traceback (most recent call last):
#   File "c:\Users\ANUBHAV\Program_Folders\Python\Intermidiate\Lectures\Lecture[48].py", line 365, in <module>
#     adder()

#     ~~~~~^^
#   File "c:\Users\ANUBHAV\Program_Folders\Python\Intermidiate\Lectures\Lecture[48].py", line 363, in adder
#     print(100 + 'hello')


#           ~~~~^~~~~~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'





# NOTE :  iske liye ham python ka Excepthook ko use krenge : 



# :: Excepthook in Python : 

# -  In an interactive sessions this happens just before control is returned to the prompt. 

# - Syntax : 

# inside sys module  

# def excepthook(exc_type , exc_value , exc_traceback):





# :--> What can we do :

# -- We can customize output by overriding this function. 
# -- sys.excepthook() handles uncaught exceptions.  
# -- execution remain stop only error format can be changed by programmer. 


# - Ex : 

#--> excepthook ko ham iss program mai format_traceback ki tarah banayenge.


# import sys    


# def format_traceback(exc_type , exc_value , exc_traceback):
#     print("Something went wrong!")
#     print(exc_type)  # output : <class 'TypeError'>
#     print(exc_value)  # output : unsupported operand type(s) for +: 'int' and 'str'
#     print(exc_traceback)  # output : <traceback object at 0x000001C1601C9500>


# sys.excepthook = format_traceback

# def display():
#     print(1 + "hello")


# display()











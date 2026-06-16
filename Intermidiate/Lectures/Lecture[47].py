
# :: Youtube Playlist Content : 

# --> lecture-236 : What is Exceptions Handelling (EH - 1).
# --> lecture-237 : EH-2. 
# --> lecture-238 : EH-3. 
# --> lecture-239 : EH-4. 
# --> lecture-240 : EH-5 (part - 1). 


# __________________________________________________________________________________________________________________________________________



# :: Exception : 

# - An excepition is an event which occurs during the execution of program that disrupts normal flow of program. 
 
# - Situation that Python can't cope with it. 




# :--> Why it is Dangerous  : 

# 1.) Lead to sudden termination of Program. 
# 2.) Can block the application. 
# 3.) Data loss problem can occur. 
# 4.) Corrupt data files. 






# :--> Exception v/s Error : 

# - Errors can't be handeled. 
# - Exceptions can be handled using exception handling syntax. 

# - Ex:  print("hello)  #--> syntaxError. 



# __________________________________________________________________________________________________________________________________________



# :: Exception Handelling : 

# - Python Performs Exception handelling by the following 4 blocks :- 

# 1.) try block 
# 2.) except block 
# 3.) else block 
# 4.) Finally block







# :--> Syntax : 



# try:
#     #code containing exceptions ( suspicious code )
# except [ ExceptionName ]:
#     #code to handle exceptions( if occurred ) 
# else: 
#     #code to execute if no exceptions occurred 
# finally: 
      #Always excecuted


# NOTE :  try block and except block is mandetory blcks but the else and finally blocks are optional. 


# - Ex :    ( without Exception handelling )

# num1 = int(input("Enter first num :"))
# num2 = int(input("Enter second num :"))

# div = num1 / num2

# print("rest of code")  

# NOTE : Without exception handelling if error occurs then it stops the upcoming code execution.









# - Ex :  ( with exception Handelling )

# num1 = int(input("Enter first num :"))
# num2 = int(input("Enter second num :"))

# try:
#     div = num1 / num2
#     print(div)
# except ZeroDivisionError:
#     print("divide by zero is not possible")



# print("rest of code")  


# NOTE : With exception handelling if error occurs then it gives the code of except block and continue the upcoming code execution.











# :--> Handelling Multiple Errors : 
# - By making multiple except writing stratigies.  








# - Ex_1 :  ( Handelling multiple exception Handelling )  

# num1 = int(input("Enter first num :"))
# num2 = int(input("Enter second num :"))

# try:
#     div = num1 / num2
#     print(di)   #----> syntaxError
# except :
#     print("divide by zero is not possible")



# print("rest of code")  


# NOTE : Here for every exception the except block return 'something went wrong'.















# - Ex_2 :  ( Handelling multiple exception Handelling )  

# num1 = int(input("Enter first num :"))
# num2 = int(input("Enter second num :"))

# try:
#     div = num1 / num2
#     print(di)   #----> syntaxError
# except ZeroDivisionError:
#     print("divide by zero is not possible")
# except NameError as obj:
#     print(obj)


# print("rest of code")  


# NOTE : Here for every exception the except block return 'name 'di{syntax error content}' is not defined'.











# - Ex_3 :  ( Handelling multiple exception Handelling )  

# num1 = int(input("Enter first num :"))
# num2 = int(input("Enter second num :"))

# try:
#     div = num1 / num2
#     print(di)   #----> syntaxError
# except (ZeroDivisionError,NameError) as obj:
#     print(obj)
# except NameError as obj:
#     print(obj)


# print("rest of code")  





# NOTE : Here for every exception the except block return the main cause of errir written inbuilt , like for ZeroDivisionError it prints 'division by zero' and for NameError it prints 'name 'di' is not defined'. 











# - Ex_4 : ( using else and finally block )



# num1 = int(input("Enter first num :"))
# num2 = int(input("Enter second num :"))

# try:
#     div = num1 / num2
#     print(div)
# except ZeroDivisionError:
#     print("divide by zero is not possible")
# else:
#     print("an exception did not occur")
# finally:
#     print("always executed")



# print("rest of code")  




# NOTE : 

# - else block and finally block are optional. 
# - We can have multiple except block for one try block. 
# - Finally block always execcuted. 
# - except block :- if exception occurs.
# - Else block :- if exception does not occur. 












# __________________________________________________________________________________________________________________________________________



# :: Printing Exceptiono name : 

# 1.) Using exception class object. 
# 2.) Using sys module. 




# 1.) Using exception class object : 



# - Ex : 

# num1 = int(input("Enter first number :"))
# num2 = int(input("Enter second number :")) 

# try:
#     div = num1/num2 
#     print("Division is :" , div)
# except ZeroDivisionError as e:
#     print(e.__class__)  # output : <class 'ZeroDivisionError'>
#     print(e)  # output : division by zero


 
# print("Rest of code") 

# ZeroDivisionError : Division by zero 








# # - Ex :  ( using Exception keyword )

# num1 = int(input("Enter first number :"))
# num2 = int(input("Enter second number :")) 

# try:
#     div = num1/num
#     print("Division is :" , div)
# except Exception as var:
#     print(var.__class__)  # output :  <class 'NameError'>
#     print(var)  # output : name 'num' is not defined


 
# print("Rest of code") 











# 2.) Using sys module. 

# - sys.exc_info ak module hai or uska 0th index batata hai class ka name , and 1st index batata hai value of the exception. 

# - Ex : 


# import sys 


# num1 = int(input("Enter first number :"))
# num2 = int(input("Enter second number :")) 

# try:
#     div = num1/num2
#     print("Division is :" , div)
# except:
#     print(sys.exc_info()[0])  # output : <class 'ZeroDivisionError'> / <class 'NameError'>
#     print(sys.exc_info()[1])  # output : name 'num' is not defined / division by zero
  

# print("Rest of code")

# ZeroDivisionError : Division by zero\





# NOTE :  Exception jo first occur hoga program execution ke time wahi priority wise print hoga , for this code as syntax first checked and then division performs , so nameError occcurs first then the ZeroDivisionError. 



# __________________________________________________________________________________________________________________________________________




# ::  Python Exception Hierarchy : 

# - When an error occurs then Python performs mainly three operations:-

# 1.) it calls the respective class exception. 
# 2.) it calls the constructor of that class. 
# 3.) it execute the Raise statement which are directed to responsible for stopping the execution of program .  


# :--> Hierarchy : 


# :-> BaseException :-

# 1.  Exception                      2. SystemExit                  3. GeneratorExit                     4. KeyboardInterrupt 




# 1.) Exception :-

# - Attribute Error 
# - Arithmetic Error  :      1. ZeroDivisionError              2. FloatingPointError                   3. OverFlowError
# - NameError 
# - LookupError       :      1. IndexError                     2. KeyError 
# - TypeError 
# - ValueError 
# - OsError           :      1. FileNotFound Error             2. PermissionError                      3. TimeoutError
# - EOFError     









# __________________________________________________________________________________________________________________________________________





# ::  Types of Exception Handelling : 

# 1.) Built-in Exceptions 
# 2.) User-defined Exceptions 






# 1.)  Built-in Exception : 

# - These are the exceptions that are directed and there class and there values are built-in by the Python interpreter. 
# -  list of built-in functions: 

# --> ValueError : Occurs when input argument / value to function is inappropriate. 
# --> IOError:  Happens when file can not be opened. 
# --> KeyboardInterrrupt : Happens when you enter CTRL+ C/DELETE/ESC during normal flow of program. 
# --> ImportError :  Happens when requested module is not present. 
# --> EOFError : Happens when end of file condition is reached without reading any data by input(). 
# --> ZeroDivisionError : Happens when you try to divide by zero. 
# --> IndexError :  Happens when you try to access index beyond the limit. 
# --> IndentationError : Happens when you give incorrect indentation to code. 
# --> TypeError : Incorrect data type related error. 
# --> OverflowError : Happens when result exceeds memory limit of specified data type. 











# 2. User-defined Exceptions : 

# - These are the exceptions which are directed to create by mainly python user. 






# __________________________________________________________________________________________________________________________________________






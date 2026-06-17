

# :: Youtube Playlist Content : 

# --> lecture-246 : EH - 10 ( thoda niche hai playlist mai ).
# --> lecture-247 : EH-11. 
# --> lecture-248 : EH-12. 
# --> lecture-249 : EH-13 (Exercise). 
# --> lecture-250 : EH-14. 


# _______________________________________________________________________________________________________________________ 



# NOTE: What will happen when exceptions occur in one thread? will it impact other threads?

# - Answer : No , it does not effect other thread execution because thread have their seperate execution flow. 


# :: Exceptions in Multi-threading : 


# - Ex :  ( without exception handelling , ,it gives error for the display() and then continue the show() function execution )



# from threading import * 
# from time import sleep 

# def display():
#     for i in range(4):
#         sleep(0.1)
#         print("hello" + 10)

# def show():
#     for i in range(4):
#         print("hello")
#         sleep(0.5)



# t1 = Thread(target = display)
# t2 = Thread(target=show)


# t1.start()
# t2.start()


# t1.join()
# t2.join()

# for i in range(4):
#     print("Bye")












# :--> What happens for exception in thread ? 

# - The interpreter calls threading.excepthook() with one argument i.e named tuple with 4 argument. 

# 1.) The exception class.
# 2.) Exception instance / value.
# 3.) A traceback object. 
# 4.) Thread name. 




# NOTE:  

# --> For main thread :  sys.excepthook runs.
# --> For created thread :  threading.excepthook runs. 









# ________________________________________________________________________________________________________________________________________



# :: Exception handelling while taking input : 

# - Ex: 

# def get_square():
#     try:
#         num = int(input("Enter the number :"))   #--> suppose input : hello
#         print("Square is :" , num**2)
#     except Exception as e:
#         print(e) 
#         get_square()



# get_square()

# print("rest of code")








# NOTE : A pitfall in Exceptiono handelling [while using file handelling]: 


# - Ex : [ here if data.txt is not present in the directory then , python interpreter gives error and does not create the f variable]


# try:
#     f = open('data.txt' , mode = 'r')
#     my_data =  f.read()
#     print(my_data)

# except Exception as e:
#     print(e)
# else:
#     print("read operation success")
# finally:
#     f.close()
# output : 

#     f.close()
#     ^
# NameError: name 'f' is not defined








# - Ex :  [ using exception handelling in the finall]y block also ] 


# try:
#     f = open('data.txt' , mode = 'r')
#     my_data =  f.read()
#     print(my_data)

# except Exception as e:
#     print(e)
# else:
#     print("read operation success")
# finally:
#     try:
#         f.close()
#     except:
#         pass


# print("rest of code")











# ________________________________________________________________________________________________________________________________________



# Question : Write a Python program that will ssum numbers present in gives list of data by use of exception handelling.  

# if input :  [1, 'a' , 'b' , 3] 
# then output is : 
# - item 'a' is not a number. 
# - item 'b' is not a number. 
# 4 




# - Answer : 



# def sum_of_int_list(my_list):
#     total = 0
#     for element in my_list:
#         try:
#             int(element)
#         except:
#             print(f"item {element} is not a number")
#         else:
#             total += element
#     return total



# print(sum_of_int_list([1 , 'hello' , 's' , 3]))


# output :  

# item hello is not a number
# item s is not a number
# 4













# Question : 2  find the total_likes 




# def total_likes():
#     reviews = [
#         {'Image' : 3 , 'Like' : 20 , 'Comment' : 10} ,
#         {'Like' : 15,  'Comment' : 8 , 'Share' : 10} ,
#         {'Image' : 7 , 'Comment' : 16 , 'Share' : 37} ,
#         {'Image' : 6 , 'Like' : 10 , 'Comment' : 9}

#     ]

#     total = 0 
#     for review in reviews:
#         try:
#             total += review['Like']
#         except:
#             pass 
#     return total 




# print(total_likes()) # output : 45





# ________________________________________________________________________________________________________________________________________




# :: Exercise on Exception handelling : 


# - Define a function named calculator. 
# - It will ask for a mathematical operation from the user ,
# - An operation is something like this : 6 * 5. 
# - This function will get this input and do the necessary calculation , and return the result as follows : 6 * 5
# - The operation type can only be one of these : + , - , * ,  /. 



# :--> Exception handelling for possible errors :- 

# 1.) Two operands and operator should be there. Else , raise exception. 
# 2.) operator must be part of ( + , = , * , /). 
# 3.) Operands must be castable into float. 
# 4.) zeroDivisionError while division. 





# - Solution : 

# class OperationError(Exception):
#     pass 

# class OperatorError(Exception):
#     pass 

# def calculator():
#     operations = ( '+' , '-' , '*' , '/')
#     try:
#         user_input = input("Please enter an operation :")  #  2 * 3 [ 2 , '*' , 3]
#         element = user_input.split()
#         if len(element) != 3:
#             raise OperationError("Please enter two operands and an operator in between separated by spaces!")
#         operator = element[1]
#         if operator not in operations:
#             raise OperatorError(f"{operator} is not valid , please enter an operator from {operations}")
#         num1 = float(element[0])
#         num2 = float(element[2])
#         if operator == '/' and num2 == 0:
#             raise ZeroDivisionError("Can't divide by zero")
#     except Exception as e:
#         print(e)
#         print("try Again!")
#         calculator()
#     else:
#         if operator == '+':
#             result = num1 + num2 
#         elif operator == '-':
#             result = num1 - num2 
#         elif operator == '*':
#             result = num1 * num2 
#         elif operator == '/':
#             result = num1/ num2 
#     finally:
#         return  f"{num1} {operator} {num2} = {result}"

# final_result = calculator()

# print(final_result)







# ________________________________________________________________________________________________________________________________________




# :: Question :  We have a dictionary of cricket teams and number points. 


# points_table =  {
#     'India' : 8 , 
#     'Pakistan' : 6 , 
#     'South Africa' : 5 , 
#     'Bangladesh' : 4 , 
#     'neitherland' : 2 , 
#     'Bermuda' : 2
# }

# --> Ask user to enter country name , if country exists in the dictionary , print its points with proper message. 

# --> If not , print "No such country in points table"

# --> It will ask user again and again untill it finds name in dicitionary. 





# - Answer :  


# points_table =  {
#     'India' : 8 , 
#     'Pakistan' : 6 , 
#     'South Africa' : 5 , 
#     'Bangladesh' : 4 , 
#     'neitherland' : 2 , 
#     'Bermuda' : 2
# }

# while True:
#     try:
#         name = input("Enter the country name:")  # Bermuda 
#         points = points_table[name]
#         print(f"{name} has got {points} points")  
#     except:
#         print("No such country")
#     else:
#         break



















# Question : Define a function named give_me_a_key :

# -> It will ask user to press any key on the keyboard. 
# -> If the key that the user pressed is: 
#   -->1.  a number :- return its square. 
#   -->2.  a letter :- return its capital form. 
#   -->3.  neither a number nor a letter :- return the key itself. 


# NOTE :  use only try-except-else-finally here. 


# Answer :  

# def give_me_a_key():
#     key = input("Press a key on keyboard :")
#     result = ''
#     try:
#         num = int(key)
#     except:
#         if key.isalpha():
#             result = key.upper()
#         else:
#             result = key
#     else:
#         result = num  ** 2
#     finally:
#         return result 
    

# print(give_me_a_key())





# ________________________________________________________________________________________________________________________________________



# :: assert statement  in Exception Handelling: 

# - An assert statement in Python is used to test an expression in the program code. 
# - Syntax : assert Expression[ , arguments]. 



# - Ex :  

print("Use of assert statement :")

def ValidAge(age):
    assert(age >= 0) , "age can't be negative"
    print("Your age is:" , age)

ValidAge(20)  # output : Your age is: 20

ValidAge(-20)  # output :   assert(age >= 0) , "age can't be negative"
#            ^^^^^^^^
# AssertionError: age can't be negative


# :: Youtube Playlist Content : 

# --> lecture-26 : Type Casting in Python.
# --> lecture-27 : print() function Arguments. 
# --> lecture-28 : input() function in Python. 
# --> lecture-29 : Python Assignment - 2. 
# --> lecture-30 : Types of Errors in Python / Handelling Errors in Python.



# _____________________________________________________________________________________________________________________


# :: Type Casting :-

# - Converting the value of one data type to another data type is called 'type casting' or 'type conversion'. 

# - Types :

# 1. Implicit type conversion. 
# 2  Explicit type conversion. 



# 1. Implicit type conversion :
# - In Implicit type conversion , Python automatically converts one data type to another data type. 
# - Generally , Python Promotes conversion of lower datatype to higher datatype to avoid data loss. 



# - Ex: 1

# x = 124   #--> int
# y = 12.4  #--> float

# z = x + y

# print(z)# 136.4 (float) 

# # NOTE: int < float < str




# - Ex : 2


# x = "1.24"  
# y = 12 

# print(x + y) 
# Output :   print(x + y)
#           ~~^~~
# TypeError: can only concatenate 
# str (not "int") to str

# _____________________________________________________________________________________________________________


# 2. Explicit type conversion :- 
# - Programmer converts one data type to another data type. 
# - We have predefined functiona for explicit type conversion. 
# - int , float , complex. [ premitive data type]. 
# - str , list , tuple. [sequential data type].

# NOTE :
# --> interconversion between premitive and sequential data type is not possible. 
# --> only premitive int , float can be convertable into str .
# - Type conversion function :

# --> int(value)
# --> float(value)
# --> str(value)
# --> complex(value)
# --> list(value)
# --> tuple(value)

# - Ex :



# value = 12.5
# print(value)  #--> 12.5
# print(type(value))
# value1 = int(value)
# print(value1)  #--> 12






# value = '12'
# print(type(value))  #--> <class 'str'>

# # value1 = int(value) #--> converting str to int.
# value2 = float(value) #--> converting str to float. 
# # print(type(value1)) #--> <class 'int'>
# print(type(value2))  #-->  <class 'float'>






# value = '12.5'

# print(type(value)) #--> <class 'str'>

# value2 = float(value)  #--> converting str to float

# print(value2)  #--> 12.5
# print(type(value2))  #--> <class 'float'>






# value = 12.5

# print(str(value))
# print(type(str(value)))  #--> <class 'str'>









# value = "hello"

# print(value)
# value1 = list(value)

# print(value1) # output : ['h', 'e', 'l', 'l', 'o']   







# value = 12.4 
# print(value)

# value1 = complex(value) 
# print(value1)  #--> (12.4+0j)


# value2 = complex(value , 3.2)
# print(value2)  #--> (12.4+3.2j)


#  _____________________________________________________________________________________________________________


# :: print function() :-

# - The print() function prints the given object to the standard output device (screen) or to the text stream file . 
# - syntax : print(*object , sep = '', end = '\n' , file = sys.stdout , flush = False)


# --> * objects[multiple objects] : objects to the printed. * indicates that there may be more than one object. 

# --> sep : objects are seperated by sep. Default value : ''. 

# --> end : end is printed at last. Default is '\n'. 

# --> file : uses write method to write in file , default is sys.stdout. 

# --> flush : If True , object is flushed, flushed means object ko permanently store krna memory mai. Default value is False. 


# --> Ex :

# :--> objects , sep :

# print("Hello" ,20 ,sep = '-')  #--> Hello-20

# print("Hello", 20, sep = '\t')  #--> Hello   20

# print("hello" , 20 , sep = "@$")  #--> hello@$20



# :--> objects , sep , end :

# print("Welcome" , sep = "-" , end = "")
# print("to", sep = "-" , end = "")
# print("codeYug")

# output : WelcometocodeYug




#  _________________________________________________________________________________________________________


# ::  Taking input from user :- 
# - Python provides one inbuilt function for taking input from user. 
# - Syntax : input([prompt])
# - Prompt :- it's a message , representing a default message before input.It is optional. 


# - Ex :

# print(print())  #--> None

# :-> Explanation :
#-> The code print(print()) is a nested function call. Here's a step-by-step breakdown of what happens during execution:

# 1. The inner print() is executed first. Since print() is called without any arguments, it doesn't output anything to the console.

# 2. The return value of the inner print() is None, as it is the default return value for a function that doesn't explicitly return a value.

# 3. The outer print() is then executed with the return value of the inner print(), which is None.

# 4. The outer print(None) outputs None to the console.

# 5. At the point where the debugger stopped, the line print(print()) has just finished executing. The inner print() has already executed and output nothing, and the outer print() has output None to the console.



# - Ex :

# name = input(print())
# print(name)  #--> None and the whatever user gives input

# :-> Explanation :

# 1. print() is executed first because it's inside the input() call.

# 2. print() without any arguments prints a newline character to the console and returns None.

# 3. The return value of print(), which is None, is then passed to input().

# 4.input(None) waits for the user to enter a value and then returns it.

# 5. The user enters "anubhav", which is stored in the name variable.



# ____________________________________________________________________________________________________


# :: Python Assignment - 2 :-



# Question : 1 What is printed when the following statement executed ? 

# x = 100 
# y = 50 
# print(x and y)

# Answer : 50 (because in the case of and operator right operand is printed.) 





# Question : 2 what is printed when the following statement is executed ? 
# x = 10 
# print(x > 3 and x < 9)

# Answer :  False ( because x < 9 is false statement , as 10 < 9 is not possible)





# Question : 3 Which of the following operator is correct for power(x^y) ?
# a) X^y 
# b) x^^y 
# c) x**y 
# d) None

# Answer : c) x**y





# Question : 4 What is printed when the following statement executed ?
# y = 10
# x = y += 2
# print(x)

# Answer :     x = y += 2
#           ^^
# SyntaxError: invalid syntax     







# Question : 5 What is printed when the following statement executed ?

# print(2*3**3*4)

# Answer : 2 * 27 * 4 = 216






# Question : 6 Which of the following is True about id() function ?

# a) id function returns memory address everytime. 
# b) id function returns unique identity number of objects. 
# c) id() returns integer value. 
# d) Both a and b 



# Answer : 
# --> for the case of c compiler it always returns memory address and also return uniqe and integer number of objects. 
# --> so option b and c are correct . 





# Question : 7 Select all correct float numbers :-

# a) 12.576   --> (true)
# b) -10.4    --> (true)
# c) 42e3     --> (true)
# d) -68.5e100 --> (true)




# Question : 8 What is the correct syntac for checking type of python object. 

# Answer : print(type(object))







# Question : 9 What is printed when following statement executed ?

print(100/25)  #----> 4.0

print(100%25)  #---->  0 



# Question : 10  What is printed when the following statements executed ?

# a = 6 
# b = 10 

# print(a == 6 and (not a == 10))

# Answer : True




# Question : 11 What will be printed in output window ?

# print(9//2) #--> 4

# print(9.0//2) #--> 4.0

# print(-9//2)  #--> -5







# Question : 12 What is printed when the following statements executed ? 
# x = 4j 
# print(type(x))


# Answer :   <class 'complex'>




# ___________________________________________________________________________________________________


# :: Errors in Python :- 

# --> Types of errors in Python. 
# --> Understanding error messages:
#     1. Value-error. 
#     2. Name-error. 
#     3. syntax-error. 
#     4. key-error. 
#     5. Type-error. 
#     6. Indentation-error. 
#     7. Index-error. 




# :--> Types of Errors in Python :
#     1. SyntaxError 
#     2. RuntimeError 
#     3. SymanticError 
#     4. TypeError
#     5. NameError
#     6. ValueError
#     7. IndentationError
#     8. IndexError


# 1. SyntaxError : syntax error is an error in syntax of code. 

# - Ex :
# print("hello"
#           print("hello"
#          ^
# SyntaxError: '(' was never closed






# 2. RuntimeError : runtime error comes during execution of program or at runtime.

# - Ex :

# print(3/0) 
#     print(3/0)
#           ~^~
# ZeroDivisionError: division by zero







# 3. symanticError(logic based error) : it comes when there is some logical error occurs in program , python does not show any error message for this , it simply does not provide the desired output because the logic is not correct.

# - Ex :

# a = 10
# b = 20 
# print(a+b/3)  # average of two numbers  






# 4. TypeError : occurs when you try to combine two objects of different types. 

# Ex : 
# a = 10 
# b = "20" 

# print(a+b)
#   print(a+b)
#           ~^~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'






# 5. NameError :  it occurs when we voilate the mistakes in the writing of the variables / values. 
# - Ex :

# a = 10 
# result = a+b 
# print(result)

#   result = a+b
#                ^
# NameError: name 'b' is not defined   




# 6. ValueError :  value is violating some limitation or not compatible. 

# Ex: 

# a = "hello"
# print(int(a))

#    print(int(a))
#           ^^^^^^
# ValueError: invalid literal for int() 
# with base 10: 'hello'





# 7. IndentationError : it occures when we do not follow correct indentation of python. 

# a = "hello"
#    print(int(a))
#     
# IndentationError: unexpected indent





# 8. IndexError : Trying to access item out of range. 

# Ex :

# a = [1,2,3,5]
# print(a[5])


#    print(a[5])
#           ~^^^
# IndexError: list index out of range   


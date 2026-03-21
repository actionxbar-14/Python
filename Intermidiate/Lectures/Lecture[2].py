
# :: Youtube Playlist Content : 

# --> lecture-11 : Some Built-in Functions.
# --> lecture-12 : Datatypes in Python. 
# --> lecture-13 : Built-in Datatypes in Python. 
# --> lecture-14 : Operators in Python. 
# --> lecture-15 : Membership/Identity Operators in Python.



# ______________________________________________________________________________________________________________________


# :: Topics :-

# - Function and function calls
# - id() function 
# - bin() function 
# - some important mathematical function 
# - How to get list of all built-in functions 






# num = int(input("Enter num : "))
# def square(num):
#     return num*num


# square_num  = square(num)

# print(square_num)



# ______________________________________________________________________________________________________________________

# :: id() function:-
# - Every Python value/object has its own unique identity number. It is called as id.
# - Cpython mai id() actual memory address hi return krta hai. 


# x = 100
# my_name = "Anubhav"
# print(id(x))  # Output: 140709521059720
# print(id(my_name)) # Output : 2929733095728


# ______________________________________________________________________________________________________________________



# :: bin() function:-
# - returns binary string equivalent to integer passed. 

# Ex:

# syntax : bin(integer)

# print(bin(10))  #output : 0b1010

# print(bin(10.2))  #output : 'float' object cannot be 
# interpreted as an integer

 


# ______________________________________________________________________________________________________________________


# :: pow() function :-

# --> syntax : pow(x,y,z)
#     x: base number
#     y: exponent 
#     z: modulous (optional)

# print(2**3)  # Output : 8

# print(pow(2,3,3))  # Output : 2


# ______________________________________________________________________________________________________________________



# :: round() function :-
# - returns rounded version of specified number. 
# - syntax :- round(number, digits)
# where , number : number specified for rounding
        # digits : number of decimals to use(optional argument and default is 0). 
        
        
# num = 4.6464
# print(round(num , 2))  # Output : 4.65


# ______________________________________________________________________________________________________________________


# :: abs() function :-
# - return absolute number. 
# - syntax : abs(value)

# print(abs(-2)) # Output: 2
# print(abs(0)) # Output: 0
# print(abs(2)) # Output: 2
# print(abs(complex(2,3))) # Output: 3.605551275463989


# ______________________________________________________________________________________________________________________

# :: how to get all built-in module in Python : 

# import builtins

# print(dir(builtins))

# # Output :
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 
# 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 
# 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 
# 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']


# ______________________________________________________________________________________________________________________



# :: Datatypes in Python :-

# - datatype is just a catogory of data. 
# - it defines possible operations :- 20 , "Anubhav"


# :Types:-

# 1. Numeric types  : int , float , complex(special type). 
# 2. Sequence types : str , list , tuple. 
# 3. Mapping types : dict 
# 4. Set types : set , frozenset
# 5. Boolean Type : Bool
# 6. Binary Types : bytes , bytearray
# 7. None type : NoneType

# ______________________________________________________________________________________________________________________

# :: type() function :-

# age = 22

# print(type(age)) # Output : <class 'int'>





# :: isinstance() function:-

# age = 22  #int

# print(isinstance(age,int))  # Output : True
# print(isinstance(age,float)) # Output : False



# ______________________________________________________________________________________________________________________

# :: Built-in Data types :-

# - Introduction to all data types , their syntaxes and usage. 
# - Checking datatype using type() function. 
# - Indexing in list , string , tuple. 





# --> Numeric - types:  ( int , float , complex ). 


# 1. int : 
# - Numeric types. 
# - contains integers. 
# - can be of any length. 
# - Ex : -3,-2,-1,0,1,2,3.... 
# - Ex : target = 180




# 2. float : 
# - Numeric type. 
# - floating point numbers. 
# - accurate upto 15 decimal places. 
# - Ex : 3.2 , 4.0 , 8.9 , -12.4 
# - Ex: temperature = 37.4 

# NOTE : Exponential data falls under "float" class. 
# - data = 2e / E7  --> ( 2 x 10**7 )




 
# 3. complex :
# -  written in form of a+bj. 
# - 'a' is real part and can be integer or float. 
# - 'bj' is an imaginary part and can be integer or float. 
# - Ex : c = 5 + 4j 







# --> Text type :  (str). 

# 1. string :
# - Sequence of characters. 
# - Anything enclosed in quotes. 
# - triple quotes are used for multi-line strings. 
# - For accessing the character of string : string_name[index_number]. 
# - Ex : name = "hello" or 'hello' or '''hello''' or """hello""". 
# - accessing character o : name[4].


# print("
# like
# share
# subscribe
      
# ")  Output : error


# print("""
# like
# share 
# subscribe
# """)
# Output :
# like
# share
# subscribe







# --> Sequence - types : ( list , tuple , dictionary , Set , frozenset , range ). 

# 1. list : []
# - list of data's having different data types. 
# - Ordered mutable sequence of items. 
# - items seperated by commas enclosed in [].
# - for accessing the elements : List_name[index_number]. 
# - Ex: 

# my_list = ['facebook' , 12.5 , 300 , 2+3j , [1,2,3]] 

# print(my_list)





# 2. tuple : ()
# - Collection of different data types. 
# - Immutable , ordered. 
# - Items are seperated with comma and enclosed with (). 
# - Ex : 
# my_tup = (12, 34.5 , "hello")
# print(my_tup)

# my_tup[2] = "Anubhav" --> Error ['tuple' object does not support item assignment]. 




# 3. dictionary :
# - Unordered set of key-value pairs. 
# - Key has primitive datatypes and value has any datatype. 
# - key-value pairs are seperated by comma. 
# - Ex : 

# my_dict = {
#         'sachin' : 110 , 
#         'kohli'  : 90,
#         'Dhoni'  : 100   
# }

# print(my_dict)







# 4. set : 
# - Unorderd collection of unique items. 
# - Items are written inside {} and seperated by commas. 
# - Items are not in order. 
# - Ex : 

# my_set = {1 ,2 , 3, 4 , "hello"}
# print(my_set)







# 5. range () :
# - It gives immutable sequence of numbers betweem start and stop. 
# - Syntax : range(start , stop , step)
# - Default starting is 0 and step is 1. 
# - Ex : range(0,11) --> 0,1,2.....10 . 

# print(list(range(1,10,2))) Output : [1, 3, 5, 7, 9]







# 6. None : 
# - None datatypes means an object that doesn't contain any value. 
# - Ex : 

# a = None
# print(a)--> None
# print(type(a)) -->  <class 'NoneType'>







# 7. bool : 
# - Two values, True and False. 
# - Used to determine given statements are true and false. 
# - True is non-zero and False is 0. 
# - Ex : 
# a = True
# print(a) --> True
# print(type(a))  --> <class 'bool'>



# ______________________________________________________________________________________________________________________


# :: Operators in Python :


# --> Operators :-
# - Symbols to carry out operations on operands(values or data). 
# - Ex : 
# 2 + 3 --> + is an operator and 2,3 are operands.  -> ( using Magic methods)


# :Types of operators :-

# 1. Arithmetic operators.
# 2. Comparison operators. 
# 3. Assignment and compound operators. 
# 4. Bitwise operators. 
# 5. Logical operatorss. 


# :--> some special operators(only exist in Python):
# - membership operators. 
# - identity operators. 
# - walrus operators.





# ___________________________________________________________________________________________________


# 1. Arithmetic operators :-
# - used to perform arithmetic operation on two or more operands. 
# - Below are arithmetic operators :

# --> + (addition). 
# --> - (Subtraction). 
# --> * (multiplication). 
# --> / (division). 
# --> % (Remainder). 
# --> // (floor division). 
# --> ** (exponentiation). 


# print(3%4) --> 3

# print(4%3) --> 1 

# print(10.0//3) ---> 3.0






# 2. Comparison operators :- 
# - compares values on either side of them and decide relation among them. 
# - return boolean value(True/False). 
# - Below are comparison operators :-

# --> greater than(>). 
# --> less than(<). 
# --> equal to (==). 
# --> not equal to (!=). 
# --> greater than or equal (>=). 
# --> less than or equal (<=). 





# 3.  Assignment operator(=) :-
# - Operators used to assign result of right expression / python object to left variable. 
# - syntax : variable = expression / Python object. 
# - Ex : num = 100





# 4. Compound operators :-
# - combination of other operator and assignment operators. 
# - Ex : a += 20 is same as a = a+10. 



# ___________________________________________________________________________________________________________



# :: Special Operators in Python :-

# - What are Python's special operators ?
# - Membership operators in Python. 
# - How membership operators works on dictionary ?
# - Identity operators in python. 
# - difference between == and 'is' operator. 





# --> Two types of special operators:
# 1. Membership operators. 
# 2. Identity operators.


# --> Why are they special ? 
# - C , C++ , JAVA do not have these operators. 
# - These operators firstly introduced in Python. 
# - Perl , Swift , PHP etc copied these operators. 


# --> Need of these operators :

# - Used in string (seqeuence / Collection of Characters). 
# - Used in List / Tuple ( Collection of different types of Values).
# - Used in dictinary ( collection of key-value pairs).add()










# :--> Membership operator :  (in / not in)

# - Checks availability or existense of a value in specified sequence. 
# - A sequence can be a string , tuple , list or dictionary.
# - in operator : return 'True' if specified value is the member of sequence / return 'False' if specified value is not a member of sequence.
# - not in operator : return 'True' if specified value isn't member of sequence / reuturn 'False' if specified value is member of sequence. 
# - Synatax : Python_value  special_operator  sequence . 




# - Ex :

# str1 = "Anubhav"
# print("a" in str1) #--> True
# print("A" in str1) #--> True
# print("f" in str1) #--> False


# print("a" not in str1) #--> False
# print("A" not in str1) #--> False
# print("f" not in str1) #--> True


# NOTE : How Membership operator works on dictionary and tricky questions ?


# 1. In dictionary membership operator iterate only key , so it ignores the value related to key in dictionary. 
# data = {
#         1 : "anubhav" ,
#         2 : "Pathak" 
# }

# print("anubhav" in data) #--> False

# print('1' in data) #--> False

# print(1 in data) #--> True


# print(1["anubhav"] in data) -- > error





# 2.  tricky question : 

# lst  = [1,2,4]
# lst1 = [[1,2,4] ,1,2,4]

# print(lst in lst)  #--> False (because it takes as [1,2,4] in [1,2,4])

# print(lst in lst1) #--> True ( because it takes as [1,2,4] in [ [1,2,4], 1,2,4] )










# :--> Identity operators : (is / is not)
# - identity operators compares id's of the objects. (takes as memory address in comparison of standard idle's)

# - used to know two objects are same or not. 

# - Ex :

# a = 100

# b = 100

# c = a

# num =  100

# d = "100"


# print(a is b) #--> True [ id(a) == id(b) ]

# print(c is a) #--> True [ id(c) == id(a) ]

# print(num is c) #--> True [ id(num) == id(c) ]

# print(d is c)  #--> False [ id(d) != id(c) ]





# print(a is not b) #--> False [ id(a) != id(b) ]

# print(c is not a) #--> False [ id(c) != id(a) ]

# print(num is not c) #--> False [ id(num) != id(c) ]

# print(d is not c)  #--> True  [ id(d) == id(c) ]




# NOTE : difference between is operator and == operator.

# :--> Ex : 1 ( for fixed value )
# a = 100
# print("id a : ", id(a))
# b = 100
# print("id b : " , id(b))


# print(a == b)  # True (  100 == 100  )
# print(a is b)  # True ( id(a) == id(b) )



# :--> Ex : 2 ( for mutable value )


data = [10,20,30,40]
print('id : data :- ' , id(data))  #-->  2526794437824


# print(id(data[0])) #--> 140707699418184   
# print(id(data[1])) #--> 140707699418184  
# print(id(data[2])) #--> 140707699418184  
# print(id(data[3])) #--> 140707699418184  



data1 = [10,20,30,40]
print("id : data1 :- ", id(data1)) #-->   2526796020160  


# print(id(data1[0])) #--> 140707699418184  
# print(id(data1[1])) #--> 140707699418184  
# print(id(data1[2])) #--> 140707699418184  
# print(id(data1[3])) #--> 140707699418184  




print(data is data1) # --> False

print(data == data1) # --> True


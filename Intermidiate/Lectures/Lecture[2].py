
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

age = 22  #int

print(isinstance(age,int))  # Output : True
print(isinstance(age,float)) # Output : False



# ______________________________________________________________________________________________________________________



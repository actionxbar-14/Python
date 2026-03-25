

# import example1

# print(example1.x)  # Output : 100

# print(example1.personal_info())  # Output : I am personal_info function and i am from the example module

# print(dir())  # Output : ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'example1']














# from example1 import * 



# x = 1000

# print(x)  # output : 1000 [overwritten value of x over 100]
# print(private_info())


# print(dir())  # Output : ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'display', 'personal_info', 'private_info', 'x']

# ____________________________________________________________________________________


# :--> after creating __all__ attribute in example1 module then :
# 



# 1.  _all__ = ['x']  (written in example1.py) :



# from example1 import *

# print(x) #--> 100
# print(private_info()) #--> erro
# print(dir())  # Output : ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',   'x']


# #NOTE : only function name written inside the __all__ attribute can access in the example.py.







# 2. _all__ = ['x' , 'private_info']  (written in example1.py) :

 
# from example1 import *

# print(x) #--> 100

# print(private_info())  #--> This is private info

# print(dir())  # -->  ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',   'private_info', 'x']





# 3.    _all__ = []  (written in example1.py) :

# from example1 import * 

# print(x) --> Error

# print(private_info) --> Error 


# print(dir())  --> []








# :: Advantages : 

# 1. prevent accidental import of private symbols. 
# 2. Explicitly define public api. 
# 3. Avoid Namespace pollution. 
# 4. Documentation and readability. 

# # import addition
# import add  as ad


# sum_of_two_number = ad.addition(1,4)
# print(sum_of_two_number)  # Output : 5












# from add import print_given_number


# print_given_number(2,4)  # Output : num1 = 2 , num2 = 4 












# from add import *

# print(addition(2,4))  # Output : 6

# print_given_number(6,8)  # Output : num1 = 6 , num2 = 8








# import math  as m 

# print(m.factorial(5))  # --> 120







# import add 

# print(dir(add))  # Output : ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'addition', 'display', 'print_given_number']     


# print(add.__file__)  # Output :c:\Users\hp\OneDrive\Desktop\Python\Intermidiate\Lectures\Module_Practice\add.py



# ____________________________________________________________________________________________________





# :--> Module level scope :

# import add

# print(dir(add))  #Output : ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
# # '__package__', '__spec__', 'addition', 'display', 'print_given_number']


# x = 10 

# def demo():
#     name = 'Anubhav'
#     print(dir())  # Output : ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
# # '__package__', '__spec__', 'addition', 'display', 'print_given_number']
    
    
    
# print(type(demo))   # Output : <class 'function'>  
# print(dir(demo))  # Output : ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']



# # ____________________________________________________________________________________________________


# :: Reloading module : 

# - using importlib module. 

import importlib
import add 

importlib.reload(add)
importlib.reload(add)
importlib.reload(add)

# output : total 4 baar print hoga 1st baar jab add module execute hoga and teen baar importlib module ki vajah se. 
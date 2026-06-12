
# :: Youtube Playlist Content : 

# --> lecture-216 : OOPS-26.
# --> lecture-217 : OOPS-27. 
# --> lecture-218 : OOPS-28 [part - 1 and part - 2]. 
# --> lecture-219 : OOPS-29. 
# --> lecture-220 : OOPS-30. 


# _______________________________________________________________________________________________________________________ 



# :: Operator Overloading : 
# - When same operator behaves differently depending on values. 
# - You can assign a new meaning to operators also and you can extend functionality of operators. 
# - You can change default behaviour of operator using over-riding. 

# -  Ex : 

# -  Consider  '+' operator.  
# -  "hello" + "world" = helloworld 












# - Ex : using numbers as an input

# num1 = 10 
# num2 = 20 

# print(num1 + num2) # output : 30

# print(num1.__add__(num2))  # output : 30

# print(int.__add__(num1 , num2))   # output : 30



# print(dir(int))  # output : ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']





#--> step - 1 : check datatype of left operand .    ( int )
#--> step - 2 : go in that class 
#--> step - 3 : call __add__() function 









# - Ex : using string as an input 


# num1 = "hello"
# num2 = "world"

# print(num1 + num2) # output : helloworld

# print(num1.__add__(num2))  # output : helloworld

# print(str.__add__(num1 , num2))   # output : helloworld



# print(dir(str))    # output : ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']









# _______________________________________________________________________________________________________________________ 




# ::  How to achieve Operator Overloading : 

# - Ex:  assigining + operator to perform addition between class methods. ( without overloading )

# class Book: 
#     def __init__(self , title , pages):
#         self.title = title 
#         self.pages = pages 


# b1 = Book('One indian girl' , 300)
# b2 = Book('making india awesome' , 200) 

# print("total number of pages :" , b1.pages + b2.pages)  # output :  total number of pages : 500









# # - Ex:  assigining + operator to perform addition between class methods. ( with overloading )

# class Book: 
#     def __init__(self , title , pages):
#         self.title = title 
#         self.pages = pages 

#     def __add__(self , other):   # ( b1 , b2 )
#        total = self.pages + other.pages
#        return total


# b1 = Book('One indian girl' , 300)
# b2 = Book('making india awesome' , 200) 

# print("total number of pages :" , b1 + b2)  # output :  total number of pages : 500







# - Ex:  ( adding multiple books )   #----> watch video




# class Book: 
#     def __init__(self , title , pages):
#         self.title = title 
#         self.pages = pages 

#     def __add__(self , other):   # ( b1 , b2 )
#        total = self.pages + other.pages
#        return Book('All books :' , total)
    

#     def __str__(self):
#         return str(self.pages)


# b1 = Book('One indian girl' , 300)
# b2 = Book('making india awesome' , 200) 

# b3 = Book('half girlfriend', 400)
# b4 = Book('girl in 105 room' , 300)


# print("total number of pages :" , b1 + b2 + b3 + b4)  # output :  total number of pages : 1200





# _______________________________________________________________________________________________________________________ 





# :: overloading the '>' operator : 


# - Ex :   ( without overloading )


# class Hotel:
#     def __init__(self , name , fare):
#         self.name = name 
#         self.fare = fare 


# h1 = Hotel('Taj hotel :' , 20000)
# h2 = Hotel('Panchratna :' , 10000)


# print(h1 > h2)   # Output :     print(h1 > h2)
#           ^^^^^^^
# TypeError: '>' not supported between instances of 'Hotel' and 'Hotel'








#  Ex :   ( with overloading )


# class Hotel:
#     def __init__(self , name , fare):
#         self.name = name 
#         self.fare = fare 

#     def __gt__(self , other):     #---> (h1 ,h2)
#         return self.fare > other.fare    # h1.fare > h2.fare 


# h1 = Hotel('Taj hotel :' , 20000)
# h2 = Hotel('Panchratna :' , 10000)


# print(h1 > h2)   # Output :  True   





# _______________________________________________________________________________________________________________________ 




# :: Method Overloading : 
# - Python mai pure method overloading ka concept exist nhi krta hai. isliye last written method ko hi recognise kiya jata hai , ex: add( 3 argument wala) ko recognize kiya or add(2 argument) wale ko ignore krr diya gaya. 

# - When a class contain two or more methods with same name but different behaviour is called as method overloading. 


# - Ex :   ( without method overloading it does not read both the add function )

# class Addition:
#     def add(self , num1 , num2):
#         print(num1 + num2)

#     def add(self , num1 , num2 , num3):
#         print(num1+num2+num3)




# a = Addition()


# a.add(10 ,20)  # output :  a.add(10 ,20)
# #     ~~~~~^^^^^^^^
# # TypeError: Addition.add() missing 1 required positional argument: 'num3'


# a.add(10 , 20 ,30)







# _______________________________________________________________________________________________________________________ 




# :: How to achieve method overloading :
# - To overload class methods , we need to write method's logic so that different code executes inside the method according to parameters provided. 


# - Ex : 

# class Calci:
#     def add(self , num1 = None , num2 = None , num3 = None):
#         if num1 != None and num2 != None and num3 != None:
#             print("Addition is :" , num1 + num2 + num3)
#         elif num1 != None and num2 != None:
#             print("Addition is:" , num1 + num2)
#         else:
#             print("incorrect parameters provided")


# c1 = Calci()
# c2 = Calci()
# # 
# c1.add(10  , 20)

# c2.add(10 ,20 ,30)







# - Ex :  


# class Area:
#     def area(self , l = 0, b = 0):
#         if l > 0 and b > 0:
#             print("area og rectange :" , l*b)
#         elif l > 0 and b == 0:
#             print("area of square is:" , l*l)


# a = Area()

# a.area(10)
# a.area(10 , 20)


    




# :: Youtube Playlist Content : 

# --> lecture-21 : Escape Sequence in Python.
# --> lecture-22 : ASCII and UNICODE in Python. 
# --> lecture-23 : Importing Module in Python/Module in Python. 
# --> lecture-24 : dir() in Python. 
# --> lecture-25 : _all_ Attribute in Python.


# ____________________________________________________________________________________________________________________

# :: Continuation character(\) :- 
# - We can extend Python statement over multiple lines by using continuation character(\). 
# - Ex :

# print(" Anubhav 
#       Pathak
#       ")   # ----> print(" Anubhav
#           ^
# SyntaxError: unterminated string literal (detected at line 18)



# print("Anubhav \
#     Pathak   ")   # Output : Anubhav     Pathak  



# x = 1+2+ \
# 3+4\
# +5

# print(x) # ---> 15






# ____________________________________________________________________________________________________________________


# :: Python Escape Sequences :- 
# - Characters that dosn't represent themselves when used inside string. 

# 1. newline character ('\n')
# 2. tab character ('\t')
# 3. backslash character ('\b')
# 4. carriage return ('\r')
# 5. character (\\)


# 1. newline character ('\n') :
# - gives a new line after where it written. 

# - Ex : 

#print("Anubhav Pathak")  #--> Anubhav Pathak
#print("Anubhav \n Pathak")  #--> Anubhav
                               # Pathak
                               






# 2. tab character ('\t') :
# - gives a varying multiple white space enter after where it written. 
# - isme 8 - 8 ka group banta hai. 

# - Ex :

#print("Anubhavv\tPathak")  #--> Anubhavv        Pathak
#print(len("Anubhavv\tPathak"))  #--> 15  (8 white spaces , kyuki Anubhavv -> 8 char total, so next grp ke liye \t ko 8 white space milega.)


#print("Anubhav\tPathak")  #-->  Anubhav Pathak
#print(len("Anubhav\tPathak"))  #--> 14  (1 white space , kyuki Anubhav -> 7 char total,so 8 ka grp banane ke liye \t ko 1 white space milega.)








# 3. backslash character ('\b') :-
# - jiss character ke agge lagayenge , uss character ko remove krke rest string return krega. 

# - Ex :

#print("Anubhav\bPathak") #--> AnubhaPathak  ('v' removed)
#print("Anu\bbhavPathak") #--> AnbhavPathak  ('u' removed)








# 4. carriage return (\r):-

# - the carriage return is a special character represented by the escape sequence \r. It moves the cursor to the beginning of the current line without advancing to the next line, allowing subsequent text to overwrite the existing content.

# - Ex :

#print("Anubhav\rPathak")  # output : Pathakv [A ko P se replace , n ko a se replace , u ko t se replace , b ko h se replace, h ko a se replace, v ko k se replace.]










# 5. Double slash character(\\) :-

# - \ slash print krne ke liye :- \\
# - \\ slash print krne ke liye :- \\\\
# - n slash print krne ke liye :- 2n slash



# - Ex :


# Escape sequence as normal text :-
# - I want to print this string as it is  :- "Hi , \n is a newline character and \t is for tab"

# and 

# I want to print this string as it is :- "Hi , \ is a backslash character and i want to print \\t\n"


# print(" Hi , \n is a newline character and \t is for tab")  
# output :  Hi ,
#  is a newline character and      is 
# for tab


# print(" Hi , \\n is a newline character and \\t is for tab")
# Output :  Hi , \n is a newline character and \t is for tab



#NOTE : 
# --> (raw string) - alternative of (\\) character :-

# print(r"Hi , \n is a newline character and \t is for tab")
# Output : Hi , \n is a newline character and \t is for tab 



# ________________________________________________________________________________________________________________________________

# :: Unicode character(\U) :- 
# - Python supports unicode + Ascii code point representation. 
# - In Python , the escape sequence \U is used to represent a unicode character in a string. 
# - It is followed by eight hexadecimal digits that represent the Unicode code point of the character. 
# - You can print a character using the unicode code point as well. 

# - Ex : 


# A :->  65  : \U00000041 (unicode representation)

#print('\U00000041')   #--> A 


# print('\U00000061')   #--> a 

# print("\U0001F609")  #--> 😉





# :--> ord and chr function :

# 1. ord function : character --> unicode number --> unicode code point
# Ex: 

# print(ord('A'))  # Output : 65 (A)

# print(ord('\U00000061'))  # Output : 97 (a)




# 2.  chr function : unicode number --> character. 
# Ex : 

# print(chr(65))   #--> A
 
# print(chr(57))   # --> 9






# ________________________________________________________________________________________________________________________________



# ::  Modules in Python :

# ----> Why Module ? :-
# - In any Project , we have to write big programs. It become difficult to manage and organize programs. 
# - So , we break down big program into small manageble and organized files having same logic. These files are nothing but modules. 
# - It provides reusability to our code. 



# ----> What are modules in Python ? :-
# - A file containing Python code is called as Python module. 
# - Module contains functions , definitions, class definitions , variables , runnable code, python statements , you want to include in your python main file. 

# - Ex :  go to Module_practice folder. 


# ----> Types of Modules in Python :

# 1. User defined modules :- modules created by us.  
# 2. Built-in modules :- modules given by python. 




# NOTE : 

# --> module is loaded only once regardless the number of times it is imported. 
# --> ak module ko ham kitni baar bhi add krr le voh execute ak baar in hoga ( only first time when it is imported).



 





# ________________________________________________________________________________________________________________________________




# :: dir() in Python :-

# - In Python , dir() is a built-in function that returns a list of all valid attributes(methods , variables and other attributes) for a given object. 

# - Syntax : dir([object])
# --> object :- value  , function , class , module etc . 
# --> object is optional. 
# --> default value :- list of names in the current local scope. 









# Ex : 1


# x = 100 
# print(x)

# name = "Anubhav"
# print(name)
# print(type(name))

# print(dir(name))
# output : ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'] 


# NOTE :

# -> __attribute__ , __methods__ having these type of syntax are called special methods and specail attributes. 
# -> all others are simple methods and attributes. 


# --> simple method and attribute :

# syntax : object_name.attribute()

# name = "Anubhav"
# print(name.upper())  # Output : ANUBHAV







# Ex : 2

# x = 100
# print(type(x))

# print(dir(x))

# Output : 
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']


#NOTE :

# -> __attribute__ , __methods__ having these type of syntax are called special methods and specail attributes. 
# -> all others are simple methods and attributes. 


# --> simple method and attribute :

# syntax : object_name.attribute()



# ________________________________________________________________________________________________________________________________


# ::  default value :- list of names in the current local scope.

# --> go to the practice_module folder. 


# ________________________________________________________________________________________________________________________________

# :: Re-loading module :

# - go to practice_module folder. 

# print(help("modules"))





# ________________________________________________________________________________________________________________________________ 



# :: __all__ variable/attribute :-

# - In Python, `__all__` is a list of strings that defines what names should be imported from the current module (Python file), to another file. Only the variables that are declared in that list can be used in that other file after importing this file; the other variables, if referenced, will throw an error.

# - Ex : go to Module_Practice folder. 


# :: Youtube Playlist Content : 

# --> lecture-51 : Complex Datatype in Python. 
# --> lecture-52 : String in Python.  
# --> lecture-53 : ord() and chr() function in Python. 
# --> lecture-54 : Indexing in Python String. 
# --> lecture-55 : String Slicing in Python. 



# _________________________________________________________________________________________________________________________


# :: Complex number :

# -> Complex numbers are especially used in electronics , optics , and quantum theory for describing waves and periodic phenomena. 
# -> Fourier transform uses complex numbers. 
# -> Audio signal processing in machine learning. 
# -> speech recognition system. 


# :--> Complex Datatype :

# - A complex number has real and imaginary part components. ( a + bj )
# - a and b can have any type of number. ( a = real part  , bj = imaginary part ). 
# - a (real part) is optional. 
# - Accessing real part :  var_name.real 
# - Accessing imaginary part :  var_name.imag 

# - Ex :

# num = 2+3j
# print(num)  #--> (2+3j)
# print(type(num))  #-->   <class 'complex'>

# - Ex :

# num = 4j
# print(num)  #--> 4j
# print(type(num))  #-->  <class 'complex'>


# - Ex :

# num = 2 + 4j
# print(num)  #--> (2+4j) 

# print(num.real)  #--> 2.0 
# print(num.imag)  #--> 4.0







# :: Python Complex() :-

# - Used to convert number or string to complex number. 
# - Syntax :  complex(real , imaginary)
# - Both are optional parameters and default are 0. 
# - Parameters can be of type int , float , str. 
# - Complex() arg is a malformed string. 

# - Ex :

# num = complex()  
# print(num)  #-->  0j
# print(type(num))   #--> <class 'complex'> 


# - Ex : 

# num  = complex(1,2)
# print(num)  #-->  (1+2j) 
# print(type(num))  #-->  <class 'complex'>     



# - Ex :

# num = complex(1)  
# print(num)    #-->  (1+0j)
# print(type(num)) #--> <class 'complex'>     



# - Ex :

# num = complex("1" , 2)
# print(num) 

# output :    num = complex("1" , 2)          pyt
#           ^^^^^^^^^^^^^^^^          o\y
# TypeError: complex() can't take secor1.nd arg if first is a string


# - Ex : 

# num = complex('s')
# print(num)

# output :     num = complex('s')              pyt
#           ^^^^^^^^^^^^              o\y
# ValueError: complex() arg is a malfor1.rmed string





# _________________________________________________________________________________________________________________________





# ::  String in Python : 

# - A string is a sequence of characters. Ex : "Anubhav"
# - Anything enclosed inside sinle quotes('') , double quotes except escape sequences is string. Triple quotes("""""") are also used but for multi-line strings and docstrings. 
# - string is a sequence of unicode characters. 

# :--> Creating string :

# my_str = 'hello'  
# my_str2 = "hello"  
# my_str3 = """hello , welcome
#            to Python"""
           
# print(my_str)  #--> hello
# print(my_str2) #--> hello
# print(my_str3)  #--> hello , welcome     
#         #    to Python



# Ex : assigning to a variable

# name = "anubhav"
# print(name) #--> anubhav
# print(type(name)) #--> <class 'str' >









# _________________________________________________________________________________________________________________________



# :: ord() function in Python : 

# - This inbuilt method returns an integer representing unicode for the given character. 
# - Syntax : ord(character)
# - Character :- a character (string of length one). 
# - Takes only one character. 
# - ord('A') to ord('Z') :- 65-90. 
# - ord('a') to ord('z') :- 97-122. 
# NOTE: 'a' --> U+0061 --> 97 --> 01100001 ( so 97 is the unicode for the character 'a').


# Ex :

# unicode_char = ord('A')

# print(unicode_char)  #--> 65

# print(ord('A')) #--> 65
# print(ord('a')) #--> 97
# print(ord('z')) #--> 122
# print(ord('#')) #--> 35










# :: chr() function in Python : 

# - This inbuilt method returns a character from an integer(representing unicode of character). 
# - Syntax : chr(integer)
# - Range of integer :- ( 0 --> 1,114,111) . 
# - If the value of integer is out of range , value-error will be raised. 

# - integer : integer value representing character unicode. 

# - Ex :

# chr_unicode = chr(103)

# print(chr_unicode)  #--> 'g'

# print(chr(103)) #--> g
# print(chr(97))  #--> a
# print(chr(98))  #--> b
# print(chr(35))  #--> #



# NOTE: ASCII is used in Python2 and UNICODE is used in Python3. 


# _________________________________________________________________________________________________________________________





# :: Accessing substring (characters) in string :-

# -> There are two ways :

# 1. Indexing  ( used to access individual [single] element of string .)
# 2. Slicing   ( used to access group of elements of a string. We can access range of characters using slicing. )












# 1. Index :

# - In Python , Every element is reperesented by index. 
# - In Python , blank space is also treated as a characater
# - To access single element , Python uses indexing. 
# - Syntax : var_name[index]
# - Ex :

# name = "code yug"

# print(name[0]) #--> c
# print(name[2]) #--> d
# print(name[5]) #--> y
# print(name[-1]) #--> g
# print(name[-4]) #--> blank space ( )
# print(name[-8]) #--> c




# NOTE :  
# 
# 1. string indexing does not allow the re assigning of the character , becuase string is immutable. 
# 2. string indexing does not allow the deleting of a character of a string .


# Ex :

# name = "code yug"

# name[2] = 's'
# print(name)

#  output : name[2] = 's'
#     ~~~~^^^
# TypeError: 'str' object does not support item assignment 



# Ex : 

# name = 'code yug'

# del name[2]

# print(name)

# output :   del name[2]
#         ~~~~^^^
# TypeError: 'str' object doesn't support item deletion   





# _________________________________________________________________________________________________________________________



# :: slicing :

# - To access a range of items ( sub-string ) , we will use 'slicing' . 

# - You can return range of characters using slicing. 

# - [:] is a slice operator. 

# - Syntax : var_name[start : stop : step]

# --> start : starting point of substring. 
# --> stop : it indicated end of string. 
# --> step : difference between indexing. 



# NOTE : 

# 1. start , stop , step are optional. 
# 2. Default start is index 0. 
# 3. Default step is 1. 
# 4. end = stop - 1. 
# 5. Character at stop index is not printed. 
# 6. Positive index : Go in forward direction. 
# 7. Negative index : Go in Negative direction.
# 8. If stop not found , nothing is returned. 



name = 'code yug' 

print(name[0:3:1]) #-->  cod 

print(name[2:4]) #--> de 

print(name[0:5:2]) #--> cd 

print(name[:4]) #--> code 

print(name[::]) #--> code yug 

print(name[0::3]) #--> ceu 



print(name[-1:-4:-1]) #--> guy 

print(name[-1:-5:-2]) #--> gy 

print(name[-2:-6:2]) #--> blanck space

print(name[-1::-1])  #--> guy edoc


print(name[-3:-11]) #--> " "

print(name[-1:-1:-1]) #--> " "


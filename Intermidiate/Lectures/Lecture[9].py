
# :: Youtube Playlist Content : 

# --> lecture-46 : Coding Question in Python.
# --> lecture-47 : Primitive Datatypes - integers. 
# --> lecture-48 : Integers Interconversions. 
# --> lecture-49 : Float datatype. 
# --> lecture-50 : NoneType & Boolean Types in Python.


# _________________________________________________________________________________________________________________________


# :: Python Program to find complement of given positive number : 

# --> Complement of a number is defined as reversing all binary 1's bit to binary 0 and all the binary 0's bit to binary 1's. 
# Ex: 
# input (given number) = 5
# Output (complement of given number) = 2


# :-> Steps to find complement :

# 1.  find the binary representation of given number.  

# 2.  Visit every bit and flip it. 

# 3.  Convert 'result of flipping' into decimal integer





# def FindComplement(num):
#     binary_num = bin(num)[2:]
#     complement_result = ''
#     for bit in binary_num:
#         if bit == '1':
#             complement_result += '0'
#         else:
#             complement_result += '1'
            
#     return int(complement_result , 2)
            


# num_input = int(input("Enter the num :"))
# print(f"The complement of {num_input} is : {FindComplement(num_input)}")








# __________________________________________________________________________________________________________________






# :: int datatype :

# -> int(integer) is a whole number , positive or negative , without decimal point. 
# Ex :  

# x =  1
# z = -2  

# -> It has unlimited length only limited by memory.
# Ex : 1234546657577577.... 


# -> Checking the type :

x = 5
# print(type(x)) # Output : <class 'int'>





# :--> Type of Integers :

# 1. Decimal int 
# 2. Binary int 
# 3. Hexadecimal int 
# 4. Octal int








# 1. Decimal int :

# --> Range :- 0 to 9 [0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]. 
# --> base is 10
# --> Ex :

# a = 20 
# print(a)  #--> 20
# print(type(a))  #--> <class 'int'>








# 2. Binary int :

# --> 0 and 1. 
# --> base is 2. 
# --> represented by prefix '0b' or '0B'. 
# --> Ex :

# print(0b1011)  #--> 11 


# num = 0b1011
# print(num)  #--> 11

# print(type(num))  #--> <class 'int'>












# 3. Octal int :

# --> Range :- 0 to 7 . (0 ,1 ,2 , 3 ,4 ,5 ,6 ,7). 
# --> base is 8. 
# --> reperesented by prefix '0o' or '0O'. 

# --> Ex :


# num = 0O15
# print(num) #--> 13
# print(type(num)) # --> <class 'int'>









# 4. Hexadecimal int :-

# --> Range :-
# 0 to 9 and a-f , A-F. [0, 1, 2, 3, 4, 5, 6, 7 ,8 , 9 , a , b , c ,d ,e ,f, A ,B, C ,D ,E ,F]. 
# --> base is 16. 
# --> represented by prefix '0x' or '0X'. 

# --> Ex :

# num = 0x124A
# print(num)  #--> 4682
# print(type(num))  # --> <class 'int'>





# __________________________________________________________________________________________________________________



# :: Inter-conversion among integers : 

# --> A number with prefix 0b/0B is considered as binary.  
# --> A number with prefix 0o/0O is considered as octal. 
# --> A number with prefix 0x/0X is considered as hexadecimal. 

# :-> Built-in function for inter-conversion :-

# 1. bin()
# 2. oct()
# 3. hex()
# 4. int()





# 1. Python bin() :

# -> Converts and returns binary string equivalent to passed integer. 
# -> Syntax : bin(num) 

# -> Ex :

# num = 5  # decimal int
# print("binary of 5 is :", bin(num))  #--> binary of 5 is : 0b101
# print(type(bin(num)))  #--> <class 'str'>


# num = 0o15  # octal int
# print("binary of 0o15 is :", bin(num))  #--> binary of 0o15 is : 0b1101
# print(type(bin(num)))  #--> <class 'str'>












# 2. Python oct() :

# -> Converts and returns string equivalent to passed integer. 
# -> Syntax : oct(num) 
# -> Ex :  
# num = 12
# print(oct(num))  # --> 0o14
# print(type(oct(num)))












# 3. Python hex() :

# -> Converts and returns hexadecimal string equivalent to passed integer. 
# -> Syntax : hex(num)
# -> Ex :
# num = 12
# print(hex(num))  # --> 0xc
# print(type(hex(num)))




# __________________________________________________________________________________________________________________




# :: Float data type in Python :

# -> The float type in Python represents the flaoting point number. 
# -> floating point number is also called as real numbers. 
# -> It has two parts :

# i) integer part
# ii) fractional part. 

# Ex:

# num = 97.88
# print(num)  #--> 97.88
# print(type(num)) #-->  <class 'float'>  









# :: Exponential representation :

# - Also called as scientific notation. 
# - It belongs to float datatype in Python. 
# - Scientific notation consists of two parts :
# i)  mantissa  
# ii) exponent

# - Syntax :   aeb    |    aEb  

# - Ex :

# num = 2e3 
# print(num)  #--> 2000.0 ( 2 x 10^3 )
# print(type(num))





# NOTE: 

# 1. Limit of float number in python is : 1.8 x 10^308. 
# 2. Any number greater than this will be indicated by the string inf in Python. 

# print(1.7e308)  #--> 1.7e+308

# print(1.8e308)  #--> inf













# :: float() constructor :

# - float() is a method that returns a floating-point number for a provided number or string. 
# - Ex :

# print(float())  #--> 0.0

# print(float(10)) #--> 10.0 

# print(float(10.2))  #--> 10.2 

# print(float("10.2")) #--> 10.2 

# print(float("9"))  #--> 9.0 

# print(float("abc")) # --> error 

# print(float("      9.2     "))   #--> 9.2

# print(float("      9.\n2     "))   #--> error

# print(float("      9.2 \n    "))   #--> 9.2 









# :--> Examples of Float() with Infinity and NaN :

# print(float(1.82e308))  #--> inf

# print(float("infinity"))  #--> inf

# print(float("inf"))  #--> inf 


# print(float("NaN"))  #--> nan

# print(float("nan"))  #--> nan











# :: float_number.as_integer_ratio() in Python :-  

# -> Syntax  : float_number.as_integer_ratio() . 
# -> It returns the two value (denomenator , numenator) inside the tuple.

# -> Ex :

# num = 7.5    #--> 15/2 
# a , b = num.as_integer_ratio()  #--> (15 ,2)
# print(a , "/" ,b, '=' , num)   # --> 15 / 2 = 7.5












# :: float.is_integer() in Python : 

# - Ex :

# num = -7.2 
# print(num.is_integer())  # --> False 



# num = -9.0
# print(num.is_integer())  # --> False 














# :: float to hex interconversion :

# num = 1.2345 
# print(num.hex())  #--> 0x1.3c083126e978dp+0
# print(type(num.hex()))





# _________________________________________________________________________________________________________________



# :: NoneType in Python :

# - In Python , None represents the absence of a value or a null value. 

# - Python uses the keyword None to define null objects and variables. 

# - Ex :

# name = None 
# print(name)  # --> None
# print(type(name)) # --> <class 'NoneType'>













# :: Boolean Type in Python :

# - In Python , boolean types are represented by the bool class. They have two possible values : True and False. 


# - Ex :

# is_married = False 
# print(is_married)  #--> False
# print(type(is_married))  #--> <class 'bool'>
       


# NOTE : 

# --> True :
        # -> non-zero ,
        # -> un-empty collections ,
        # -> True  ,
        # -> an expression returning no-zero value. 
        # -> an expression returning no-zero value. 
# --> False :
        # -> 0 ,
        # -> False , 
        # -> None ,
        # -> empty collections ,
     
        


# data = []
# data1 = {}
# data2 = ""
# data3 = ()
# print(bool(data))  #--> False
# print(bool(data1)) #--> False
# print(bool(data2)) #--> False
# print(bool(data3)) #--> False





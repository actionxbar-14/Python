
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








# ________________________________________________________________________________________________________________________




# :: int datatype :

# -> int(integer) is a whole number , positive or negative , without decimal point. 
# Ex :  

# x =  1
# z = -2  

# -> It has unlimited length only limited by memory.
# Ex : 1234546657577577.... 


# -> Checking the type :

x = 5
print(type(x)) # Output : <class 'int'>





# :--> Type of Integers :

# 1. Decimal int 
# 2. Binary int 
# 3. Hexadecimal int 
# 4. Octal int



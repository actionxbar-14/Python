
# :: Youtube Playlist Content : 

# --> lecture-121 : Dictionary Practice Questions.
# --> lecture-122 : bytes & bytearray. 
# --> lecture-123 : Operations on Bytes data. 
# --> lecture-124 : voting system using python. 
# --> lecture-125 : Enumerate() in Python. 


# _______________________________________________________________________________________________________________________ 


# :: Dictionary Practice question : 



# Question : 1) There is a dictionary containing students data :-
# How to fetch the last key-value pair from the student dictionary ?


# Answer : 1) 


# students = {'Ajay' : 89 , 'Jay' : 91 , 'Shantanu' : 99 , 'Vicky' : 91}

# # print(students)
# # print(len(students))

# students_list = list(students.items())

# # print(students_list) 

# last_keyValue = students_list.pop()
# print(last_keyValue)  # output : ('Vicky', 91)

# print(f"the key is  {last_keyValue[0]} and the value is :{last_keyValue[1]}")  # output : the key is  Vicky and the value is :91








# _______________________________________________________________________________________________________________________ 


# Question : 2) We have a dictionry :-


# Write a Python Program to count number of items having list as values. 
# data = {'Jay' : ['male , 23 , 2000'] , 'raj' : 25 , 'Vicky' : ['male , 22'] , 'ram' : ['male' , 23]} 



# Answer : 2) 



# :--> Approach  : 1 

# data = {'Jay' : ['male , 23 , 2000'] , 'raj' : 25 , 'Vicky' : ['male , 22'] , 'ram' : ['male' , 23]}   

# data_list = list(data.items())


# # print(data_list)
# count = 0
# for data in data_list:
#     print(data[1])
#     if type(data[1]) == type([]):
#         count+=1
        
# print(count)





# --> Approach : 2


# data = {'Jay' : ['male , 23 , 2000'] , 'raj' : 25 , 'Vicky' : ['male , 22'] , 'ram' : ['male' , 23]}   

# count = 0
# for key in data:
#     # print(data[key])
#     if type(data[key]) == type([]):
#         count += 1
        
        
# print(count)





# --> Approach : 3   By isinstance() method



# :--> isinstance() method : 
# - It gives true if the provided argument is equal to the given data type otherwise return false. 
# - Syntax : isinstance(value , data_type)

# - Ex : 

# value = [20, 30 ,50]

# print(isinstance(value , list))  # output : True
# print(isinstance(value , tuple)) # output : False







# data = {'Jay' : ['male , 23 , 2000'] , 'raj' : 25 , 'Vicky' : ['male , 22'] , 'ram' : ['male' , 23]} 

# count = 0

# for value in data.values():
#     if isinstance(value , list):
#         count += 1
        
# print(f"count is: {count}")   # output : count is: 3






# _______________________________________________________________________________________________________________________ 



# ::  bytes & bytearray :
# - There are two important datatype in Python :
# - bytes . 
# - bytearray. 

 
# 1.) Introduction to bytes and bytearray datatypes. 
# 2.) How to create these types data? 
# 3.) some important properties. 
# 4.) Advantages of bytes data. 
# 5.) Interview questions and often doubts. 






# :--> bytes datatype : 


# - bytes are immutable data types that represents group of bytes values. 
# - 1 byte = 8 bits. 
# - bytes must be in range of (0 , 256). 
# - Only integer values can be converted into bytes. (str , other are not allowed). 
# - Syntax : bytes(python_object)




# - Ex :  

# data = [10 , 20 , 30 , 40]

# b = bytes(data)
# print(b)
# print(type(b))

# del data 

# for element in b:
#     print(element)

# output : 
# 10
# 20
# 30
# 40



# - Ex :  for single integer it print the bytes value equal to that integer. 

# print(bytes(5))  # output : b'\x00\x00\x00\x00\x00'

# print(bytes(8))  # output : b'\x00\x00\x00\x00\x00\x00\x00\x00'

# print(bytes([5]))  # output : b'\x05'

# print(bytes([8]))  # output : b'\x08'




# NOTE : 

# --> The key takeaway is that when you pass a single integer to bytes() , Python interpretes it as the length of the bytes object , not the byte value. 





# - Ex :  use of indexin and slicing .


# data = [10 , 20 , 30 , 40]

# b = bytes(data)

# print(b[1])   # output : 20

# for element in b[0:2]:
    # print(element)
    
# output :  

# 10
# 20




# - Ex :  assignment and deletion to bytes data in not allowed , but we can delete the entire bytes.

# data = [10 ,20 , 30 , 40]

# b = bytes(data)

# # b[1]  = 50  # output :     b[1]  = 50
# #     ~^^^
# # TypeError: 'bytes' object does not support item assignment


# del b   #--> this is valid


# del b[1]   # output :     del b[1]
# #         ~^^^
# TypeError: 'bytes' object doesn't support item deletion


















#  :--> bytesarray datatype : 

# - It is a mutable type of datatype.
# - it supports the assinging or indexing method.

# - Ex: 

# data = [10 , 20 , 30 , 40]

# b = bytearray(data)

# print(type(b))
# print(b)

# for ele in b:
#     print(ele)
    
# output :
# 10
# 20
# 30
# 40





# - Ex : 


# data = [10 , 20 ,30, 40]
# b = bytearray(data)
# b[1] = 100

# for ele in b:
#     print(ele)

# output :

# 10
# 100
# 30
# 40






# NOTE:  bytes and  bytesarray are used for memory efficiency : 

# import sys  
# data1 = [10 , 20 , 30 , 40]
# data2 = bytes([10 , 20 , 30 , 40])

# print("memory consumed by data1 : " , sys.getsizeof(data1))  # output : memory consumed by data1 :  88
# print("memory consumed by data2 : " , sys.getsizeof(data2))  # output : memory consumed by data2 :  37





# NOTE : why list take more memory size :

# - Because list is a data structure and it has to store the refrences and list data structure metadeta. 








# NOTE :  When to use bytes and bytesarray and why there is limitation on bytes and bytearray : 

# - memory optimization. 
# - To work with binary files.

# - because :  1 byte = 8 bit ( 0 or  1)

# 00000000 :- minimun 0
# 11111111 :- maximun 256








# NOTE :  working with str in bytes and bytearray :


# import sys 
# str1 = "Shantanu @ codeyug"
# print("size of str1 :" , sys.getsizeof(str1)) # output : memory consumed by data1 :  88


# b = bytes(str1 , 'utf-8')
# print(b)
# print("size of b :" , sys.getsizeof(str1))  # output : memory consumed by data2 :  37



















# _____________________________________________________________________________________________________________________________________________




# ::  Operation on bytes and bytearray : 


# :--> Encoding :- 

# - Computer can only understand binary langauge. so assigning the value of each character uniqly then it is known as Encoding. 
# - Chr() and ord() function. 



# Ex : 

# print(ord('A'))  # output : 65
# print(chr(65))   # output : A




# - Ex : 

# data = [10 , 12 , 14 , 16]

# data_bytes = bytes(data)


# print(chr(10))  #--> '\n'
# print(chr(12))  #--> '\x0c'
# print(chr(14))  #--> '\x0e'
# print(chr(16))  #--> '\x10'

# print(data_bytes)  # output : b'\n\x0c\x0e\x10'
   
   
   
   


# - Ex :   with bytes

# data = [65 , 97 , 98]
# data_bytes = bytes(data)


# print(data_bytes)  # output : b'Aab'
   
   



# - Ex : with bytearray 

# data = [65 , 97 , 98]
# data_bytes = bytearray(data)


# print(data_bytes)  # output : bytearray(b'Aab')
   




















# :-->  Converting string values into bytes and bytearray : 



# - Ex :

# byte_string = bytes("shantanu" , encoding='utf-8')  

# print(byte_string)  # output : b'shantanu'




# - Ex : 


# bytearray_string = bytes("shantanu" , encoding='utf-8')  

# print(bytearray_string)  # output : b'shantanu'




# - Ex :  checking memory space taking by string with or withou bytes and bytearray. 

# import sys 

# str1 = "shantanu" 
# print(sys.getsizeof(str1))  # output : 57

# bytes_str1 = bytes("shantanu" , encoding='utf-8')
# print(sys.getsizeof(bytes_str1))  # output : 41
  



























# :--> Different Operations perform on bytes and bytearray : 






# - Ex :  using len() function

# byte_str  = bytes("shantanu" , encoding = 'utf-8')
# print(len(byte_str))  # output : 8











# - Ex : using index() method  


# byte_str  = bytes("shantanu" , encoding = 'utf-8')

# print(byte_str.index('t'))  # output :     print(byte_str.index('t'))  # output : 
#           ^^^^^^^^^^^^^^^^^^^
# TypeError: argument should be integer or bytes-like object, not 'str'


# NOTE : We must write b with the entered argument. 




# byte_str  = bytes("shantanu" , encoding = 'utf-8')

# print(byte_str.index(b't'))# output : 4  











# - Ex :  using find() method


# byte_str  = bytes("shantanu" , encoding = 'utf-8')

# print(byte_str.find(b't'))  # output :  4






# - Ex :   using upper() method


# byte_str  = bytes("shantanu" , encoding = 'utf-8')

# print(byte_str.upper())  # output :  b'SHANTANU'





# - Ex : using  split() method 

# byte_str  = bytes("shantanu Anubhav" , encoding = 'utf-8')

# print(byte_str.split())  # output : [b'shantanu', b'Anubhav']




# NOTE: bytes are immutable so we can't change or delete anything in the bytes , but we can delete entire bytes using del keyword  :


# - Ex :

# byte_str  = bytes("shantanu Anubhav" , encoding = 'utf-8')

# byte_str[2] = 'y'

# print(byte_str) # output :     byte_str[2] = 'y'
# #     ~~~~~~~~^^^
# TypeError: 'bytes' object does not support item assignment





# - Ex :

# byte_str  = bytes("shantanu Anubhav" , encoding = 'utf-8')

# del byte_str

# print(byte_str)  # output : int(byte_str)
# #           ^^^^^^^^
# NameError: name 'byte_str' is not defined




























# :--> using bytesarray for changing value in str : 

# - Ex : 

# bytearray_str = bytearray("shantanu kejkar" , encoding='utf-8')

# # bytearray_str[0] = 'a'  # NOTE :  we can't give 'a' here , we have to give ascii value of a 

# bytearray_str[0] = 97

# print(bytearray_str)  # output : bytearray(b'ahantanu kejkar')




























# :--> Encoding and Decoding :- 

## Encoding: Python object sai ----> bytes.
## Decoding: bytes sai ----> Python object.

# NOTE: For Encoding we can use bytes() / bytearray()  and encode() / decode() function.  [b"shantanu" ----> "shantanu"]



# - Ex : decode()

# str1 = "shantanu"
# str1_byte = bytes(str1 , 'utf-8')

# del str1 


# str2 = str1_byte.decode()
# print(str2)    # output : shantanu

# print(type(str2))  # output : <class 'str'>








# - Ex : encode()

# str1 = "shantanu"
# str1_byte = bytes(str1 , 'utf-8')

# del str1 


# str2 = str1_byte.decode()
# print(str2.encode())    # output : b'shantanu'

# print(type(str2))  # output : <class 'str'>









# _____________________________________________________________________________________________________________________________________________




# :: Voting System Using Python : 

# print("__________Voting System__________")



        
# candidate1 = input("Enter 1st candidate name :")
# candidate2 = input("Enter 2nt candidate name :")
# cand1_votes = 0
# cand2_votes = 0 

# voters_id = [101 , 102  , 103 , 104 , 105 , 106]
# no_of_voters = len(voters_id)
# print("number of voters :" , no_of_voters)

# voted = []

# while True:
#     if voters_id == []:
#         print("voting is over")
#         if cand1_votes > cand2_votes:
#             print(f"{candidate1} won the election with {cand1_votes}")
#         elif cand2_votes > cand1_votes:
#             print(f"{candidate2} won the election with {cand2_votes}")
#         elif cand1_votes == cand2_votes:
#             print("tied!!!")
#         break
    
#     else:
#         voter = int(input("Enter your id :"))
#         if voter in voted:
#             print("you already voted!")
#         else:
#             if  voter in voters_id:                     
#                 print(f"1.{candidate1} \n 2.{candidate2}")
#                 choice = int(input("Enter your choice :"))
#                 if choice == 1:
#                     cand1_votes += 1
#                     print(f"You Voted {candidate1}")
#                 elif choice == 2:
#                     cand2_votes += 1
#                     print(f"You voted {candidate2}")
                    
#                 voters_id.remove(voter)
#                 voted.append(voter)
#             else:
#                 print("you are not allowed to vote!")
                
            
        
        
        
        
            
        
    
    
    
    
# _____________________________________________________________________________________________________________________________________________
    
    
    
# :: Enumerate() function in Python : 

# - Keeps a counter to iterable and returns it. 
# - Syntax : enumerate(iterable , [start = 0])
# --> iterable :- any object that supports iteration. i.e list . 
# --> start :- starting point of counter.  , default is 0. 


# - Ex : 

# sports = ['cricket' , 'kabaddi' , 'tennis' , 'badminton']

# enum_object = enumerate(sports)

# print(enum_object) # output : <enumerate object at 0x0000015334F91A30>

# print(type(enum_object))  # output  : <class 'enumerate'>

# print(list(enum_object))  # output : [(0, 'cricket'), (1, 'kabaddi'), (2, 'tennis'), (3, 'badminton')]




# '''USECASE OF ENUMERATE IN PYTHON '''

# Ex :  use in loopings


# sports = ['cricket' , 'kabaddi' , 'tennis' , 'badminton']

# for position , element in enumerate(sports):
#     print(f"{position} : {element} ")
    
# output : 
# 0 : cricket 
# 1 : kabaddi 
# 2 : tennis 
# 3 : badminton  



# Ex :  Conversion of dictionary

# sports = ['cricket' , 'kabaddi' , 'tennis' , 'badminton']

# dict_enumerate = dict(list(enumerate(sports , 1)))

# print(dict_enumerate)  # output : {1: 'cricket', 2: 'kabaddi', 3: 'tennis', 4: 'badminton'}





# # - Ex :  use in json module 

# import json

# sports = ['cricket' , 'kabaddi' , 'tennis' , 'badminton']

# dict_enumerate = dict(list(enumerate(sports , 1)))

# f = open('dict_enumerate.json' , 'w')
# json.dump(dict_enumerate , f)

# f.close()
  
    
    
    




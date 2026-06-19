

# :: Youtube Playlist Content : 

# --> lecture-251 : Assert Statement in Python.
# --> lecture-252 : File Handelling ( FH-1 ). 
# --> lecture-253 : FH-2. 
# --> lecture-254 : FH-3. 
# --> lecture-255 : FH-4.


# ______________________________________________________________________________________________________________________________________ 








# :: assert statement  in Exception Handelling: 

# - An assert statement in Python is used to test an expression in the program code. 
# - Syntax : assert Expression[ , arguments]. 



# - Ex :  

# print("Use of assert statement :")

# def ValidAge(age):
#     assert(age >= 0) , "age can't be negative"
#     print("Your age is:" , age)

# ValidAge(20)  # output : Your age is: 20

# ValidAge(-20)  # output :   assert(age >= 0) , "age can't be negative"
# #            ^^^^^^^^
# # AssertionError: age can't be negative




# ______________________________________________________________________________________________________________________________________ 




# :: File_Handelling in Python : 


# :--> What is File? 
# - Files are named locations on disk to store information. 
# - They are used to store data permanently. 
# - Data is stored in non-volatile memory. 
# - We can retrieve data whenever required. 




# :--> Types of files :

# 1.) Text files :- 
# - Stores data in the form of characters. It is used to store data and strings. 
# - Ex :  .txt files 





# 2.) Binary files :- 
# - Stores data in the form of bytes. (group of 8 bits)
# - Ex: image , pdf, musix , video files. 







# :--> What is file handelling ?

# - File handeliig means :- 

# i) Opening a file. 
# ii) Performing some operations on it. 
# iii) Closing a file. 








# __________________________________________________________________________________________________________________________________________ 




# :: Need of file handelling :  

# -  File handelling ka use hota hai data ko permanently store krne ke liye in the files. 
# -  Ex :  

# age = input('Enter your age :')
# f = open(r"C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt", 'w')

# f.write(age)   #--> input age is stored in the given file location. 
# f.close()






# NOTE : 
# - Smaller application , json files ke liye ham file handelling ka use karenege . 
# - Larger application ke liye ham database ka use karenge. 






# __________________________________________________________________________________________________________________________________________ 


# :: Opening file  and mode attribute : 

# - Python provides an in-built function open() to open a file. 
# - Syntax :  

# f =  open(filename , mode = 'r' , buffering , encoding=None , errors = None , newline=None , closefd=True)

# f = open(filename , mode = 'r')


# :--> filename :-  file to be accessed. [string format]
# :--> mode     :-  access mode ( purpose of opening file ) , default mode is 'r' ( read ). [string format]
# :--> f        :-  file handler , file pointer. 



# - Ex :  



# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' )

# if f:
#     print("file succusfully open!")



# __________________________________________________________________________________________________________________________________________ 



# :: Buffering in Python : 

# - Buffering is s positive integer value used to set buffer size for file. 
# - In text mode , buffer size should be 1 or more than 1. 
# - In binary mode , buffer size can  be 0. 
# - Default size : 4096-8192 bytes. 









# NOTE :
# - Agar hame ak python program mai ko specific file[ 1 GB ] jo hard disk m stored hai , usse open krna chahte hai , toh uss pure file ko ak time prr fetch krna it is not possible , and very less efficient , 
# - iske liye ham main memory mai ak buffer create krte hai , or ye main memory ka hi part hota hai , ye 1GB data ko n no. of chunks mai divide krti hai , ak chunk ki size voh hogi jo ham decide karenge buffer ke liye  ,
# - So agar ham buffer size 1MB rakhte hai , toh 1MB ke n chunks create honge or ak time prr 1MB data fetch kiya jayega or process kiya jayega. 











# :--> Encoding : 
# - Encoding type used to decode and encode file. 
# - should be used in text mode only. 
# - Default value depends on OS. 
# - For windows :-  cp1252. 










# :--> errors : 
# - Represents how encoding and decoding errors are to be handled. 
# - Can't be used in binary mode. 
# - Some standard values are :- strict , ignore , replace etc. 






# :--> newline : 
# - it can be  \n , \r , \r\n . 










# - Ex :  

# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r' , buffering=10 ,encoding='utf-8')
# if f:
#     print("opened")
# print(f)






# __________________________________________________________________________________________________________________________________________ 


# :: Closing file : 
# - After performing operations , we have to close a file. 
# - close() :- function used to close a file . 

# - Syntax:   

# file_handler.close()




# :--> What happens when we close a file : 

# - File object is deleted from memory and file is no more accessible unless we open it again. 





# :--> What happens when we do not close a file : 

# - After program execution , python garbage collector will destroy file object and closes file automatically. 

# - NOTE : Don't rely on garbage collector. 





# - Ex : 

# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r')

# #operations 


# f.close()

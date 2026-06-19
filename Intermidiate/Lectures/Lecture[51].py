

# :: Youtube Playlist Content : 

# --> lecture-256 : FH-5.
# --> lecture-257 : FH-6. 
# --> lecture-258 : FH-7. 
# --> lecture-259 : FH-8. 
# --> lecture-260 : FH-9.


# ________________________________________________________________________________________________________________________________________ 


# :: Accessing the attributes of file handelling : 

# - Ex : 


# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r', encoding = 'utf-8')

# print("file name is :" , f.name)  # output : C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt

# print("encoding is :" , f.encoding)  # output : encoding is : utf-8

# print("mode is:" , f.mode)  # output :  mode is: r

# print("is file closed ?" , f.closed)  # output : False






# ________________________________________________________________________________________________________________________________________ 




# :: File object methods : 

# 1.) readable()
# 2.) writable()







# 1.) readable() : 
# - This method is used to check whether file is readable or not. 
# --> True :- if file is readable. 
# --> False :- if ifle is not readable.  





# 2.) writable() : 
# - This method is used to check whether file is writable or not. 
# --> True :- if file is writable. 
# --> False:- if file is not writable.  




# - Ex :  


# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r')


# print(f.readable())  # output : True
# print(f.writable())  # output : False



# - Ex:   W+ mode ( supporting both read and write method )





# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'w+')


# print(f.readable())  # output : True
# print(f.writable())  # output : True





# ________________________________________________________________________________________________________________________________________ 




# :: isfile() method : 
# - This method is used to check file exist or not. 
# - This method belongs to path module which is sub-module of os module. 

# :--> Syntax : 

# import os 

# os.path.isfile(filename)




# - Ex:  

# import os 

# print(os.path.isfile(r"C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt"))  # output : True



# - Ex : 


# import os 


# filename = input("Enter the file name :") 
# if os.path.isfile(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt'):
#     f = open("C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt")
#     #operations 
#     f.close()
# else:
    # print("file not exist")




# ________________________________________________________________________________________________________________________________________ 




# :: Ways of closing files : 

# - There are three ways of closing a file : 

# 1.) Normal way 
# 2.) Using exception handelling
# 3.) with statement. 





# 1.) Normal way : 

# - Syntax :  

# f = open('filename' , mode = 'r')
# #operations 
# f.close()





# 2.) Using exception handelling : 

# - Syntax : 

# try: 
#     f = open('filename' , mode = 'r')
#     #operations 
# finally:
#     f.close()






# 3.) with statement : 

# - Syntax :  

# with open('filename' , mode = 'r') as f:
    #operations 


# with open('filename' , mode = 'r') as f:
#     data = f.read()
#     print(data) 



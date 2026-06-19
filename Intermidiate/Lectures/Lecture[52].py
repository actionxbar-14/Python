

# :: Youtube Playlist Content : 

# --> lecture-261 : FH-10.
# --> lecture-262 : FH-11. 
# --> lecture-263 : FH-12. 
# --> lecture-264 : FH-13. 
# --> lecture-265 : FH-14.

# _______________________________________________________________________________________________________________________________________



# :: Mode of opening file : 

# - When you open a file for operations , you have to specify the mode . mode specifies the purpose of opening file. There are two types of modes : 

# 1.) Text modes. 
# 2.) Binary modes. 







# 1.)  Text mode : 

# - When you open a file in text modes , python treates it's content as "str" type. 
# - When you get data from a text mode file ,  python first decodes the raw bytes using either a platform dependent encoding or specified encoding. 




# :--> Types of Text modes : 



# :-> r : Open file for reading only. if the file doesn't exist , it will show 'FileNotFoundError' (default). 
# :-> w : Open file for writing only. If the file doesn't exist , it will create a file. 
# :-> a : Open for appending . It appends new data at the end of file. If file does not exist , it creates a new file. 
# :-> x : Open for exclusive creation for writing. The specified file must not be avialable. It creates a new file and then we write data into it. If file exists , it will give an error. 
# :-> r+ : Open for reading and then writing. 
# :-> w+ : Open for writing and then reading. 
# :-> a+ : Open for appending and then writing. 









# 2.) Binary mode : 

# - When you open a file for binary mode , python uses the data without any encoding. Binary mode file reflects the raw data directly in the file. 
# - Python treats file contents as "bytes" type.  These modes are used while dealing with non-text files like images , audios , videos etc. 




# :--> Types of binary modes : 

# :-> rb : Open for reading in binary mode. ( same as text 'b').  
# :-> wb : Open for writing in binary mode. (same as text 'w'). 
# :-> ab : Open for appending.  (same as text 'a') 
# :-> xb : Open for exclusive creation and writing. (same as 'x')
# :-> rb+ : Open for read and then write in binary. 
# :-> wb+ : Open for writing and then reading in binary. 
# :-> ab+ : Open for append and then read in binary. 




# _______________________________________________________________________________________________________________________________________



# :: Reading data from file: 

# - To read content of file , we have following three methods :-

# 1.) read()
# 2.) readline()
# 3.) readlines()










# 1.)  read() : 
# - This method is used to read data/content from a file and returns it as a string in text mode. It returns bytes in binary mode. 

# - Syntax :  file_object.read(size)

# :-> size :- It represents the number of characters to be read in text mode. 



# - Ex : 

# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r')

# data = f.read()
# print(data)
# f.close()



# - Ex :  (with size)

# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r')

# data = f.read(10)
# print(data)
# f.close()





# _______________________________________________________________________________________________________________________________________



# 2.) readline() : 
# - This function is used to read a single line from a file. 

# -  Syntax :  file_object.readline(size)

# :-> size :- number of characters to read from line. 


# - Ex: 

# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r')

# data = f.readline()
# print(data)  # output  : hello world
# f.close




# - Ex: 

# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r')

# data = f.readline(3)
# print(data)  # output  : hel
# f.close







# _______________________________________________________________________________________________________________________________________




# 3.) readlines() :
# - This method is used to read all lines from a file and returns a list of lines. 

# - syntax : file_object.readlines()




# - Ex : 

# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r')

# data = f.readlines()
# print(data)

# f.close() # output : ['hello world\n', 'welcome to the world of programming']





# - Ex :  


# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r')

# data = f.readlines()

# for line in data:
#     print(line , end = "")

# f.close()
# output : 
# hello world

# welcome to the world of programming


# _______________________________________________________________________________________________________________________________________





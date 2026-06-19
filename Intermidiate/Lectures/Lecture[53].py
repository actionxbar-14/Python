

# :: Youtube Playlist Content : 

# --> lecture-266 : FH-15.
# --> lecture-267 : FH-16. 
# --> lecture-268 : FH-17. 
# --> lecture-269 : FH-18. 
# --> lecture-270 : FH-19. 


# ______________________________________________________________________________________________________________________________________




# ::  tell() : 

# - This method is used to find the current position of a file pointer from the beginning of the file. 

# - Position starts from 0. It is just like indexing in string. 

# - Syntax: file_object.tell() 


# - Ex :  


# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r')

# print(f.tell())  # output : 0

# f.read(3)  
# print(f.tell())  # output : 3
# f.close() 













# :: seek() :- 
# - This method is used to change the position of file pointer. 
# - Remember , file pointer position is always counted from the beginning. 

# - Syntax :  file_object.seek(position) 


# - Ex : 


# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r')

# print(f.tell())  # output : 0

# f.read(3)  
# print(f.seek(0))  # output : 0
# f.close() 





# ______________________________________________________________________________________________________________________________________



# - Ex :   [ counting the number of words , number of chars , number of lines ]



# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r') 

# number_of_words = 0
# number_of_chars = 0
# number_of_lines = 0 

# for line in f:
#     number_of_lines += 1
#     line = line.strip("\n")
#     number_of_chars += len(line)
#     list1 = line.split()
#     number_of_words = len(list1)

# print("number of lines :" , number_of_lines)  # output : 2
# print("number of chars :" , number_of_chars)  # output : 46
# print("number of character :" ,number_of_words)  # output : 6
# f.close()



# ______________________________________________________________________________________________________________________________________



# :: Writing in a file : 

# - In order to write data in file  , we have to open in a mode which provides the facility of writing data.
# - Ex :  w , a , x etc. 






# 1.) 'W' mode : 

# - It opens the file to write only . 
# - It overwrites the data in a file. 
# - If a file doesn't exist , it creates a new file and write into it. 
# - The file pointer exists at the beginning of file. 


# :--> Mainly , two methods are used for writing data in file :

# i) write()
# ii) writelines()






# i) write() :
# - This method delete all the existing content / rewrite and then update the content given.

# -> Syntax :  file_object.write(data in string format)




# - Ex:  

# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'w') 

# f.write("this is the content of write method")

# f.close()





# - Ex:  

# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'w') 

#n = f.write("this is the content of write method")
# print(n)  # output : 8
# f.close()







# ii) writelines() : 
# - This method is used to write a group of lines of strings into the file represented by a file object. 
# - Group of strings are stored in list , tuple or set. 

# - Syntax :  file_object.writelines(list/set/tuple)



# - Ex : 

# f = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'w') 

# lines_list = ['yogesh' , 'ram' , 'raj' , 'shantanu']

# f.writelines(lines_list)
# f.close()
























# ______________________________________________________________________________________________________________________________________



# ::  Copying the content from one file to another : 


# - Ex : 



# f1 = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data.txt' , mode = 'r' , encoding='utf-8') 

# f2 = open(r'C:\Users\ANUBHAV\Program_Folders\Python\Data\data_one.txt' , mode = 'w' , encoding='utf-8') 

# data = f1.readlines()
# for line in f1:
#     f2.write(line)

# f1.close()
# f2.close()



# ______________________________________________________________________________________________________________________________________



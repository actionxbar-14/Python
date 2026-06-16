

# --> How to use Execption_Handelling in File_Handelling  :


# - Ex : 



# f =  open(r"C:\Users\ANUBHAV\Program_Folders\Python\Intermidiate\Lectures\Lecture_Practice\Module_Practice\Exception_Handelling\leetcode.txt" , mode = 'r')

# #--> operation : 

# f.close()
# print("rest of code")   # it runs succussfully











# # - Ex :



# f =  open(r"C:\Users\ANUBHAV\Program_Folders\Python\Intermidiate\Lectures\Lecture_Practice\Module_Practice\Exception_Handelling\leet-code.txt" , mode = 'r')

# #--> operation : 

# f.close()
# print("rest of code")   # output :     f =  open(r"C:\Users\ANUBHAV\Program_Folders\Python\Intermidiate\Lectures\Lecture_Practice\Module_Practice\Exception_Handelling\leet-code.txt" , mode = 'r')
# FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\ANUBHAV\\Program_Folders\\Python\\Intermidiate\\Lectures\\Lecture_Practice\\Module_Practice\\Exception_Handelling\\leet-code.txt'


# NOTE: by entering wrong file name error occurs and flow of execution is stopped. So we have to use Exception handelling. 





# - Ex : 



# try:       
#     f =  open(r"C:\Users\ANUBHAV\Program_Folders\Python\Intermidiate\Lectures\Lecture_Practice\Module_Practice\Exception_Handelling\leet-code.txt" , mode = 'r')
#     f.write("hello world")

# #--> operation : 

# except Exception as e:
#     print(e)

# else:
#     f.close()







# print("rest of code")



# __________________________________________________________________________________________________________________________________________



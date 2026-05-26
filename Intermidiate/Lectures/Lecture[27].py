
# :: Youtube Playlist Content : 

# --> lecture-136 : Python virtual Enviornment.
# --> lecture-137 : How to create Python Virtual Enviornment. 
# --> lecture-138 : 3 best Logical question for freshers. 
# --> lecture-139 : Python Interview Question. 
# --> lecture-140 : Python Programming Question. 


# _______________________________________________________________________________________________________________________ 


# :: Python Virtual Enviornment  ( Python venv ) : 

# - According to Python documentation   , "A virtual enviornment is a Python enviornment such that the Python interpreter , libraries & scripts installed into it are isolated from those which are installed in other virtual enviornments  , and ( by default ) any libraries installed in a "system" Python , i.e. one which is installed as part of your operating system". 

# - It is an isolated runtime environment that allows Python users & applications to install and upgrade packages without interfering with other python applications. 

# - A self-contained directory tree that contains a python installation for a particular version of python  , plus a number of additional package. 
 

# - Ex : Visualization  [ Base OS : Windows]

# :- Virutal Env ( Base ) :

# -> Package A (2.1)
# -> Package B (1.0)




# :- Virtual Env (1) :

# -> Package A (3.1)
# -> Package B (1.1)




# :- Virtual Env (2) :

# -> Package A (1.0)
# -> Package B (1.1)






# _______________________________________________________________________________________________________________________ 



# :: How to create Python Virtual Enviornment : 

# --> Genral Way : 

# 1.) Install Python on your machine. 
# 2.) Install all your required libraries using pip. 
# 3.) write all your code in a single .py file. 
# 4.) Run it through terminal or directly. 



# --> Your new virtual enviornment has :-

# 1.) pip to install libraries .
# 2.) its own libraries folder. 
# 3.) its own Python interpreter version.  







# NOTE : To create Python virtual Enviornment we have two ways : 


# 1.) Way - 1 : [ Using virtualenv ]

# :--> step 1 : Install virtualenv 
# - it is a tool to set up your Python enviornments. 
# - command : pip install virtualenv. 



# :--> step 2 : Create virtual Enviornment 
# - first make the folder and inside this folder location run the command. 
# - command : Python -m venv <virtual-enviornment-name> 





# :--> step 3 : Activate Virtual Enviornment 
# - Navigate to virutal env folder/Scripts.
# - Enter 'ACTIVATE' command.
# NOTE :  For deactivating the virtualenv and write the command : 'DEACTIVATE' 


















# 2.) Way - 2 : [ Using virtualenvwrapper extension ]


# :--> Step 1 : install virtualenvwrapper 
# - run the command inside the required folder where you want to create virtual enviornment. 
# - command : pip install virtualenvwrapper-win 




# --> Step 2 : Create a virtual env
# - Create a virtual env inside the folder where you installed the virtualenvwrapper. 
# - Command : mkvirtualenv <virtual_env_name>






# ________________________________________________________________________________________________________________________________________


# :: Python Interview Question :  


# Question : 1 .  Given : 

# my_str = "Sky is blue"

# we want that ;

# my_str = "blue is Sky"



# Answer : 

# my_str = "Sky is blue"
# my_list = my_str.split()
# print(my_list)   # output : ['Sky', 'is', 'blue']


# rev_list = my_list[::-1]
# print(rev_list)  # output : ['blue', 'is', 'Sky'] 


# result_str = " ".join(rev_list)
# print(result_str)  # output : blue is Sky


# NOTE : In one line 

# str1 = "Sky is blue" 
# print(" ".join(str1.split()[::-1]))  # output : "Sky is blue"












# Question : 2   Given :
# print the list of element having one occurrence .
# List = [1 , 2 , 2 , 3 , 3 , 4 , 5 , 5 , 5 , 6 , 6]  
# Output :  [1 , 4] 



# Answer :

# my_List = [1 , 2 , 2 , 3 , 3 , 4 , 5 , 5 , 5 , 6 , 6]   
# new_List = []
# for num in my_List:
#     if my_List.count(num) == 1:
#         new_List.append(num)
        
# print(new_List)   # output : [1, 4] 


# NOTE: In one line 

# my_List = [1 , 2 , 2 , 3 , 3 , 4 , 5 , 5 , 5 , 6 , 6]  
# new_List = [num for num in my_List if my_List.count(num) == 1]   

# print(new_List)    # output : [1, 4]














# Question : 3 

# Given :  my_str = "a ,a ,a ,b ,b ,c ,c ,c" 
# We want : 
# output :  a:3 , b: 2 , c : 3 ( char : count of char) 


# Answer : 

# my_str =  "a ,a ,a ,b ,b ,c ,c ,c"  

# my_list = my_str.split(',')

# visited = []
# final_list = []

# for ch in my_list:
#     if ch not in visited:
#         final_list.append(f"{ch} : {my_list.count(ch)}")
#         visited.append(ch)
        
# print(final_list)
# print(", ".join(final_list))
  




# ________________________________________________________________________________________________________________________________________




# ::  Python Interview Question : 

# Question 1 : Write Python Program for : 

# Given : my_str = 'my23name45is'
# we want Output :  'si23eman45ym' 




# Answer :  


# my_str = 'my23name45is'
# output = ''

# alphas = [char for char in reversed(my_str) if char.isalpha()]
# print(alphas)  # output : ['s', 'i', 'e', 'm', 'a', 'n', 'y', 'm'] 

# i = 0
# for char in my_str:
#     if char.isalpha():
#         output += alphas[i]
#         i += 1 
#     else:
#         output += char
        
# print(output)  # output : si23eman45ym








# ________________________________________________________________________________________________________________________________________



# :: Python Interview Question : 



# Question : 
# Given :- student_data = {
    # 'jay' : {'details' : {'roll' : 101 , 'marks' : [92 , 89 , 90 , 95 , 78]}},
    # 'viru' : {'details' : {'roll' : 102 , 'marks' : [61 , 81 , 91 , 98 , 79]}},
    # 'basanti' : {'details' : {'roll' : 103 , 'marks' : [83 , 89 , 80 , 95 , 78]}},
    # 'thakur' : {'details' : {'roll' : 104 , 'marks' : [52 , 69 , 90 , 95 , 78]}},
    
# }

# -> We have to find the percentage gain by the each student : 


# Answer : 


# student_data = {
#     'jay' : {'details' : {'roll' : 101 , 'marks' : [92 , 89 , 90 , 95 , 78]}},
#     'viru' : {'details' : {'roll' : 102 , 'marks' : [61 , 81 , 91 , 98 , 79]}},
#     'basanti' : {'details' : {'roll' : 103 , 'marks' : [83 , 89 , 80 , 95 , 78]}},
#     'thakur' : {'details' : {'roll' : 104 , 'marks' : [52 , 69 , 90 , 95 , 78]}}   
# }

# jay_percantage = student_data['jay']['details']['marks']
# viru_percantage = student_data['viru']['details']['marks']
# basanti_percantage = student_data['basanti']['details']['marks']
# thakur_percantage = student_data['thakur']['details']['marks']






# student_name = [key for key in student_data.keys()]

# # print(student_name)

# percentage_data = [sum(jay_percantage)  , sum(viru_percantage) , sum(basanti_percantage) , sum(thakur_percantage)]

# # print(percentage_data)

# result_student = {}

# result_student.update({student_name[0] : f'{percentage_data[0]*10/100}%' , student_name[1] : f'{percentage_data[1]*10/100}%' , student_name[2] : f'{percentage_data[2]*10/100}%' , student_name[3] : f'{percentage_data[3]*10/100}%'})

# print(result_student)



# print(f"{sum(jay_percantage) * 10/100} %")
# print(f"{sum(viru_percantage) * 10/100} %")
# print(f"{sum(basanti_percantage) * 10/100} %")
# print(f"{sum(thakur_percantage) * 10/100} %")





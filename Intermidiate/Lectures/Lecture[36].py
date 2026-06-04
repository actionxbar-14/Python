
# :: Youtube Playlist Content : 

# --> lecture-181 : Eval() function in Python - 1.
# --> lecture-182 : Eval() function in Python - 2. 
# --> lecture-183 : Command line Arguments - 1. 
# --> lecture-184 : Command line Arguments - 2. 
# --> lecture-185 : Switch case in Python / Match case in Python. 


# _________________________________________________________________________________________________________________________________



# :: Eval() function in Python - 1 : 

# - eval() is a built-in function used in Python. 
# - eval() function parses the string argument and evaluates it as a Python expression. 
# - String ---- Python Expression .


# - Syntax : eval(expression , globals = None , locals = None)
# --> expression :- A string to evaluate. 
# --> globals :- available global methods and variables. 
# --> locals :- available local methods and variables. 

# NOTE : 
# - globals , locals :- optional argument 
# - Expression :- mandatory  
# - we can use eval() to take the input from user and can convert it into list , set , tuple , dictionary.  



# :--> Return value of eval() :
# - result of expression present in string argument. 
# - Ex : 

# num = 3
# eval_num = eval('num * num')
# print(eval_num)  # output : 9




# - Ex : 

# add_list = eval('[1,2,3] + [4,5,6]')
# print(add_list)  # output : [1, 2, 3, 4, 5, 6]

# print(type(add_list))   # output : <class 'list'>





# - Ex : taking input of list by the eval() 

# data = list(eval(input("Enter the list :")))
# print(data)

# print(type(data)) # output : <class 'list'>



# - Ex : Solving the equation 

# x = int(input("Enter the value of x :"))
# eq = 'x * (x + 2)'

# ans = eval(eq)
# print(ans)







# NOTE : Where is eval() function mostly used.

# 1.) To solve mathmatical expresssion from string. 
# 2.) To take input from the user and convert it into list , set , tuple ,dictionary. 
# 3.) If the user wants to evaluate the string into code then can use eval function. 





# NOTE :  Warning when using eval()

# --> When We use Unix system ( macOS , Linux etc) , then if we imported the os module and run the command 'eval('rm -rf *)' then everything including each and every file of os gets deleted. 

# --> ex : 

##### import os 
##### eval('rm -rf*') 











# _________________________________________________________________________________________________________________________________





# :: Eval() function in Python - 2 : 
# - controling the power of eval() . 

# - Ex :  when we give password() as a input then eval() excutes and give the printed statement. 

# def password():
#     print("secret password is 1234")


# y = 10
# def solve_eq():
#     eq = input("Enter the equation in the form of x :")
#     x = int(input("Enter the value of x :"))
#     ans = eval(eq)
#     print("Solution :" , ans)
    
    
# solve_eq()






# - Ex :  ( Solution )
# -> We can use dictionary argument to allow only user to enter the specific input. 



# def password():
#     print("secret password is 1234")



# def solve_eq():
#     eq = input("Enter the equation in the form of x :")
#     x = int(input("Enter the value of x :"))
#     ans = eval(eq , {'x' : x})
#     print("Solution :" , ans)


# solve_eq()   # now when we enter password() as a input it gives nameError. , it only accept one x parameter.  
#    ans = eval(eq , {'x' : x})
#           ^^^^^^^^^^^^^^^^^^^^
#   File "<string>", line 1, in <module>
# NameError: name 'password' is not defined






# NOTE : sqrt() is not an built-in module/ function so it can only executes while we import the math module and does not give any globals() [ {} ] or give specification of allowing only sqrt to exectues. 


# - Ex : 

# from math  t(25)'))  # output : 5.0 


# - Ex :  

# from math import * 
# print(eval('sqrt(25)' , {'sqrt' : sqrt} ))  # outout : 5.0






# - Ex : 

# from math import * 
# print(eval('sqrt(25)' , {} ))  # outout :     print(eval('sqrt(25)' , {} ))  # outout : Error
#           ^^^^^^^^^^^^^^^^^^^^^^
#   File "<string>", line 1, in <module>
# NameError: name 'sqrt' is not defined


# :--> but other built-in module executes easily :

# from math import * 
# print(len('anubhav') , {})# outout :   7    {}



# NOTE : built-in function ka name in eval() argument and usko calling ke samay ka name exact same hona chaiye wrna error aa jayega. 


# - Ex :

# from math import * 
# print(pi)
# print(eval('sqrt(25)', {'square' : sqrt}))     # output :   print(eval('sqrt(25)', {'square' : sqrt}))   
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<string>", line 1, in <module>
# NameError: name 'sqrt' is not defined



# - Ex : 

# from math import * 
# print(pi)  # output : 3.141592653589793

# print(eval('square(25)' , {'square' : sqrt}))  # output : 5.0



# - Ex :  exectuing built-in and specific together


# from math import * 
# print(pi)

# print(eval('square(25) + len("hello")' , {'square' : sqrt}))


# - Ex : 

# from math import * 
# print(pi) 
# print(eval('square(25) + len("hello")' , {'square' : sqrt , '__builtins__' : None}))  # output :  iltins__' : None}))
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<string>", line 1, in <module>
# TypeError: 'NoneType' object is not subscriptable




# _________________________________________________________________________________________________________________________________


# :: Command line arguments : 

# - These are arguments passed when you run python program / script on command line. 
# - Syntax : python filename.py  arg1 arg2 arg3 

# --> These arguments are stored in a list named 'argv' inside sys module. 
# --> you can use these passed arguments using indexing like sys.argv[0] ( for first argument ). 


# - Ex : 

# import sys 

# print(sys.argv) 
# #--> we write in the command shell as argument : python Lecture[36].py 10 20.3 'hello' (10 , 20 , 30). 
# #--> and we get output as : ['Lecture[36].py', '10', '20.3', "'hello'", '(10', ',', '20', ',', '30)']


# - Ex :

# import sys 
# my_list = sys.argv 

# print('file name is :' , my_list[0])  # output : python Lecture[36].py 10 20.3 'hello' (10 , 20 , 30)







# - Ex :  write a Python script to check weather particular character present or not in string. 

# import sys 
# arg_list = sys.argv 

# if arg_list[1] in arg_list[2]:
#     print("found")
# else:
#     print("not found")


# print(arg_list)  
#output :['c:\\Users\\hp\\OneDrive\\Desktop\\Python\\Intermidiate\\Lectures\\Lecture[36].py']



# :: Usecase of Command line argument :  

# -> Passing file name as command line arguments instead of hardcoding in script. 
# -> Passing database name. 
# -> remote ip to which we want to connect. 





    
# _________________________________________________________________________________________________________________________________
    
    

# :: Command line Arguments - 2 : 
# - NOTE : Go to the module practice folder for this content and watch video.
# - Ex : [ copying data from one file to another file using command line argument. ]

#--> In example.py 

# f1 = open('one.txt' , mode = 'r')
# f2 = open('two.txt' , mode = 'a')

# data = f1.read()

# f2.write(data)
# f1.close()
# f2.close()





# _________________________________________________________________________________________________________________________________
    
    
# :: Switch case in Python / Match case in Python :

# - Since Python does not contain any switch case functionality , so we can only use alternatives of Switch case in Python . 

# - There are Three alternatives of Switch case in Python. 

# 1.) Switch Case implement in Python using Dictionary Mapping. 
# 2.) By using if-elif-else. 
# 3.) Match case.  [ after Python 3.9 version ]





# 1.) Switch Case implement in Python using Dictionary Mapping : 


# Ex :  getting the marks of the named person 

# def marks(name):
#     mapping = {
#     'shantanu' : 90 , 
#     'raj' : 91 , 
#     'jay' : 92 , 
#     'akshay' : 94 
#     }
    
#     return mapping.get(name, 'student does not exist')


# print(marks(input("Enter the name :")))






# 2.) By using if-elif-else : 

# - Ex : getting the grade of person belong to the marks entered. 

# marks = float(input("Enter marks :"))

# if marks >= 80 and marks <= 100:
#     print("You got grade A")

# elif marks >= 80 and marks <= 60:
#     print("You got grade B")

# elif marks >= 60 and marks <= 35:
#     print("You got grade C") 
# else:
#     print("You are failed/incorrect marks")







# 3.)  Match Case : 

# -> Default case is optional.
# - Ex : 

# choice = int(input("Enter the choice :"))

# match choice:
#     case 1:
#         print("redirect to login page")
#     case 2: 
#         print("redirect to info page")     
#     case 3:
#         print("redirect to info page")
#     case default:
#         print("redirect to Home")
   
 






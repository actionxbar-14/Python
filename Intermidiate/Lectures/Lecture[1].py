

# :: Youtube Playlist Content : 

# --> lecture-6 : How to Run Python Program on CMD. 
# --> lecture-7 : Python IDLE Tutorial / Continuation Character. 
# --> lecture-8 : Variables and KeyWord in Python. 
# --> lecture-9 : Python is Compiled or Interpreted. 
# --> lecture-10 : Single and Multiline Comments in Python. 





# :: IDE:- 

# - IDE stands for Integrated Development Environment. 
# - Provides tools and enviornments to create applications. 
# - IDE provides programming environment. 


# :Features:-

# - Syntax Highighlighting. 
# - Syntax Checking. 
# - Syntax Completion. 
# - Error Checking. 
# - Interactive Console. 
# - Integration with Tools and Frameworks.


# _______________________________________________________________________________________________________________


# :: IDLE :-

# - Provided by python. 
# - Only for learning purpose. 
# - CPython compiler is used. 


# :: Spyder :-

# - specifically designed for scientific and data-related programming. 
# - part of anaconda distribution. 
# - data analysis , visualization , and scientific computing. 


# :: Pycharm :-

# - specially designed for python community. 
# - provides all tools and frameworks of Python. 


# :: Vscode , Jupyter , atom ...... 


# ____________________________________________________________________________________________________________


# :: What is IDlE ?

# - Integrated Development Learning Environment. 
# - It is an IDE provided by Python. 
# - when you install Python , IDLE application gets installed. 
# - available from python 3.12 version. 


# --> Two ways to run programs using IDLE :

# 1. using interactive shell. 
# 2. using a script file. 



# ____________________________________________________________________________________________________________



# :: print function:

# def print(
#     *values: object,
#     sep: str | None = " ",
#     end: str | None = "\n",
#     file: SupportsWrite[str] | None = None,
#     flush: Literal[False] = False
# ) -> None: ...


#print("hello") #--> Output : hello

#print("hello" , "world" , sep='%')  #--> Output : hello%world


#print("hello" , "world" , sep='%' , end = ' $ ')  # Output : hello%world $




# continous character: \
    
# print("hello  \
#     world")  output : "hello      world"

# for i in \
#     range(5):
#         print("hello")
        
# output:
# hello
# hello
# hello
# hello
# hello



# ___________________________________________________________________________________



# :: Variables & Keywords :

# - what are variables and need of variables?
# - How to create variables & Working of variables?
# - Rules for creating variables ( Naming conventions )
# - do's & dont's 
# - Keywords in Python. 







# ----> Need of Variables / identifiers :

# - for data manipulation. 
# - for reusability of data. 
# - for storing results of expressions. 


# pi  = 3.14159
# radius = 3

# AOC = pi*radius*radius

# print(f"The area of Circle of radius {radius} is: {AOC}") # Output : The area of Circle of radius 3 is: 28.274309999999996








# ----> How to create variables in  python?

# In C :- 
# int age = 20;

# In Python :- 
# age = 20

#NOTE : No need to specify datatype while declaring. 







# ----> How to read variable assignemnt?

# In Python :-  salery = 60,000. 

# - salery is equal to 60,000  [wrong]
# - 60,000 is assigned to salary  [right]
# - salary has value 60,000 [right]
# - salary refers 60,000 [right]






# ----> How variable works in Python ?

# : how variable works in C?
# --> C mai memory allocation variables ke liye hota hai. 

#int a = 20;                int b = 20;               int c = a;           int d = 30;

#      a                       b                          c                     d
#      20                      20                         20                    30
#   address : 1244        address : 1248             address : 1252        address : 1256




# : How variables works in Python?
# --> Python mai memory allocation values ke liye hota hai. 

# (learn from lecture-8 playlist video)

# # Ex :

# a = 100
# print("a : " ,id(a))  # Output :-  a :  140715374669704

# b = 100 
# print("b :" , id(b))  # Output :-  b : 140715374669704

# c = 100
# print("c : ", id(c))  # Output :-  c :  140715374669704

# d = 200
# print("d :" , id(d)) # Output :-  d : 140715374672904

# d = 300
# print("d :" , id(d)) # Output :-  d :  d : 1606072974512




# ____________________________________________________________________________________________________________________


# :: Re-assigning variables: 

# age = 20

# age = "Two"

# print(age) # Output : Two 

# name = "shantanu"
# age = 23
# salary = 35505.4






# name , age , salary = "shantanu" ,22 ,  244349.9
# print(name) , print(age) , print(salary)

# Output : 
# shantanu
# 22
# 244349.9




# num = age = value = 22

# # print(num) , print(age) , print(value)

# output:
# 22
# 22
# 22



# __________________________________________________________________________________________  




# :: Rules for creating variables :

# 1. variable must start with alphabet or an underscore(_):

# -   balance  [right]
# -   _balance [right]
# -   1balance  [wrong]
# -   __balance  [right]


# 2. can't use special symbols except underscore(_):

# - my_balance [right]
# - my$balance [wrong]


# 3. Can't use Keywords as variable names. 

# - True
# - def 
# - import


# 4. variable name should not start with digit. 

# - 100_notes.


# 5. NO whitespaces allowed in variable names. 

# -  My balance [wrong]


# 6. variable in python are case-sensetive.

# - name = 'shantanu'
# print(Name)  --> error





# __________________________________________________________________________________________________________________


#NOTE:

# 1. Always create meaningful variables names. 
# 2. Recommended to use lowercase letters. 
# 3. Separate multiple words by underscore. 
# 4. Avoid funny and meaningless variable names. 
# 5. class name should start with uppercase letters. 



# __________________________________________________________________________________________________________________

# :: How to delete a variable : 

# a = 100
# print(a) output: 100

# del a  --> NameError


# __________________________________________________________________________________________________________________



# :: Variable annotations:

# name:str = "Anubhav"

# print(name)


# name = 23
# print(name)


# __________________________________________________________________________________________________________________


# :: keyword : keywords are the reserved words that cannot used as a variable. 
# -->> How to get list of keywords?

# import keyword

# print("keywords are :", keyword.kwlist)

# Output :

# keywords are : ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
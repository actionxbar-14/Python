
# :: Youtube Playlist Content : 

# --> lecture-126 : Python Scripts , Package , Module and library in Python.
# --> lecture-127 : PIP tool. 
# --> lecture-128 : How Python Search Modules & Packages. 
# --> lecture-129 : Python commands on CMD. 
# --> lecture-130 : List Comprehension in Python. 


# ______________________________________________________________________________________________________________________________________


# :: Python Scripts , Package , Module and library in Python :




# --> Python Scripts :- 
# - A Scripts is a Python file that is intended to run directly. If you run it , it should do something. This means that script contains code written outside the scope of classes and functions. 

# - Ex :   addition.py 

# def add(x , y):
#     return x+y 
# result = add(5 , 4)
# print(result)








# --> Python module :- 
# - A module is a Python file that is intended to be imported into other scripts. It consists of classes , functions and variables to be used in other files. 
# - Ex : 

# def add(x ,y):
#     return x+y 





# --> Python Package :- 
# - Collection of related modules that work together to provide certain functionality. 
# - Ex : FOLDER --> contains multiple .py files ( _init_.py files shows that particular folder is a package ).







# --> Python Library :- 
# - It is a collection of packages. It contains 100's of modules in it. These modules provide range of functionalities. 










# ______________________________________________________________________________________________________________________________





# :: Everything About pip : 

# --> Content :-

# 1.) What is PIP & why it is needed ?
# 2.) What is Pypi ?
# 3.) How to manage third party packages ?
# 4.) All PIP commands 
# 5.) How PIP works ?












# 1.)  What is PIP & How it is needed  :

# - PIP stands for ( Package Installer for Python ). 
# - PIP gives a tool called as 'pip' using which you can install , manage additional packages and libraries. 
# - PIP is a package manager in Python. 
# - While working on projects , you will need additional packages. Hence , it is essential tool for Python developer's. 





# :--> How it is needed :- 

# - Jab ham Python install krte hai tab hame python ka standard distribution milta hai and usme bahot sare modules , packages and built-in libraries milti hai. 
# - But , Python has huge community , it is impossible to give all packages with standard distribution , that's why it provide PIP tool for installing further modules , packgaes and libraries that are not inculded in the Python distributions. 



# :--> How to install PIP :-

# - PIP has been included with the python installer since version 3.4 . 
# - Now , PIP is distributed with Python unless you use older versions. 






# :--> Verify PIP is installed or not :-

# i)    pip --version 
# ii)   pip -V
# iii)  py -m pip --version




# :--> How to update pip :- 

# - pip install --upgrade pip
# - py -m pip install --upgrade pip






# :--> How to get help :-

# - pip help




# :--> How to installing Packages with PIP :-

# - There are two ways :
# 1.) pip install [ packagename/module ]. 
# 2.) py -m pip install [ packagename/module ]. 




# - There are two sources : 

# 1.) Online repo ( PyPI and Github ).  : [ PyPI Python ki ak online repository hai jisme modules and packages ko host kiya jata hai .]
# 2.) distribution file ( From the local storage/file ). 


# NOTE : Python programs do tarike se execute hote hai  , output dono ka same hota hai but execution alag alag hota hai :

# --> i.)   moduler approach ( modules ) :
# - Execution Syntax :- py modulename.py



# --> ii.)  scripts ( standalone programs ) :
# - Execution Syntax :- py -m modulename 





# NOTE : There are two main online repo. , we can check if the package is present in the system or not by using the command [ pip list ].

# 1.) Pypi ( Python Package index )
# 2.) Github



# NOTE: uninstalling the current packages and installing them with specific version. 

# - pip uninstall [packagename] 

# - pip install packagename == [versionname]



# NOTE : list the outdated packages. 

# - pip list --outdated --verbose



# NOTE : downloading the packages into the specific location :

# - pip install requests --target [path]





# NOTE: Installing packages from github :

# -> pip install Github_repository_URL
# - Ex: pip install git+https://github.com/examplesuser/example-package.git 




# NOTE : Installing multiple packages using a requirements file. 

# 1.)  create a requirement.txt file  , write all the packages with their latest version ( packages =  version). 
# 2.) run the command in the location where the requirements.txt file is created :  pip install -r requirement.txt 



# NOTE : For checking any breaking requirements :

# -> pip checkz


# :--> Benifits :

# 1. simplifies the process of managing dependencies. 
# 2. Helps maintain consistency in package versions. 





# _______________________________________________________________________________________________________________






# :: How Python search for imported module / Package :

# -> PythonPath :- ( it is an enviornment variables )
# - The "Python Path" refers to the list of directories that Python uses to search for modules , packages and other files when executing a script or importing modules.  

# -> How Python searches ? 
# - jab ham ak module ko import krte hai to Python sabse pahle usee :
# i.)   Current directory mai search krta hai , agar vaha nahi milta vo module toh , 
# ii.)  PythonPath Enviornment Variables mai search krta hai  , agar vaha bhi nahi mila toh , 
# iii.) Standard Library mai search krta hai , agar vaha bhi nahi mila toh , 
# iv.)  Site-packages mai search krta hai. 





# -> How to check Python search Path ?

# import sys


# print(sys.path)  # output : ['c:\\Users\\hp\\OneDrive\\Desktop\\Python\\Intermidiate\\Lectures', 'C:\\Program Files\\Python311\\python311.zip', 'C:\\Program Files\\Python311\\DLLs', 'C:\\Program Files\\Python311\\Lib', 'C:\\Program Files\\Python311', 'C:\\Users\\hp\\AppData\\Roaming\\Python\\Python311\\site-packages', 'C:\\Program Files\\Python311\\Lib\\site-packages']

# import demo_package as dp # output : -  demo run!

# print(dp.add(2,4))  # output : 6






# _______________________________________________________________________________________________________________



# :: 7 Windows Commands on CLI For Python :



# 1. Installation folder ka path janne ke liye :- 

# - command :  where Python 

# output :
# C:\Program Files\Python311\python.exe
# C:\Users\hp\AppData\Local\Microsoft\WindowsApps\python.exe





# 2. To run a Python script : 

# - command : python filename.py
# ( agar ye file current directory mai hi hogi tabhi run hogi otherwise filename.py ki jagah file ka pura path dena pdega.) 




# 3. Run Python statements :
# - Simple python statements containing one line.

# - command :   python -c "program_code_one_line"
# - Ex : python -c  "print('hello anubhav')" 




# 4.  check version of Python : 

# - command :  py --version 
# - command : python --version 



# 5. Install third party/External package : 

# - command : pip install package_name
# - Ex : pip install pandas 



# 6. Use python interpreter : 

# - command :  python
# NOTE : for exit this enviornment : exit()





# 7. To install python from cmd : 

# - command : choco install python --pre








# _______________________________________________________________________________________________________________



# :: Comprehension : 
# - It is a way of writing compact code in Python. 
# - Ex : (long code)
# lst = []
# for i in range(1,4):
#     for j in range(5,7):
#         lst.append(i*j)
#     print(lst)
    
    
# - Ex : (compact code)

# print([i*j for j in range(5,7) for i in range(1,4)])



# :--> Types of Comprehension : 

# 1.) List Comprehension . 
# 2.) Set Comprehension. 
# 3.) Dictionary Comprehension. 










# 1.) List Comprehension : 

# :--> Syntax - 01 : Normal
# [ expresion for variable in iterable ].

 
# - Ex : finding Sq of numbers ( without List Comprehension ).

# nums = [3 , 6 ,8 , 12 , 14 ,15]
# sq_num = []

# for num in nums:
#     sq_num.append(num*num)
    
# print(sq_num)  # output : [9, 36, 64, 144, 196, 225]




# - Ex : finding Sq of numbers ( with List Comprehension ).

# nums = [3 , 6 ,8 , 12 , 14 ,15]
# sq_num = [num*num for num in nums]

# print(sq_num)  # output : [9, 36, 64, 144, 196, 225]






















# -> Syntax - 02 : If condition.
#  [ expression for varible in iterable if condition ]

# - Ex : finding sq of Even numbers only ( without List Comprehension ). 

# nums = [3 , 6 ,8 , 12 , 14 ,15]
# sq_num = []

# for num in nums:
#     if num%2 == 0:
#         sq_num.append(num*num)

# print(sq_num)  # output : [36, 64, 144, 196]





# - Ex : finding sq of Even numbers only ( with List Comprehension ). 



# nums = [3 , 6 ,8 , 12 , 14 ,15]
# sq_num = [num*num for num in nums if num%2 == 0]

# print(sq_num) # output : [36, 64, 144, 196]





















# -> Syntax - 03 : Nested if's
# [ expression for variable in iterable if condition_1 if condition_2 ]


# - Ex : finding sq of Even num divisible by 3 also ( without List Comprehension ). 

# nums = [3 , 6 ,8 , 12 , 14 ,15]
# sq_num = []

# for num in nums:
#     if num%2 == 0:
#         if num%3 == 0:
#              sq_num.append(num*num)

# print(sq_num)  # output : [36, 144]





# - Ex : finding sq of Even num divisible by 3 also ( with List Comprehension ). 

# nums = [3 , 6 ,8 , 12 , 14 ,15]
# sq_num = [num*num for num in nums if num%2==0 if num%3==0]

# print(sq_num)  # output : [36, 144]













# -> Syntax - 04 : If - else 
# [ expression if condition else expression]

# NOTE :  with for loop : [ expression if condition else expression for variable in iteration]. 





# - Ex : Finding square of Even numbers and cubes of Odd numbers. (without using List Comprehension ). 


# nums = [3 , 6 ,8 , 12 , 14 ,15]
# sq_num = []
# cube_num = []

# for num in nums:
#     if num%2 == 0:
#         sq_num.append(num*num)
#     else:
#         cube_num.append(num*num*num)
        

# print(sq_num)  # output : [36, 64, 144, 196]
# print(cube_num) # output : [27, 3375]







# - Ex : Finding square of Even numbers and cubes of Odd numbers. (with using List Comprehension ). 



# nums = [3 , 6 ,8 , 12 , 14 ,15]
# sq_num = []
# cube_num = []
# result = [sq_num.append(num*num) if num%2==0 else cube_num.append(num*num*num) for num in nums]

# print(sq_num) # output : [36, 64, 144, 196]
# print(cube_num)  # output : [27, 3375]






# NOTE :   Nested loops

# lst = []

# for i in range(3,6):
#     for j in range(5,7):
#         lst.append(i*j)
# print(lst)  # output : [15, 18, 20, 24, 25, 30]







# nested_loop = [(i*j) for i in range(3,6) for j in range(5,7)]

# print(nested_loop)  # output : [15, 18, 20, 24, 25, 30]




# :-> Advantages : 

# 1.  Compact and elegant code 
# 2.  Less code 
# 3.  Faster execution 


# :-> Disadvantages : 

# 1. complex syntax  
# 2. Hard to understand










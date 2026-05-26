
# :: Youtube Playlist Content : 

# --> lecture-151 : Variable Length arguments[*args , **args].
# --> lecture-152 : Mixing different type of arguments. 
# --> lecture-153 : Lambda Function in Python. 
# --> lecture-154 : Use of Lambda Function. 
# --> lecture-155 : Nested Lambda Function in Python. 


# _______________________________________________________________________________________________________________________ 


# :: Variable Length Arguments : 
# - There are basically two types :-
# 1.) Variable Length Positional Arguments. 
# 2.) Variable Length Keyword Arguments. 








# 1.) Variable Length Positional Arguments : 

# - It provides the feature of assigning variable length of parameter. 
# - It assign all the parameter to one variable and enclosed into an tuple. 


# - Ex : nums ak tuple hai jisme saare parameter store hote hai

# def addition(*nums):  #--> nums = (10 , 20 ,30 ,40)
#     sum1 = 0
#     for n in nums:
#         sum1 += n 
#     return sum1
   

# answer_sum = addition(10 ,20 , 30 , 40)
# print(answer_sum)  # output : 100



# - Ex : 




# def addition(*nums):  #--> nums = (10 , 20 ,30 ,40)
#     return sum(nums)
    


# answer_sum = addition(10 , 20 ,30 , 40)
# print(answer_sum)  # output : 100

 
 
 
 
 
 
 
 
#  2.) Variable Length Keyword Arguments : 
# - it store all the assign keyword arguments inside an dictionary.

# - Ex : 



# def addition(**nums):  #--> {'n1': 10, 'n2': 20, 'n3': 30, 'n4': 40}
#     return sum(nums.values())


# answer_sum = addition(n1 = 10 , n2 = 20 ,n3 = 30 ,n4 = 40)
# print(answer_sum)  # output : 100









# :--> mixing variable length keyword arguments (VLKA) and variable length positional arguments (VLPA) :

# NOTE :  

# ->  (**VLKA , *VLPA) : this syntax gives error
# ->  (*VLPA , **VLKA) : this syntax is right. 




# Ex - 1 :   (wrong syntax)

# def addition(**nums , *num):
#     return sum(nums.values())


# print(addition(n1 = 10 , n2 = 20 , n3 = 30 , 100 , 200 , 300))

# output :   def addition(**nums , *num):
#                           ^
# SyntaxError: arguments cannot follow var-keyword argument




# Ex - 2 : ( Right syntax )



# def addition(*num , **nums):
#     print(num)  # output : (100, 200, 300)
#     print(nums) # output : {'n1': 10, 'n2': 20, 'n3': 30}
#     return sum(nums.values())

# print(addition(100 , 200 , 300 ,n1 = 10 , n2 = 20 , n3 = 30 ))  # output : 60










# _______________________________________________________________________________________________________________________ 


# :: Mixing Multiple types of arguments : 

# 1.) Positional arguments 
# 2.) Keyword arguments 
# 3.) default arguments 
# 4.) variable length Positional arguments (*nums)
# 5.) variable length keyword arguments (**nums)





# Follow this Order : 

# positional argument >> variable length Positional arguments (*nums) >> Keyword arguments >> variable length keyword arguments (**nums)  >>  default arguments 


# _______________________________________________________________________________________________________________________ 


# NOTE : In Python , there are two types of functions :- 

# 1.) Normal Functions :- Created Using def keyword. 
# 2.) Lambda Functions :- Created Using lambda keyword(Anonymous Function). 









# :: Lambda Function in Python :
 
# - Argument is optional.
# - All type of arguments are allowed. 
# - only one expression / Python statement is allowed. 
# - It have in-built return statement.
# - For calling the lambda function we can create alias for that function. 

# - Syntax :-  lambda arg_list :  expression / python statement


# - Ex :  ( without lambda function )


# def addition(x ,y):
#     return x + y

# print(addition(2,3))  # output : 5




# - Ex :  ( with Lambda Function )

# add = lambda x , y : x + y
# print(add(2,3))  # output : 5

# print(type(add))  # output : <class 'function'>




# - Ex : using default arguments


# add = lambda x , y = 5 : x + y
# print(add(5))  # output : 10




# - Ex : using simple statements 

# display = lambda x , y : print(f"x : {x} and y : {y}") 
# print(display(5,7))  
# output : 
# x : 5 and y : 7  
# None  [ because print function default mai None return krta hai ]



# - Ex : assigning multiple statements by giving inside tuple 

# add = lambda x , y : (x + y , x - y)

# addition , subtraction = add(30 ,-10)

# print(f"addition is : {addition} and subtraction is  : {subtraction}")
# output : addition is : 20 and subtraction is  : 40






# NOTE :  Usecase 


# 1.) Incrementing number :-   lambda n : n + 1

# 2.) finding power of number :- lambda n : n**2 

# 3.) convert string to uppercase :- lambda str1: str1.upper()

# 4.) celsius to Fahrenheit :- lambda c : c * 9/5 + 32





# :: Why Lambda Functions :- 

# 1.) The purpose of lambda functions is to be used as parameters for functions that accept functions as parameters. 
# 2.) Mostly used in higher order functions. 
# 3.) Very usefull for small expressions and Less code required. 
# 4.) Lambda functions are very useful when we use filter() , map() , reduce() and higher order functions.  we will learn in upcoming chapters. 






#_______________________________________________________________________________________________________________________ 





# :: Usecase of Lambda Function : 




# 1.) Using Lambda function with the sorted() Function :- 

# - Ex :  

# data = ['Sharma Rohit' , 'Kohli Virat' , 'Tendulkar Sachin' , 'Raina Suresh' , 'Gill Shubhman', 'Kishan Ishan']

# print(sorted(data , key = len))  # output : ['Kohli Virat', 'Sharma Rohit', 'Raina Suresh', 'Kishan Ishan', 'Gill Shubhman', 'Tendulkar Sachin']




# - Ex :  ( without Lambda function )


# def func(nm):
#     names = nm.split()[1]  #--> ('Sharma Rohit' --> 'Rohit')
#     return names 
     
     
# data = ['Sharma Rohit' , 'Kohli Virat' , 'Tendulkar Sachin' , 'Raina Suresh' , 'Gill Shubhman', 'Kishan Ishan']

# print(sorted(data , key=func))  # output : ['Kishan Ishan', 'Sharma Rohit', 'Tendulkar Sachin', 'Gill Shubhman', 'Raina Suresh', 'Kohli Virat']








# - Ex : ( with Lambda function )

     
# data = ['Sharma Rohit' , 'Kohli Virat' , 'Tendulkar Sachin' , 'Raina Suresh' , 'Gill Shubhman', 'Kishan Ishan']

# print(sorted(data , key = lambda nm:nm.split()[1]))  # output : ['Kishan Ishan', 'Sharma Rohit', 'Tendulkar Sachin', 'Gill Shubhman', 'Raina Suresh', 'Kohli Virat']








#_______________________________________________________________________________________________________________________ 




# :: Nested Lambda Function :-  



# - Ex :  ( Without using Lambda Function)

# def outer():
#     def add(num1 , num2):
#         return num1 + num2 
#     return add(2, 5)

# result = outer()

# print(result)  # output : 7



# - Ex : ( Using Lambda Function )


# outer = lambda : lambda num1 , num2: num1 + num2 

# add = outer()  # add function definition 

# print(add(2,4))  # output : 6

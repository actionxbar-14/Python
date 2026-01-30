
                   # TOPIC : Function Arguments







# FUNCTION ARGUMENT :

# - Argument are the values that are passed into a function when it's called.
# - A function must be called with  the right number of arguments. If a function has 2 parameter , you must provide 2 arguments when calling it.

# Example : function defined using one parameter(variable)

# def greeting(name):  # name as a parameter.
#     print(f"hello, {name}")

# greeting("Anubhav") #output : hello , Anubhav  # Anubhav as argument.


# Types of Function Arguments:

# - Required arguments (Single/Multiple arguments).
# - Defalut argument.
# - Keyword arguments.
# - Arbitary arguments( variable - length arguments *args and **kwargs)



# 1. Required arguments (Single / Multiple arguments):


# ex:  name is defined as parameter and 'Anubhav' as Argument at the time of function calling is a Required argument.

# def greeting(name):  # name as a parameter.
#     print(f"hello, {name}")

# greeting("Anubhav") #output : hello , Anubhav  # Anubhav as an argument.


# ex:  course_name and instructor_name as an parameter. and 'Python' and "Rishabh" as an argument at the time of function calling.

# def Course_intro(course_name , instructor_name):
#     print(f"This is a {course_name} Tutorail and my instructor for this course is {instructor_name}")

# Course_intro('Python',"Rishabh") 
#output: This is a Python Tutorail and my instructor for this course is Rishabh.







# 2. Defalut Argument : 

# - You can assign default values to arguments in a function definition. if a value isn't provide when the function is called ,the default value is used.

# Ex: function defined using parameter & default value.

# def greeting(name = "World"):
#     print(f"hello, {name}!")


# greeting() # output : hello , world. [Printing default argument.]
# greeting("Anubhav") # output : hello , Anubhav.




# 3. Keyword Argument :

# - When calling a function , you can specify arguments by the parameter name. These are called keyword arguments and can be given in any order.

# Example : function defined using two parameters.

# def divide(a,b):
#     return a/b

# result1 = divide( b = 10 , a = 20)  # with keyword arguments
# print(f" The division of {a}/{b} is = {result1}") #output : 2

# result2 = divide( 10 , 20 )  # with positional arguments[takes a = 10 , b = 20 as position.]
# print(f" The division of {a}/{b} is = {result2}") #output : 0.5




# 4. Keyword Argument :
# 
# - If You're unsure how many arguments will be passed , use [ *args ] to accept any number of positional arguments.
# PURPOSE : Allows you to pass a variable number of positional arguments.
# TYPE: The arguments are stored as a [ tuple ].
# USAGE : Use when you want to pass multiple values that are accessed by position.

# ex: program to add n numbers.

# def add_numbers(*args):
#     print(type(args)) # OUTPUT : <class 'tuple'>
#     return sum(args)

# #Any number of arguments
# result1 = add_numbers(1,2,3,4)
# print(result1)  # output : 10

# result2= add_numbers(1,2,3,4,5,6)
# print(result2)  # output : 21


# ex: greeting of n person.

# def greeting(*names):
#     for name in names:
#         print(f"hello , {name}!")

# greeting("Anubhav" , "Divyanshu", "Neha" ,"Mannu")







# 5. Arbitary Keyword Arguments(**kwargs):

# -If you want to pass a variable number of keyword arguments , use **kwargs.
# PURPOSE : Allows you to pass a variable number of keyword arguments.(argument with names)
# TYPE : The arguments are stored as a dictionary.
# USAGE : Use when you want to pass multiple values that are accessed by name.

# ex:

# def print_details(**kwargs):
#     print(type(kwargs)) #output : <class 'dict'>
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# print_details(name = "Anubhav" , age = 20 , city = 'Rajpura') 
# # output: 
# name : Anubhav
# age : 20
# city : Rajpura


# print_details(name = "Anubhav" , age = 20 , city = 'Rajpura' , status = 'Active') 
# output:
# name : Anubhav
# age : 20
# city : Rajpura
# status : Active
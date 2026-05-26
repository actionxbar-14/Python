
# :: Youtube Playlist Content : 

# --> lecture-146 : Function is an Object.
# --> lecture-147 : Nested function in Python. 
# --> lecture-148 : Positional and keyword Arguments. 
# --> lecture-149 : Default arguments in Python. 
# --> lecture-150 : Mutable default Arguments.


# _______________________________________________________________________________________________________________________ 



# :: NOTE : 

# 1.) Function is an object :

# - Ex : 

# def display():
#     print('Hello world')
    
# print(type(display))  # output : <class 'function'>


# 2.) We can create aliases for Function : 

# - Ex : 

# -> var is an alias for the display function

# def display():
#     print('Hello world')
    

# var = display

# var()  # output : Hello world
# display()  # output : Hello world




# _______________________________________________________________________________________________________________________ 



# :: Nested Function : 

# - A nested function is simply a function defined inside another function. 
# - nested function ka scope sirf ussi function tk hota hai jiske ander use define kia gaya hai. 


# - Syntax : 

# def outer():
#     def inner():
#         pass

# - Ex : 

# def outer():
#     print("Hello world!")
#     def inner():
#         print("welcome!!")
#     inner()
    
# outer()






# _______________________________________________________________________________________________________________________ 





# --> Parameters :-
# - Variables for holding actual values. 
# - Present in function definition.
# - Ex def function_name(a, b) 


# --> Arguments :-
# - Values provided at function call.  
# - Ex :  function_name(5,2)




# ::  Types of Arguments :- 


# 1.) Positional arguments 
# 2.) Keyword arguments 
# 3.) Default arguments 
# 4.) Variable length arguments. 






# 1.) Positional arguments :
# - paramter and arguemnts ka order/Position values ke according hona chaiye agar order change kiya toh error ya galat variable mai value store ho jayegi.
# - no. of parameters ke equal no. of arguments bhi dene pdenge vrna TypeError aa jayega. 

# - Ex : 

# def display(name , age):
#     print(f"name is {name} and age is {age}")
    
    
# display('jay' , 23)  # output : name is jay and age is 23
# display(22 , 'jay')  # output : name is 22 and age is jay

  





# 2.) Keyword arguments : 
# - Isme order/Position matter nahi krti . 
# - no. of parameters ke equal no. of arguments bhi dene pdenge vrna TypeError aa jayega. 


# - Ex : 



# def display(name , age):
#     print(f"name is {name} and age is {age}")
    
# display(name = 'jay' , age = 23)  # output : name is jay and age is 23
# display(age = 23 , name = 'jay')  # output : name is jay and age is 23



# NOTE : Mixing of positional & keyword arguments :

# (keyword argument , positonal argument)  #--> wrong
# (positonal argument , keyword argument)  #--> right

# - Ex : 


# def display(name , age):
#     print(f"name is {name} and age is {age}")



# display(age=23 , 'jay')  #--> wrong
# diplay('jay' , age = 23) #--> right






# _______________________________________________________________________________________________________________________ 



# 3.) default arugments : 
# 
# - Ex : 

# def total_cost(items = {} , currency = 'Rupees'):  #--> default currency is Rupees , and default dictionary is empty dictionary
#     total = sum(items.values())  #--> [1.00 , 0.75 , 1.25]
#     print("Total cost is :", total , currency)



# cart = {"apple" : 1.00 , "banana" : 0.75 , "orange" : 1.25}
# total_cost(cart)  # output : Total cost is : 3.0 Rupees


# cart = {"apple" : 1.00 , "banana" : 0.75 , "orange" : 1.25}
# total_cost(cart , currency = 'USD')  # output : Total cost is : 3.0 USD



# NOTE :  

# -> phle default argument likhne ke baad dusrna non-default argument nhi de skte vrna error aa jayega.

# - Ex :


# def total_cost(items = {} , currency):    #--> SyntaxError
#     total = sum(items.values())  #--> [1.00 , 0.75 , 1.25]
#     print("Total cost is :", total , currency)


# cart = {"apple" : 1.00 , "banana" : 0.75 , "orange" : 1.25}
# total_cost(cart , currency = 'USD')  # output : SyntaxError: non-default argument follows default argument



# - Ex : Right way


# def total_cost(items , currency = 'Rs' ):    #--> SyntaxError
#     total = sum(items.values())  #--> [1.00 , 0.75 , 1.25]
#     print("Total cost is :", total , currency)


# cart = {"apple" : 1.00 , "banana" : 0.75 , "orange" : 1.25}
# total_cost(cart , currency = 'USD')  # output :Total cost is : 3.0 USD









# _______________________________________________________________________________________________________________________ 




# :: Default arguments on mutable datatypes : 
# --> Watch video for better understanding. 

# - Ex : 

# def add_item(name , employee_data = []):
#     employee_data.append(name)
#     print("Update data is : " , employee_data)
    
    
# add_item("jay")  # output : Update data is :  ['jay']
# print(add_item.__defaults__)  # output :  (['jay'],)


# add_item("viru") # output : Update data is :  ['jay', 'viru']
# print(add_item.__defaults__)  # output : (['jay', 'viru'],)


# add_item("basanti")  # output : Update data is :  ['jay', 'viru', 'basanti']
# print(add_item.__defaults__)  # output : (['jay', 'viru', 'basanti'],)
  

# add_item("thakur")  # output :   Update data is :  ['jay', 'viru', 'basanti', 'thakur']
# print(add_item.__defaults__)  # output : (['jay', 'viru', 'basanti', 'thakur'],)



# - Ex :  solution to this problem = assign None 


# def add_item(name , employee_data = None):
#     if employee_data is None:
#         employee_data = []
#     employee_data.append(name)
#     print("Update data is : " , employee_data)
    
    
    
    
# add_item("jay")  # output : Update data is :  ['jay']
# print(add_item.__defaults__)  # output : (None,)


# add_item("viru") # output : Update data is :  ['viru']
# print(add_item.__defaults__)  # output : (None,)


# add_item("basanti")  # output : Update data is :  ['basanti']
# print(add_item.__defaults__)  # output : (None,)
  

# add_item("thakur")  # output :   Update data is :   ['thakur']
# print(add_item.__defaults__)  # output : (None,)


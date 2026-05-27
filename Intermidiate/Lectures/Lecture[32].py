
# :: Youtube Playlist Content : 

# --> lecture-161 : Higher Order function.
# --> lecture-162 : filter() Function in Python. 
# --> lecture-163 : filter() function Examples. 
# --> lecture-164 : map() function in Python. 
# --> lecture-165 : filter() & map() Examples. 


# _______________________________________________________________________________________________________________________ 


# :: Higher Order function : 

# - A Function is called as higher order functions if :- 

# 1.) It contains other functions as parameters. 
# 2.) Returns a function as an output for further processing. 

# - Simply , A function which operates on other functions is called a higher order function. 


# - Ex :  

# def add(n1 , n2):
#     return n1 + n2


# def display(func):
#    print(func(10 , 20))

# display(add)  #--> display() function takes add() function as an argument so it is a higher order function. 



# - Ex :

# def display():
#     print("hello")
#     def printer():
#         print("Welcome!")
#     return printer  #--> display() function inner function printer() ke output ko return krega. 

# display()  # output : hello  




# _______________________________________________________________________________________________________________________ 



# NOTE : There are some important built-in functions :-

# 1.) filter()
# 2.) map()
# 3.) reduce()

# - There is a built-in module called as 'functools' which contains lots of built-in higher order functions. 













# 1.) filter() Function in Python : 

# -  Ye do parameter leta hai , function_name and iterable . 
# - function_name mai logic likha hota hai jo iterable prr perform krna hota hai ,
# - if logic is true then the items are considered or added to the result , otherwise items are removed.
# - We can only take the output of filter function and use the output only once. 


# - Syntax : filtered_object = filter(function_name , iterable). 

# :-> function_name : Function that test's if each element of a sequence is True or not. It consists of a logic of filtering elements from a given sequence. 
# :-> Iterable : Sequence like string , tuple , set , list from which we have to filter elements. 






# - Ex: ( filter even numbers from the data ).



# data = [23 , 22 , 36 , 54 , 59 , 90]

# def even(num):
#     if num %2 == 0:
#         return True
#     else:
#         return False



# :--> we can shorten the function : 

# def even(num):
#     return num%2 == 0



# filtered_obj = filter(even , data)
# # print(filtered_obj)  #output : <filter object at 0x000001F48281B9D0>

# print(type(filtered_obj))  # output :   <class 'filter'>



# :-> Printing data items in a list :-
# print(list(filtered_obj))  # output : [22, 36, 54, 90]



#:-> Printing data items using for loop : -
# for element in filtered_obj:
#     print(element)

# output : 
# 22
# 36
# 54
# 90





# - Ex : ( filter even numbers from the data using lambda Function )



# data = [23 , 22 , 36 , 54 , 59 , 90]

# filtered_obj = filter(lambda num:num%2==0 , data)
# print(list(filtered_obj))  # output : [22, 36, 54, 90]




# - Ex : Extreme shorten syntax 

# print(list(filter(lambda num : num%2==0 ,[23 , 22 , 36 , 54 , 59 , 90]))) # output : [22, 36, 54, 90]






# _______________________________________________________________________________________________________________________ 



# :: filter() functions Examples : 

# - Ex : filter vowels from given string 



# str1 = 'shantanu'
# vowels_list = ['a' , 'e' , 'i' , 'o' , 'u']

# def vowels(char):
#     if char in vowels_list:
#         return True
#     else:
#         return False 
    

# filtered_obj = filter(vowels , str1)

# print(list(filtered_obj))  # output : ['a', 'a', 'u']



# - Ex:  filter vowels from given string using Lambda Function 



# str1 = 'shantanu'
# vowels_list = ['a' , 'e' , 'i' , 'o' , 'u']

# filtered_obj = filter(lambda char: char in vowels_list , str1)
# print(list(filtered_obj))  # output : ['a', 'a', 'u']
    
    
    
    
    




# - Ex : filter students having marks greater than or equal to 90. 

# data = {'Nitesh' : 78 , 'Rahul' : 98 , 'Raj' : 91 , 'Amar' : 90 , 'Abhi' : 81} 


# def toppers(student):
#     if data[student] >= 90:
#         return True 
#     else:
#         return False

# toppers_student = list(filter( toppers, data))

# print(toppers_student)








# _______________________________________________________________________________________________________________________ 






# :: map() function in Python : 
# -  Ye do parameter leta hai , function_name and iterable . 
# - function_name mai logic likha hota hai jo iterable prr perform krna hota hai ,
# - We can only take the output of filter function and use the output only once. 




# - Syntax : mapped_object = map(function_name , iterable)

# :-> function_name : Function that process every element and returns result. 
# :-> Iterable : Sequence like string , tuple , set , list from which we have to filter elements. 



# - Ex : 

# names = ['raj' , 'yash' , 'yashraj']

# def find_length(name):
#     return len(name)


# mapped_obj = map(find_length , names)

# print(type(mapped_obj))  # output : <class 'map'>

# print(list(mapped_obj))  # output : [3, 4, 7]

# print(list(mapped_obj))  # output : []



# - Ex : Using tuple 



# names = ['raj' , 'yash' , 'yashraj']

# def find_length(name):
#     return name , len(name)

# mapped_obj = map(find_length , names)

# for element in mapped_obj:
#     print(element[0]  , element[1] , sep = "---->")


# output : 
# raj---->3
# yash---->4
# yashraj---->7







# - Ex :  

# nums = [5 ,3 , 8 , 11 ,6]

# def square(n):
#     return n**2 

# mapped_obj = map(square , nums)
# print(list(mapped_obj))  # output : [25, 9, 64, 121, 36]




# - Ex : Using lambda function 


# nums = [5 ,3 , 8 , 11 ,6]

# mapped_obj = map(lambda n:n**2, nums)
# print(list(mapped_obj))  # output : [25, 9, 64, 121, 36]









# _______________________________________________________________________________________________________________________ 



# :: filter() & map() Function Examples : 



# - Ex : passing two iterables into map() function

# marks = [60 , 70  , 80 , 90  , 100]
# bonus = [1 , 2 ,3 , 4]

# def logic(arg1 , arg2):
#     return arg1 + arg2 

# mapped_obj = map(logic , marks , bonus)

# for element in mapped_obj:
#     print(element)


# output : 
    
# 61
# 72
# 83
# 94








# - Ex : 

# laptops = { 'hp' : 50000 , 'lenovo' : 60000 , 'Asus' : 45000 , 'macbook' : 120000}

# budget = float(input("Enter your budget : "))

# def filter_items(element):
#     if laptops[element] <= budget:
#         return True 
#     else:
#         return False 
    

# filtered_obj = filter(filter_items , laptops)

# print(list(filtered_obj))
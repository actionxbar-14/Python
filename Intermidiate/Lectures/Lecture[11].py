
# :: Youtube Playlist Content : 

# --> lecture-56 : Slicing in Python Example.
# --> lecture-57 : String Operations in Python. 
# --> lecture-58 : Length of String in Python. 
# --> lecture-59 : Python Count() string method. 
# --> lecture-60 : startswith() and endswith() method. 


# _______________________________________________________________________________________________________________________ 


# ::  Python tricky Slicing Example :

# l = [1,2,3,4,5,6,7,8,9]
# print(l[:-4:-1])   #--> Here start value is not given , so default start is taken which is : 1.  [-1:-4:-1]

# Output: [9,8,7]




# _______________________________________________________________________________________________________________________ 



# :: Context : 

# - Concatenation of strings. 
# - Multiplication of string. 
# - Deletion of string. 
# - Iteration through string. 
# - Checking character / substring present in string. 









# :: Concatenation :

# - Joining two or more strings into a single one. 
# - It adds strings together. 
# - The '+' operator does this. 
# - Ex :

# str1 = 'Python is'
# str2 = 'awesome' 
# str3 = str1 + str2 

# print(str3)  #--> Python isawesome


# - Ex :

# name = "Anubhav"
# surname = "Pathak"
# Full_name = name + " " +surname 
# print("Full name is  :" , Full_name)  #--> Full name is  : Anubhav Pathak   

# # - Ex :

# num1 = '2'
# num2 = '3'

# print(num1 + num2)  #--> 23


# - Ex : we have to give both as a string , one str and one int object is not valid.

# num1 = 2
# num2 = '3'
# print(num1 + num2)

# Output  :   print(num1 + num2)
#           ~~~~~^~~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'




# # NOTE :  Typecasting for concatenate string and int. 

# num1 = 2
# num2 = '3'

# print(f"after concatenation of  is {num1} and {num2}: " + str(num1) + num2)
# #  output : after concatenation of  is 2 and 3: 23





















# ::  Multiplication : 

# - Repeat same string for multiple times. 
# - Using '*'  operator. 
# - Ex :


# str1 = 'codeyug'
# str2 = str1 * 2

# print(str2) #--> codeyugcodeyug




# - Ex :

# print("codeyug"*2)     #--> codeyugcodeyug
# print("codeyug " * 2)  #--> codeyug codeyug






# - Ex :  [usecase]


# print("Hello")
# print('-' * 25)
# print("Anubhav")

# output :
# Hello
# -------------------------
# Anubhav


















# :: Deleting :-

# - We can not delete characters  of string. But  , deleting entire string is possible using 'del' keyword. 

# - Example :

# str1 = 'codeyug'
# del str1 
# print(str1)

#  output :    print(str1)
#           ^^^^
# NameError: name 'str1' is not defined. Did you mean: 'str'?




# NOTE :  writing direct string in sequence to concatenate them . 

# str = 'hello' 'anubhav'

# print(str)  #--> helloanubhav



# _______________________________________________________________________________________________________________________ 




# :: Iteration over string :

# - Ex : 
# name = "Anubhav"

# for char in name:
#     print(char , end = " ")  # --> A n u b h a v
    
    
    
    
    
    
    
    
    
    
    


# :: Length of a string : 

# - Length of string is nothing but number of characters in string. 
# - Two ways of finding length :

# 1.) By manual programming
# 2.) By len() function





# 1.) By manual Programming :

# name = input("Enter the string")

# length = 0

# for char in name:
#     len += 1
    
# print(f"lenth of string {name} is : {length}")





# 2. By len() function :

# name = input("Enter the string")

# print(len(name))






# :--> string membership :

# name = 'codeyug' 

# if 'de' in name:
#     print('present')  #--> present


    
    
# Ex :  calculate number of vowels in string. 

# str1 = input("Enter string :")
# vowels = ['a' , 'e' , 'i'  , 'o' , 'u']

# count_vowels = 0

# for char in str1:
#     if char in vowels:
#         count_vowels  += 1
        
# print(f"The total number of vowels in {str1} is {count_vowels}")
    
    
    
    
    
    
    
    
    
    
    
# _______________________________________________________________________________________________________________________ 




# :: count() method in Python : 

# - Inbuilt method which returns a number of times a specified substring in a string. 
# - Syntax : string.count(substring , start , end)
# - start , end are optional. 
# - Substrig is required argument. 
# - Default start is index 0. 
# - Default end is end of string ( index length of string ). 

# - substring :-  A string whose occurrences is to be calculated. 
# - start     :-  From where to start searching. (start index). 
# - end       :-  Where to end searching. (end index). 


# -Ex :


# str1 = input("Enter the string :")
# counter = str1.count('Co')

# print("Length of string :" , counter)  #--> 2




# - Ex :

# str1 = input("Enter the string :")
# counter = str1.count('Co' , 3 , 7)
# print('Length of string :' , counter) #--> 1




# - Ex : count how many times india wins the world cup



# world_cup_winners = '''
#   1975: West Indies , 
#   1979: West Indies,
#   1983: India,
#   1987: Australia,
#   1992: Pakistan,
#   1996: Sri Lanka,
#   1999: Australia,
#   2003: Australia,
#   2007: Australia,
#   2011: India,
#   2015: Australia,
#   2019: England,
#   2023: Australia'''
  
  
# world_cup_india = world_cup_winners.count('India') #--> two time
# world_cup_india = world_cup_winners.count('India' , 97)  #--> 1 times
# # ( 1  97  5 --> West Indies)

# print(f"India win world cup : {world_cup_india} times")














# :: enumerate() method in Python :

# 
# - It returns a list of tuples having two value the first is the index of the character and the second is the character itself.

# - Ex : 


# name = "Anubhav"

# print(list(enumerate(name)))
    
# output : [(0, 'A'), (1, 'n'), (2, 'u'), (3, 'b'), (4, 'h'), (5, 'a'), (6, 'v')]




# ___________________________________________________________________________________________________________________________







# :: startswith() method in Python :

# - This inbuilt method returns True if string starts with specified prefix. if not , returns False. 

# - Syntax :  string.startswith(prefix , start , end)

# - Substring(prefix) :- A string or tuple to be checked.


# - Ex :

# message = "hello , welcome"

# print(message.startswith('hello'))  #--> True
# print(message.startswith('heo'))    #--> False


# print(message.startswith(',we' , 5, 11))    #--> True 




# - Ex : 

# Write a program for finding country of mobile number using prefix. 

# mob_number = input("Enter mobile number :")

# if mob_number.startswith('+91'):
#     print(f"{mob_number} belongs to india")
    
# elif mob_number.startswith('+1'):
#     print(f"{mob_number} belongs to america")

# elif mob_number.startswith('+86'):
#     print(f"{mob_number} belongs to china")
    
    
    
















# :: endswith() :

# - This inbuilt method returns True if string with specified suffix. if not , returns False. 

# - Syntax : string.endswith(suffix , start , end)

# - suffix : A string or tuple to be checked. 
# - start : starts index from where searching starts. 
# - end : End index of searching. 


# - Ex :

# message = 'hello , Anubhav'

# print(message.endswith('bhav' , 5))  #--> True




# - Ex : 

# write a program to check the website TLD(top level domain). 

# url = input("Enter URL :")
# if url.endswith('.com'):
#     print("commercial website")
# elif url.endswith('.edu'):
#     print("educational website")
# elif url.endswith('.org'):
#     print("organization website")












    
    
    
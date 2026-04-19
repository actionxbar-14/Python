
# :: Youtube Playlist Content : 

# --> lecture-66 : C-style string formatting.
# --> lecture-67 : f-string in Python.
# --> lecture-68 : center() & zfill() in Python. 
# --> lecture-69 : spilt() function in Python. 
# --> lecture-70 : join() method in Python. 


# _______________________________________________________________________________________________________________________ 



# :: String formatting in Python :

# 1.) C style formatting
# 2.) .format() method 
# 3.) f-string 














# 1.) C style formatting : 

# - % operator/modulo operator is used for formatting string.This is also called as format specifier. 
# - String ---> %s , Float ---> %f , Integer ---> %d . 

# - Syntax :  print("format specifier"%(data))    #--> [Data can be literal , variable , expression etc]

# - Ex : 

# print("My name is %s and my age is %d" %("jay" , 22)) 


# - Ex :

# name = input('Enter name :')
# age = int(input('Enter age :'))

# print("Entered name is %s and age is %d"%(name, age))








# NOTE : without managing the order of name and age. 

# --> Using key-value pair. 
# --> Syntax : print("format specifier"%{key:value})


# - Ex : 

# print("My name is %(name)s and my age is %(age)d" %{'name' : "jay" , 'age' : 22})


# - Ex :

# name  = input("Enter the name :")
# age = int(input("Enter the age :"))

# print("My name is %(name)s and age is %(age)d" %{'age' : age , 'name' : name})





















# 2.) .format() method for string formatting :

# - Ex : 
    
# a = "shakshi" # name 
# b = 22 # age

# msg = "My name is {0} and I am {1} years old.".format(a,b)
# print(msg)











# 3.)  f-string in Python :  (Python 3.6 version)

# - f-string is also known as 'Literal string interpolation'. 
# - Every f-string statement consists of two parts :-
# 1.) charactet "f" or "F". 
# 2.) string you want to format. 


# - Syntax :  f"string"


# - Ex :


# name  = input("Enter the name :")
# age = int(input("Enter the age :"))

# print(f"the name is {name} and age is {age}")




# - Ex : Expressions 

# print(f"{5*5}") #--> 25


# - Ex :  we can call function inside f-string. 

# def printer(name) :
#     return "hello" + name 

# print(f"{printer('jay')}")   #--> hellojay










# NOTE:  Why to use f-string. 

# 1.) simple syntax. 
# 2.) Faster than format() method and c-style formatting. 








# _______________________________________________________________________________________________________________________ 




# :: center() method in Python :

# - The center() method allign string to the center by filling paddings left and right of the string. 
# - Syntax : string.center(width , fillchar). 

# ---> Width :- length of string with padded characters. 
# ---> fillchar :- padding character. It is optional argument. Default value is space. 



# - Ex :

# string = "Be a programmer"

# str1 = string.center(25 , '*')

# print(str1)  #--> *****Be a programmer*****


# - Ex :

# string = "Be a programmer"

# str1 = string.center(length(string) + 10 , '*')  #--> #--> *****Be a programmer*****
















# :: zfill() in Python :

# - The zfill() method returns a copy of string with '0' character padded to the left. 

# - syntax: string.zfill(width)





# - Ex :

# string = "Be a programmer"

# str1 = string.zfill(len(string)+5)
# print(str1)  #--> 00000Be a programmer



# - Ex :

# num = '-182'
# print(num.zfill(8))  #--> -0000182














# _______________________________________________________________________________________________________________________ 




# :: split() method in Python : 

# - the split() method breaks up a string at specified separator and returns a list of strings. 
# - syntax : string.split(seperator , maxsplit). 

# --> separator : separator for splitting string. By default , whitespace is a seperator. 
# --> maxsplit : how many splits to do. 



# -  Ex : 

# msg = "i want to become python programmer"

# words = msg.split()
# print(words)  #--> ['i', 'want', 'to', 'become', 'python', 'programmer']
# print("no. of words =", len(words))  #--> no. of words = 6






# - Ex :

# countries = "india , pakistan , australia , srilanka , america , england"
# split_country = countries.split(",")
# for country in split_country:
#     print(country)  #
    
# output  :
# india 
#  pakistan
#  australia
#  srilanka
#  america
#  england





# - Ex : 


# countries = "india , pakistan , australia , srilanka , america , england"

# country = countries.split("," , 3)

# print(country)  # output : 
# # ['india ', ' pakistan ', ' australia ', ' srilanka , america , england']










# _______________________________________________________________________________________________________________________ 





# :: Join() method in Python :

# - The join() method takes all items in iterable (string) and joins them into one string. 
# - Syntax : seperator.join(iterable)

# --> iterable : object capable of returning it's member one at a time.  (list , string , tuple)



# - Ex :

# l = ['P' , 'y' , 't' , 'h' , 'o' , 'n']

# str1 = ''.join(l)
# print(str1)  #--> Python
# print(type(str1))  #--> <class 'str'>




# - Ex :

# lang = { 'java' , 'Python' , 'c++'}
# lang1 = '-->'.join(lang)

# print(lang1)  #--> java-->Python-->c++





# - Ex : using with dictionary


# # --> .join() operates over the key while using inside the dictionary.
# country = {'india' : 20 , 'nepal' : 12  , 'england' : 18}
# print(' country '.join(country))  #--> india country nepal country england 

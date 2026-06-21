

# :: Youtube Playlist Content : 

# --> lecture-271 : QR Code using Python.
# --> lecture-272 : Rolling Dice Using Python. 
# --> lecture-273 : Random module in Python. 
# --> lecture-274 : Password without Echoing in Python. 
# --> lecture-275 : Prevent Password Echo. 


# ______________________________________________________________________________________________________________________________________



# :: What is QR code ? 

# - QR code stands for Quick Response code. It is a 2D pictographic code used for its fast readability and large storage capacity. 
# - The information can be any kind of data. 




# :--> Steps to follow :- 

# 1. Install module 'qrcode' using pip. 
# 2. Import module 'qrcode'. 
# 3. Create an object of 'QRCode' class. 
# 4. Add data in qr object using 'add_data()' method. 
# 5. Create image of qrcode and save it. 




# import qrcode 



# qr = qrcode.QRCode(
#     version=15,
#     box_size=10 ,
#     border = 5 
# )



# data = "https://github.com/actionxbar-14"

# qr.add_data(data)

# qr.make(fit=True)
# img = qr.make_image(fill = "black" , back_color = "white")
# img.save('Github_profile_QR.png')



# ______________________________________________________________________________________________________________________________________




# :: Python Program for rolling dices : 

# import random 

# min =  1
# max =  6

# roll_again = 'yes'

# while roll_again == 'yes':
#     print("rolling the dices....")
#     print("the values are....")
#     print(random.randint(min , max))  # dice1 
#     print(random.randint(min , max))  # dice2

#     roll_again = input('roll the dice again :')






# ______________________________________________________________________________________________________________________________________



# :: Random Module in Python : 

# - 'random' module is used for generating random things. 
# - it has many Number of functions. 



# :--> Generating random numbers :- 

# 1. random() method.
# 2. randint() method.
# 3. randrange() method. 





# 1. random() : 
# - It generates a float random number between 0.0 To 1.0.
# - Ex :  

# import random 

# print(random.random())  







# 2. randint() : 
# - it takes two argument (start , end ) and print the random integer number between them. 


# - Ex : 

# import random 

# print(random.randint(10 , 200))







# 3. randrange() : 
# - it takes three argument (start , stop , step) and it prints the random number between the numbers which are produced by this (start, stop  , step). 

# - Ex : 

# import random 

# print(random.randrange(10 , 30  ,4))   #:-  10  , 14 , 18 , 22 , 28 [ inme se hi random number dega]









# :--> Ex :  Python program to generate 10 random numbers between 1-100. 

# import random 

# rand_nums = []

# for i in range(10):
#     rand_nums.append(random.randint(1 , 100))

# print(rand_nums)  # output : [44, 90, 54, 36, 96, 57, 6, 100, 20, 68]




# ______________________________________________________________________________________________________________________________________







# :: Getpass Module in Python : 

# - The gatepass is a module in Python. 
# - It asks the user for a password without echoing , which means without displaying what the user is typing. 
# - Supported only for terminal-based apps. 



# :--> There are two functions : 

# 1. getpass() function  
# 2. getuser() function




# - Ex :   getpass() function



# import getpass


# my_password = getpass.getpass(prompt= "Enter the password :")


# if my_password == 'admin':
#     print("login successfull!")
# else:
#     print("login failed! , incorrect password")


# NOTE: prompt is optional , default it prints as "password :"








# - Ex : getuser() function [ print the current username in the form of string. if it cannot find then it give an error .]

# import getpass 

# user_name = getpass.getuser()

# pass_word = 'admin'



# #interface : 

# user = input("Enter the username :")

# password = getpass.getpass()



# if user == user_name and password == pass_word:
#     print("Login successfull!")

# else:
#     print("incorrect credentials!")






# ______________________________________________________________________________________________________________________________________






# NOTE : 


# print(bool(None))  # False

# print(bool(1))   # True

# print(bool(0))  # False

# print(bool(''))  # False







# :: any() and all() in Python : 

# :--> any() :- 
# - This function return an boolean True if any True value present in the given object. 
# - Ex : 

# list1 = [0,0,0,0,0,1,0,1,0]
# print(any(list1)) # output : True




# :--> all() :- 
# - this function return an boolean True if all the value in the object are True.
# - Ex : 

# list1 = [0,0,0,0,0,1,0,1,0]
# print(any(list1)) # output : False
 





# - Ex : Python program for sublist present or not. 


# mylist = eval(input("Enter a list :"))  # ex: [1,2,3,[1,2,3]]


# if any([isinstance(element , list) for element in mylist]):
#     print("sublist is present")
# else:
#     print("sublist is not present")









# ______________________________________________________________________________________________________________________________________




# :: Write a Python program for checking digits present or not in list using any function. 



# def check_digits(lst):

#     if any(isinstance(eval(str(item)) , int) for item in lst):
#         return "digits present!"
    
#     return "digits not present!"



# my_list = ["hello", "25", "python"]

# print(check_digits(my_list))
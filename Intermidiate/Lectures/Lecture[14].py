
# :: Youtube Playlist Content : 

# --> lecture-71 : in-built functions in Python string.
# --> lecture-72 : title() and capitalize() in Python. 
# --> lecture-73 : isalnum() & isdigit() / isalpha() in Python. 
# --> lecture-74 : isupper() & islower() / istitle() string method. 
# --> lecture-75 : isidentifier() , isprintable() , isspace() in Python. 


# ______________________________________________________________________________________________________________________________________



# :: In-built functions in Python string  :





# --> upper() :
# - The string upper() method converts all lowercase characters in a string into uppercase characters and returns a new copy. 
# - This method doesn't take any parameter. 


# - Syntax :  string.upper()

# - Ex  :

# str1 = "Hello , WelcoME"

# Upper_str = str1.upper()

# print(Upper_str)  #--> HELLO , WELCOME



# - Ex (practical):

# user_input = input("Enter your usename :")
# correct_username = 'Anubhav'

# if user_input.upper() == correct_username.upper():
#     print("Valid username")













# --> lower() :
# - The string lower() method converts all uppercase characters in a string into lowercase characters and returns a new copy. 
# - This method doesn't take any parameter. 

# - Syntax :  string.lower()


# - Ex :

# str = "CODEyug"

# lower_str = str.lower()

# print(lower_str)

















# --> swapcase() :
# - lowercase characters ko uppercase characters mai convert kr dega. 
# - uppercase characters ko lowercase characters mai convert kr dega. 
# - and return a copy of string. 

#  - This method doesn't take any parameter. 


# - Syntax : string.swapcase()

# - Ex :

# str = "CODEyug" 

# swap_str = str.swapcase()

# print(swap_str)










# ________________________________________________________________________________________________________________________________________
 



# :: title() :
# - The string title() method returns a string with the first letter of each word capitalized. 
# - Syntax :   string.title() 

# - This method doesn't take any parameter. 

# - Ex  :

# msg = 'i love you'

# title_msg = msg.title()

# print(title_msg)   #--> I Love You



# - Ex : 

# msg = '#i $love @you'

# title_msg = msg.title()

# print(title_msg)   #--> #I $Love @You












# :: capitalize() :
# - The string capitalize() method returns a string with the first letter of whole string is capital and others are in lowercase. 

# - Syntax : string.capitalize() 


# - Ex :

# msg = "i love programming" 
# capitalize_msg = msg.capitalize()

# print(capitalize_msg)   #--> I love programming


# - Ex : 




# msg = "+ love programming" 
# capitalize_msg = msg.capitalize()

# print(capitalize_msg)   #--> + love programming





# ________________________________________________________________________________________________________________________________________
 
 
 
 
 
 
 
# :: Functions for string validation :







# 1. Python isalnum() :
# - alphanumeric = alphabets(A-Z and a-z) / Numbers(0-9)
# - It returns True  : If all characters in string are alpha-numeric , else return False. 
# - It does not take any parameter.
# - NOTE : 

# Welcome --> alphanumeric
# welcome1234 --> alphanumeric
# welcome 1234 --> space aaya toh alphanumeric nahi
# welcome#1234 --> alphabets ya numeric value ke alawa kuch bhi aya toh alphanumeric nahi hoga. 

# - Syntax : string.isalnum()


# - Ex :

# msg = "Welcome1234"
# print(msg.isalnum())  #--> True


# - Ex :

# msg = "Welcome 1234"
# print(msg.isalnum())   #--> False

















# 2.  Python isalpha() :
# - It returns True if All characters in string are alphabets , else return False. 
# - Syntax :   string.isalpha()


# - Ex :

# msg = "Welcome"
# print(msg.isalpha())  #-->True


# - Ex :  

# msg = "Welcome$"
# print(msg.isalpha())  #--> False

















# 3. Python isdigit() :
# - It returns True If All charaters in string are digits , else return False. 
# - Syntax : string.isdigit() 

# - Ex :

# msg = "907545884"

# print(msg.isdigit())  #--> True


# - Ex :

# msg = "9075 45884"

# print(msg.isdigit())  #--> False



# - Ex : 

# msg = "90754hello5884"

# print(msg.isdigit())  #--> False


# - Ex :

# mob_no = input("Enter the mobile number :")

# if mob_no.isdigit() == True:
#     print("mobile no. is valid")
# else:
#     print("Invalid number")








# ________________________________________________________________________________________________________________________________________




# 4. isupper() :
# - return True if all alphabets are in UPPERCASE. 
# - return False if all alphabets are in lowercase. 
# - This method does not take any arguments.

# - Syntax : string.isupper()



# - Ex :

# str1 = "WELCOME TO MY HOME"

# print(str1.isupper())  #--> True


# - Ex :


# str1 = "WELCOME TO 5Y HOME"

# print(str1.isupper())  #--> True


# - Ex :


# str1 = "WELCOME TO %Y HOME"

# print(str1.isupper())  #--> True




# - Ex :


# str1 = "WELCOMe TO %Y HOME"

# print(str1.isupper())  #-->  False






















# 5. islower() : 
# - It returns True if all aplhabets are in lowercase. 
# - False if any alphabets is in UPPERCASE. 

# - Syntax : string.islower()



# - Ex :

# str1 = "coDeyug" 
# print(str1.islower()) #--> False



# - Ex :

# str1 = "codeyug" 
# print(str1.islower()) #--> True





# - Ex :

# str1 = "code @yug" 
# print(str1.islower()) #--> True





















# 6. istitle() :
# - It returns True if string is titled string. 
# - It returns False if string is not titled string. 
# - This method doesn't take any arguments.

# - titled string :  'Python Is Easy' { first letter of all word must be capital}. 


# - Syntax : string.istitle()





# - Ex : 


# str1 = "Python Is Easy"
# print(str1.istitle())   #--> True



# - Ex : 

# str1 = "Python Is @asy"
# print(str1.istitle())  #--> False 












# ________________________________________________________________________________________________________________________________________




# 7. isidentifier() :
# - It returns True if string is valid identifier. Else , returns False. 
# - This method doesn't take any arguments.
# - Syntax : string.isidentifier()  

# - Ex : 

# string = "abcdef"
# print(string.isidentifier())  #--> True


# - Ex :

# string = " abcdef"
# print(string.isidentifier())  #--> False












# 8. isprintable() :
# -  It returns True if all characters are printable or the string is empty. 
# -  Syntax : string.isprintable()  

# - This method doesn't take any parameter. 
# - Printable characters : characters that occupies printing space on the screen.  



# - Ex : 

# str1 = " Python is easy"
# print(str1.isprintable())  #--> True




# - Ex : 

# str1 = " Python \nis easy"
# print(str1.isprintable())  #--> False





# - Ex : 

# str1 = ""
# print(str1.isprintable())  #--> True













# 9. isspace() : 
# -  returns True if all characters are spaces. 

# - Syntax : string.isspace() 

# - Ex : 

# str1 = "    "
# print(str1.isspace())  #--> True


# - Ex : 

# str1 = ""
# print(str1.isspace())  #--> False



# - Ex : 

# str1 = "\t"
# print(str1.isspace())  #--> True




# str1 = "\n"
# print(str1.isspace())  #--> True
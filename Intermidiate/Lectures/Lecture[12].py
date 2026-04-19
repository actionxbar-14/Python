
# :: Youtube Playlist Content : 

# --> lecture-61 : strip in Python
# --> lecture-62 : How to Reverse string in Python. 
# --> lecture-63 : Comparing Strings in Python. 
# --> lecture-64 : replace() method in Python. 
# --> lecture-65 : find() and rfind() / index() and rindex() in Python.


# _______________________________________________________________________________________________________________


# :: Removing leading and trailing charactera from given string :

# - Three important in-built methods :

# 1.) lstrip()
# 2.) strip() 
# 3.) rstrip()





# 1.) lstrip() :

# - It removes any leading characters(space is the default leading characters to remove. )
# - Syntax : string.lstrip(characters)
# - characters : a set of characters to remove as leading characters. It is optional argument. 
# - All combinations of characters are removed from left untill first mismatch. 


# - Ex :

# name = input("Enter your name :")
# print(name)  Output :  ____anubhav____    
# name = name.rstrip()
# print(name)  output :  anubhav______


# - Ex : 

# urls = ['http://www.cricbuzz.com' , 'http://www.youtube.com' , 'http://www.facebook.com']

# for url in urls:
#     url = url.lstrip('htp:/w.')  #[ 'htp:/w' == 'http:/www.']
#     print(url)


# output :
# cricbuzz.com
# youtube.com
# facebook.com



# - Ex : lstrip() pahle unmatch character ke baad ke sare words ko print krr deta hai. 

# urls = ['http://www.cricbuzz.com' , 'http://www.youtube.com' , 'http://www.facebook.com']
# for url in urls:
#     url = url.lstrip('htp/w.')  
#     print(url)


# output :

#://cricbuzz.com
#:// youtube.com
#://facebook.com









# 2.) strip() :

# - It removes leading and trailing characters (space is the default characters to remove) . 
# - Syntax : string.strip(characters)
# - characters :- a set of characters to remove. It is optional argument. 
# - All combinations of characters are removed from left unitl first mismatch. Then , it remove from right untill first mismatch. 


# - Ex :


# urls = ['http://www.cricbuzz.com' , 'http://www.youtube.com' , 'http://www.facebook.com']
# for url in urls:
#     url = url.lstrip('htp://com')  
#     print(url)

# Output :

# www.cricbuzz.com
# www.youtube.com
# www.facebook.com










# 3.) rstrip() :


# - It removes any trailing characters(space is the default leading characters to remove. )
# - Syntax : string.rstrip(characters)
# - characters : a set of characters to remove as leading characters. It is optional argument. 
# - All combinations of characters are removed from right untill first mismatch. 


# - Ex :

# name = input("Enter your name :")
# print(name)  Output : ____anubhav____    
# name = name.rstrip()
# print(name)  output : ______anubhav


# - Ex : 

# urls = ['http://www.cricbuzz.com' , 'http://www.youtube.com' , 'http://www.facebook.com']

# for url in urls:
#     url = url.lstrip('htp:/w.')  #[ 'htp:/w' == 'http:/www.']
#     print(url)


# output :
# cricbuzz.com
# youtube.com
# facebook.com



# - Ex : rstrip() pahle unmatch character ke baad ke sare words ko print krr deta hai. 

# urls = ['http://www.cricbuzz.com' , 'http://www.youtube.com' , 'http://www.facebook.com']
# for url in urls:
#     url = url.rstrip('.com')  
#     print(url)


# output :

# http://www.cricbuzz
# http://www.youtube
# http://www.facebook












# _______________________________________________________________________________________________________________________




# :: Reverse string in Python :

# - Three ways of reversing string :-
# 1.) using while loop
# 2.) using for loop
# 3.) using slicing









# 1.) using while loop :


# - Create empty string which will have reversed string. 
# - Visit characters in name in reverse order. 
# - After each visiting , concatenation to r_name. 



# name_input = input("Enter the name :")
# print("Orignal string : " , name_input)
# length  = len(name_input)
# i = 0
# rev_name = ''
# while i < len(name_input):
#     rev_name += name_input[(length - i)-1]
#     i += 1

# print("Reversed string using while loop : " , rev_name , end = " ")    

















# 2.) using for loop : 


# name_input = input("Enter the name :")
# print("Orignal string : " , name_input)
# length  = len(name_input)

# rev_name = ''
# for char in range(len(name_input)):
#     rev_name += name_input[(length-char) - 1]
   

# print("Reversed string using while loop : " , rev_name , end = " ")    







# 3.) using slicing :


# name_input = input("Enter the name: ")

# print("Original string :" ,name_input)

# print("reversed string :" , name_input[::-1])









# _______________________________________________________________________________________________________________________




# :: Python string comparison :

# - Python string comparison can be done using comparison operators ( == , != , > , < , >= , <=). 
# - The characters of both strings are compared one by one. 
# - When different characters are found , then their unicode values is compared. 



# - Ex :

# name = 'codeyug' 

# name1 = 'codeyug'

# print(name == name1)  #--> True 



# - Ex : 


# name = 'codeyug'

# name1 = 'codeyug' 

# print(name > name1)  #--> False

# print(ord('u') , ord('y'))    #--> ord('u') --> 117 , ord('y') --> 121



# - Ex :



# x = 'a' 
# y = 'A'

# print(ord(x) , ord(y))  #--> ord('x') --> 97 , ord('y') --> 65  


# print(x > y)   #--> True   



















# _______________________________________________________________________________________________________________________





# :: replace () method in Python : 

# - The replace() method returns a copy of string where all occurences of a sub-string is replaced with another substring . 


# - Syntax : string.replace(old_value , new_value , count) . 


# --> old_value :-  old substring you want replace. 
# --> new_value :-  new substring for old one. 
# --> count     :-  optional argument . Number of times you want to replace. 



# - Ex : 

# msg = ' C is object-oriented Programming language , C is easy'

# msg1 = msg.replace("C" , "Python" , 1)

# print(msg1)  # output :  Python is object-oriented Programming language , C is easy



# - Ex :


# msg = ' C is object-oriented Programming language , C is easy'

# msg1 = msg.replace("C" , "Python" , 2)

# print(msg1)  # output :  Python is object-oriented Programming language , Python is easy






# - Ex :

# msg = "helloRam"  
# print(msg)   #--> helloRam
# msg1 = msg.replace("ll" , "oo")

# print(msg1)  #-->  heoooRam














# _______________________________________________________________________________________________________________________




# :: find() in  Python :

# - The find() method returns "index" of first occurrence of substring. If not found , it returns -1. 
# - Syntax : string.find(substring , start , end)

# --> substring : The substring to search for. 
# --> start     : where to start search. Default is 0. 
# --> end       : where to end the search. Default is end of string. 


# - Ex :

# msg = "hellojay" 

# msg1 = msg.find('l')

# print(msg1)  #--> 2




# - Ex : 

# msg = "Python is powerfull programming language" 

# print(msg.find("powerfull"))   #--> 10






















# :: rfind() in Python :

# - The rfind() method returns index of last occurrence of substring. If not fount, it returns -1. 
# - Syntax : string.rfind(substring , start , end)




# - Ex : 

# msg = 'Python powerfull is powerfull,  powerfull programming language'

# print(msg.rfind('powerfull'))  #--> 32
# print(msg.rfind("xyz"))  #--> -1




















# :: index() in Python :
 
# - The index() method returns index of first occurrence of substring. If not fount, it returns 'valueError'. 
# - Syntax : string.index(substring , start , end)



# # - Ex :

# msg = 'Python powerfull is powerfull,  powerfull programming language'

# print(msg.index('powerfull'))  #--> 7
# print(msg.index("xyz"))  #--> valueError























# :: rindex() in Python :
 
# - The rindex() method returns index of last occurrence of substring. If not fount, it returns 'valueError'. 
# - Syntax : string.rindex(substring , start , end)



# - Ex :

# msg = 'Python powerfull is powerfull,  powerfull programming language'

# print(msg.rindex('powerfull'))  #--> 32
# print(msg.rindex("xyz"))  #--> valueError



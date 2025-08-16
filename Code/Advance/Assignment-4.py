# Question : 1  
# Limit the decimal places to digits using '.format()' method and print result , for the variable pi = 3.14159265359.

# Answer:
# pi = 3.14159265359

# print(round(pi,2)) #output : 3.14

# ::using ( ().format ) method :

# print("Value of pi is {:.2f}".format(pi)) #output : 3.14
# print("Value of pi is {:.1f}".format(pi)) #output : 3.1
# print("Value of pi is {:.0f}".format(pi)) #output : 3

# :: using f-string method :

# print(f"{pi:.2f} using f-string")  #output : 3.14 using f-string





# Question : 2 Extract characters from index 2 to 8 with a step of 2: Given
# my_string = "Python Course" , slice characters from index 2 to 8 , skipping every other char.

# my_string = "Python Course"
# print(my_string[2:8:2]) #output : Pyh



#Question** : 3 Slice to get only the middle character(s) : 
# For my_string = "Madhav" , use slicing to extract the middle character(s).  -> 6 characters(even)
# For my_string = "Madhava" , use slicing to extract the middle character(s).  -> 7 characters(odd)


# my_string = "Madhav"  #(dh is middle) - odd
# #  index  =  012345


# my_string2 =  "Madhava"  #(h is middle) - even
# #  index   =   0123456


# def mid_str(word):
#     middle = int(len(word)/2)

#     if len(word) % 2 == 0:
#         return word[middle-1 : middle+1]  #2:4

#     else:
#         return word[middle]


# print(mid_str(my_string))  #output : dh
# print(mid_str(my_string2))  #output : h




# name = "Anubhav"  #middle word : [b]
# #index = 0123456
# def middle_word(name):
#     middle = int(len(name)/2)
#     if len(name) % 2 == 0:
#         return name[middle-1 : middle+1]
#     else:
#         return name[middle]

# print(middle_word(name))





# Question : 4 Remove the first 3 and last 3 characters : 
# Given my_string = "Regression Analysis" , remove the first 3 and last 3 characters.


# my_string = "Regression Analysis"   #[ans : ression Analy]
# # index =    0123456789012345678

# remove_first_three = my_string[0:3]
# print(remove_first_three)  # output : Reg

# remove_last_three = my_string[-4:len(my_string)-1]
# print(remove_last_three)   # output : ysi


# print(my_string[3:-3])  #output: ression Analy





#Question : 5 Get the substring that starts 4 characters from the end to the last character: For my_string = "Classification" , slice the string starting from the 4th character from the end to the last character.


# Answer : 

# my_string = "Classification"

# print(my_string[-4:]) # output : tion


#Question : 6 How to Reverse a String Using Python String Methods?
# Answer :

# word = "Python"
# print(word[::-1])  #output : nohtyP


#Question : 7 Write a Python function to check if a string is a palindrome using string methods.

# Answer : 

# word = "madam"
# word2 = 'madan'

# def is_palindrome(s):
#     if s == s[::-1]:
#         print(f"{s} is an palindrome")
#     else:
#         print(f"{s} is not an palindrome")

# print(is_palindrome(word))  #output : madam is an palindrome
# print(is_palindrome(word2))  #output : madan is not an palindrome


#Question : 8 Difference Between find() and index() in python.

# Answer : 

# name = "Anubhav"

# # ::find : find the respective letter if it is present than return its index value and if it is not present than return -1

# print(name.find('A'))  # output : 0
# print(name.find('c'))  # output : -1
# print(name.find('a'))  # output : 5

# :: index : simple find the index of a letter in a given string.

# print(name.index('A'))  # output : 0





# Question : 9 Efficient String Concatenation method : 
# Why is using join() often more efficient than using concatenation in a loop.

# Answer : 


# 1. 

# '+' in a Loop = Inefficient Memory Use
# ex:
# result = ''
# for word in words:
#     result += word

# #NOTE : 
# Python creates a new string every single time. Why? Because strings are immutable in Python.

# So:

# On the first loop: '' + word1 → new string

# On the second: new_string1 + word2 → another new string

# And so on...

# Imagine doing that 10,000 times. Python has to:

# Allocate new memory

# Copy all the previous characters

# Add the new word

# Throw away the old string

# That’s a lot of overhead.


# 2.

# result = ''.join(words)

# Python knows the size of the final string in advance

# It allocates memory just once

# Then it fills it in one go

# This is way faster and way more memory efficient.




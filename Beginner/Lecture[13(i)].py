
                     # TOPIC :   Strings[Part - 1]
                        #      [ Format & Operators ]
 



#Strings :
# A string is a sequence of characters. In python , strings are enclosed within single(') or double or triple(""") quotation marks.

# ex:

# print('Hello World!')  # use type() to check data type.

# print("Won't Give Up!")

# print('''  "Quotes" and 'single quotes' can be tricky.  ''') #output : "Quotes" and 'single quotes' can be tricky.

# print("  \"Quotes\" and 'single quotes' can be tricky.  ") #output : "Quotes" and 'single quotes' can be tricky.






#Formatted String :
# A Formatted string in python is a way to insert variables or expressions inside a string. It allows you to format the output in a readable and controlled way.

# -> Old - style formatting (% operator).
# -> str.format() method.
# -> F-string(formatted string literals).



# --> Old - style formatting(% operator):-
# This approach uses the % operator and is similar to string formatting in language like c.

# Syntax:  "string % value"

# Ex:

# name = "Anubhav"
# age = 20
# print("My name is %s and age is %d." % (name,age)) # output : My name is Anubhav and age is 20.
# print("My name is %s and age is %d." % (age,name)) #output : TypeError: %d format: a real number is required, not str.




#NOTE: %s and %d are placeholder for strings and integer.






# --> str.format() method :- available in python3.

# In python3, the format() method is more powerfull and flexible than the old-style % formatting.

# Syntax: "string {}".format(value)

# Example:
# name = "Anubhav"
# age = 20
# print("My name is {} and I'm {}.".format(name,age))

# You can also refrence the variables by index or keyword:

# print("My name is {0} and I'm {1}.".format(name,age)) #indexing ,
# output : My name is Anubhav and I'm 20.

# print("My name is {0} and I'm {0}.".format(name,age)) #indexing ,
# output:My name is Anubhav and I'm Anubhav.

# print("My name is {1} and I'm {0}.".format(name,age)) #indexing ,
# output : My name is 20 and I'm Anubhav. 


# print("My name is {name} and I'm {age}.".format(name = "Anubhav",age = 20)) 
# #output : My name is Anubhav and I'm 20.







# F-strings(formatted string literals) :-

# -In Python 3.6 , F-strings are the most concise and efficient way to format strings. You prefix the string with an f or F , and variables or expressions are embedded directly within curly braces{}.

# Syntax : f"string {variable}"

# # Example:
# name = "Anubhav"
# age = 20
# print(f"My name is {name} and i am {age} years old")

# You can also perform expressions inside the placeholders
# print(f"2 + 2 = {2 + 2}") #output : 2 + 2 = 4.






# :: Escape characters :
# - Escape characters in python are special characters used in strings to represent whitespace , symbols or control characters that would otherwise be difficult to include. An escape character is a [ backslash \ ] followed by the character you want to insert.

# print('Hello \n World!')  # \n for new line.
# output : Hello
        # World!

# print('Hello \t World!')  # \t for tab.
# output : Hello    World!

# print(" \"Quotes\" and \'single quotes\' can be tricky. ") # print single and double quotes.
# output : "Quotes" and 'single quotes' can be tricky.











# String Operators :

# 1. + ( concatenation ) - Add values on either side of the operator.
# ex:
# a = "Hello"
# b = "Python"

# print(a+b) #output : HelloPython



# 2. * ( Repetition ) - Create new strings , concatenating multiple copies of the same string.
# ex:
# a = "Hello"
# b = "Python"
# print(a*2) #output : HelloHello


# 3. [] ( Slice ) - Gives the character from the given index.
# ex :
# a = "Hello"
# b = "Python"
# print(a[0]) #output : H
# print(a[1]) #output : e


# 4. [:] (Range Slice) - Gives the character from the given range.
# ex:
a = "Hello"
# print(a[1:4]) #output : ell
# print(a[:]) #output : Hello
# print(a[0:3]) #output : Hel


# if 'H' in a:
#     print(f"{a} contain the letter H")  

# if 'H' not in a:
#     print(f"{a} not contain the letter H")  
    #output : Hello not contain the letter H



:: Raw string :  reverse the escape character.
# print(r'Hello\nWorld') #output : HelloWorld.
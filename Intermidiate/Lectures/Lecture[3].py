

# :: Youtube Playlist Content : 

# --> lecture-16 : Logical Operators in Python.
# --> lecture-17 : Bitwise Operators in Python. 
# --> lecture-18 : Precedence & Associativity of Operators in Python. 
# --> lecture-19 : PEP8 in Python. 
# --> lecture-20 : Python Assignment - 1.


# _____________________________________________________________________________________________________________________

# :: Logical Operator :-

# - logical operators operates on relational or conditional statements. 
# - Returns True or False based on truth value. 

#--> Python has three logical operators :-

# 1. logical and 
# 2. logical or 
# 3. logical not


# --> Use :-

# 1. making decisions. 
# 2. for controlling flow of code. 



# ____________________________________________________________________________________________


# 1. Logical and :- 
# - if both the condition is true then only it gives "True" as output. 

# - Ex :

# py_lang = input("Do you have Python knowledge(Y/N) :")
# marks_input = int(input("Enter the marks:"))
# candidate_name = input("Enter Your name :")

# if py_lang == 'yes' and marks_input >= 60:
#     print(f"{candidate_name} is selected for interview")
    
# else:
#     print(f"{candidate_name} is not selected for interview")
    
    
    
    


# 2. Logical or :-
# - if one of the given two condition gives true then logical or gives "True" as a output. 

# - Ex: 

# py_lang = input("Do you have Python knowledge(Y/N) :")
# marks_input = int(input("Enter the marks:"))
# candidate_name = input("Enter Your name :")

# if py_lang == 'yes' or marks_input >= 60:
#     print(f"{candidate_name} is selected for interview")
    
# else:
#     print(f"{candidate_name} is not selected for interview")
    
    

    
    
    
    
# 3. Logical not :-

# - it reverese the output of the statement/expression. 

# - Ex:

# age = 10
# marks = 40

# print(age >= 18) #--> False
# print(not age >= 18) #--> True



# __________________________________________________________________________________________________________________


# :: NOTE:-




# 1. True and Expression :  ( Expression )
# - It output depends on the expression because if, expression is true the whole statement is true and if expression is false then whole statement is false. 

# - Ex: 

# a = 10
# b = 20

# print(True and a > b) #--> 'False' (because expression is false)

# print(True and a < b) #--> 'True' (because expression is True)


# print(True and 100)  # Output : 100

# name = "Anubhav"

# print(True and name) # Output : Anubhav


# print(100 and 200) # Output : 200( always give value which is after and statement)

# print("Anubhav" and True)  # Output: True

# print(True and "Anubhav")  # Output : Anubhav








# 2.  False and Expression : 
# - always give false as output. 

# print(False and 100)  #--> False





# 3. True or Expression :  
# - always give the value written before the or statement. 


# print(True or 100)  # Output : True

# print("Anubhav" or "Divyanshu") # Output :  Anubhav





# 4. False or Expresion :
# - always give the value written after the or statement.  

# print(False or 100)  # Output : 100

# print(False or "Anubhav")  # Output : Anubhav




# __________________________________________________________________________________________________________________

#NOTE :

# -->  0(zero) , None , [] , () , {} are gives 'False' as Output. 

# --> anything except these are gives 'True' as Output. 












# __________________________________________________________________________________________________________




# :: Bitwise Operator :-

# - Computers stores data as stream of binary digits. 
# - text , images , videos , audios everything is represented in the form of bits internally. 
# - You can manipulate these bits using Python's bitwise operators. 
# - bitwise operators perform bit by bit operations on binary values of two operands. 

# :-->  Real Use :

# - Encryption and decryption. 
# - compressing files. 
# - error detections. 
# - in IOT devices where Python is used. 


# :--> Below are bitwise operators :-

# 1. Bitwise logical operators :

# - Bitwise and (&) 
# - Bitwise or  (|)
# - Bitwise xor (^)
# - Negation    (~)


# 2. Bitwise shift operators :

# - Bitwise left shift (<<)
# - Bitwise right shift (>>)



# _________________________________________________________________________________________________________________




# 1. Bitwise logical Operators :-


# --> Bitwise and (&) :

# - Bitwise (&) gives 1 if both bits are 1 else gives 0. 
# - Syntax : op1 & op2

# - Ex:

# op1 & op2 

# print(bin(5)) #--> 0b101  (5 -> 101)
# print(bin(4)) #--> 0b100  (4 -> 100)

# print(0b101 & 0b100) #--> 4

# a = 5
# b = 4 

# print(5 & 4)  #--> 4






# --> Bitwise or (|) :

# - Sets bit to 1 if atleast one of both bits is 1. 
# - Syntax :-  op1 | op2 
 
# - Ex: 


# op1 | op2 

# print(bin(5)) #--> 0b101  (5 -> 101)
# print(bin(4)) #--> 0b100  (4 -> 100)

# print(0b101 | 0b100) #--> 5

# a = 5
# b = 4 

# print(5 | 4)  #--> 5









# --> Bitwise Xor(^) :

# - Sets bit to 1 if both bits are different. 
# - Same bit = gives output (0)
# - Different bit = gives output (1)
# - syntax :- op1 ^ op2 

# - Ex:



# op1 ^ op2 

# print(bin(5)) #--> 0b101  (5 -> 101)
# print(bin(4)) #--> 0b100  (4 -> 100)

# print(0b101 ^ 0b100) #--> 1(True)

# a = 5
# b = 4 

# print(5 ^ 4)  #--> 1(True)








# --> Bitwise Negation(~) :

# - Reverse the output of bit. 

# - Ex :

# a = 5
# b = 6

# print(~5)  # Output : -6 

# print(~6)  # Output : -7  




# ______________________________________________________________________________________________________________________


# 2. Bitwise shift operators :


# --> Bitwise left shift operator :-

# - In Python , the  left shift operator (<<) is a bitwise operator that shifts the bits of a binary representation of a number to the left by a specified number. 
# - Syntax : operand  << number of bits. 



# - Ex :

#print(5 << 2)  #--> 20 [ position ko left mai 2 se shift krna hai ]

# 5 --> 0000 0101 after shifting by 2 digit to left it becomes : (0001 0100). 









# --> Right shift operator :-

# - In Python , the right shift operator (>>) is a bitwise operator that shifts the bits of a binary representation of a number to the right by a specified number. 

# - Syntax : operand >> number of bits  

#print( 5 >> 2) # --> 1  [ position ko right mai 2 se shift krna hai ]

# 5 --> 0000 0101 after shifting by 2 digit to right it becomes : (0000 0001).





# ______________________________________________________________________________________________________________________



# :: Precedence & Associativity :-


# --> Precedence : 

# - It specify the order of operations. [BODMAS]
# - To Evaluate expression containing more than two operators , there is a rule of precedence in Python. 
# - It guides the order in which operations are carried out. 
# - It specifies which operator will be evaluated first. 

 
 

# [ Operators            -                        Description ] : ( precedence order)

# 1. **                                           Exponentiation
# 2. +x , -x , ~x                                 Unary Positive , Unary Negative , BitWise negation.
# 3. + , -                                        Addition , Subtraction
# 4. << , >>                                      Bitwise left shift , Bitwise right shift. 
# 5. &                                            Bitwise AND
# 6. ^                                            Bitwise XOR
# 7. |                                            Bitwise OR
# 8. == ,!=, <,<=,>,>=,is,is not,in,not in        Comparisons , identity , and membership.add()
# 9.  not                                         Logical not.
# 10. and                                         Logical and.
# 11. or                                          Logical or.
# 12. :=                                          Walrus









# --> Associativity of operators :

# - When two operators are having same precedence , associativity helps to determine order of evaluation. 
# - Two types of associativity :
# 1. Left to Right
# 2. Right to Left

# - Ex : ( 2 * 3 // 2 )

# NOTE : Exponentiation and assignment operators have right to left associativity. 


# print(2**3**4)


# ____________________________________________________________________________________________________________ 



# :: PEP8 :- 

# - Python Interprise Proposal. 

# - A document that provides guidelines and best practices on how to write Python code. 
# - It was written in 2001 by Guido van Rossum. 
# - These guidelines are helpfull to enhance the readability and consistency of programs. 

# Ex :

# 1. Naming conventions of variables , modules & packages. 
# 2. Variable name for constant and Class-name. 

# REFRENCE : https://peps.python.org/pep-0008/




# ____________________________________________________________________________________________________________ 


# :: Python Assignment - 1 :-



# Question : 1 Is Python case sensitive while dealing with identifiers ?
# Answer : Yes  ( Name , name , NaMe are thre different identifiers)


# Question : 2 Python is compiled or interpreted ?
# Answer : Compiled-interpreted



# Question : 3 IDLE stands for....?
# Answer : Integrated Development Learning Environment. (It is an IDE given by python.org)


# Question : 4 When we download python from it's official website , which compiler we get....?
# Answer :  Ccompiler



# Question : 5 After the following statements , what are the values of x and y ?

# x = 32
# y = x 
# x = 18 


# Answer :  x is 18 and y is 32 



# Question : 6 What is printed when the following statement executed?
# print(12 ,000)

# Answer :   12 000 



# Question : 7 Why Python is called as 'dynamically typed language' ?

# Answer : Python do not requires declaration of data types. When we create Python object , Python automatically interpretes it's datatype. 










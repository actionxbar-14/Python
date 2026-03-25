
                                    # TOPIC : Operators in Python




# Operators : 

# 1. Arithmetic Operators.
# 2. Comparison ( Relational ) Operators.
# 3. Assignment Operators.
# 4. Logical Operators.
# 5. BitWise Operators.
# 6. Identity Operators.
# 7. Membership Operators.








# [ Operators      -     Description ]

# ()                    Parentheses
# **                    Exponentiation
# + , - , ~             Positive-Addition , Negative-Subtraction , BitWise NOT.
# * , / , // , %        Multiplication , Divison , Floor Divison , Modulus.
# == ,!=,>,>=,<=        Comparison - double equal to , not equal to , greater than , greater than equal to ,      less then equal to.
# NOT , AND , OR        logical NOT , Logical AND , Logical OR.
# << , >>               Bitwise Left Shift , Bitwise Right Shift.
# & , ^ , |             Bitwise AND , Bitwise XOR , BitWise OR.









# 1. Arithmetic Operators : Precedence(PEMDAS)

# Operator          Name                    Example ( a = 5, b = 3)
# +                 Addition                    a + b  #o/p : 8
# -                 Subtraction                 a - b  #o/p : 2
# *                 Multiplication              a * b  #o/p : 15
# /                 Division                    a / b  #o/p : 1.666666666666666
# //                Floor Division              a // b  #o/p : 1
# %                 Modulus                     a % b  #o/p : 2
# **                Exponentiation              a ** b  #o/p : 125








# 2. Comparison ( Relational ) Operators :

# Operator             Name                            Example ( a = 5, b = 3)
# ==                 Equal to                           a == b  #o/p : False
# !=                 Not Equal to                       a != b  #o/p : True
# >                  Greater than                       a > b  #o/p : True
# <                  Less than                          a < b  #o/p : False
# >=  , <=           Greater/Less than or equal to      a >= b , a <= b.








# 3. Assiginment Operators : 

# Operator          Example ( a = 5, b = 3)
# =                 a = b  #o/p : a = 3
# +=                a += b  #o/p : a = 8
# -=                a -= b  #o/p : a = 2
# *=                a *= b  #o/p : a = 15
# /=                a /= b  #o/p : a = 1.666
# %=                a %= b  #o/p : a = 2
# //=               a //= b  #o/p : a = 1
# **=               a **= b  #o/p : a = 25
# &=                a &= b   #o/p : a = 1









# 4. Logical Operators :

#           Operator                                                                       Description  

# NOT  [not (a>2 and a<10) #o/p : False]                Logical NOT : Reverse True if one of the statements is true.
# AND [ a > 2 and a < 5  #o/p : False]                  Logical AND : Returns True if both statements are true.                     
# OR  [ a > b or a < 10 #o/p : True]                    Logical OR : Returns True if one statement are true.           









# 5. Identity & Membership Operators : 
# ----> Identity Operators are used to compare the memory locations of two objects , not just eqaul but if they are the same objects.

# ---> Membership operators checks whether a given value is a member of a sequence( such as strings,lists and tuples) or not.




#  :: Identity : (is) / (is not) :-
#   - Returns True if both variables are the same object and false if both are not the same object.
#   - ex : a is b. / a is not b.




#Example : Identity

x = [1,2,3]
y = x 
z = [1,2,3]

# print(x is y) output: True
# print(x is not y) output: False
# print(x is z) #output: False
# print(x is not z) output: True

# :STRING :-

short_name = "anu"
full_name = "anu"
print(short_name is full_name)  # output : True


# :LIST :-

list_1 = [1,2,3]
list_2 = [1,2,3]

print(list_1 is list_2)   # output : False


# :TUPLE :-

tup_1 = (1,2,3)
tup_2 = (1,2,3)

print(tup_1 is tup_2)  # output : True

# : dictionary :-

mydict_1 = {"name" : 'anubhav', 'age' : 20}
mydict_2 = {"name" : 'anubhav', 'age' : 20}

print(mydict_1 is mydict_2)   # output : False












#  :: Membership : (in) / (not in) :-
#   - Returns True if a sequence with the specified value is present in the object and false if the specified value is not present in the object.
#   - ex : a in b / a not in b.


#Example : Membership - in , not in

# my_list = ['apple' , 'orange','watermelon']
# print('apple' in my_list) #output: True
# print('grapes' in my_list) #output: False
# print('apple' not in my_list) #output: False











# 6. BitWise Operators : 

# :: AND (&) : 
# - sets each bit to 1 if both bits are 1.
# - ex : a & b.

# :: OR (|) :
# - sets each bit to 1 if one of the two bits is 1.
# - ex : a | b.

# :: NOT (~) :
# - invert all the bits.
# - ex : ~a.
 
# :: Zero fill left shift (<<):
# - shift left by pushing zeroes in from the right and let the leftmost bits fall off.
# - ex : a << 2.

# :: Zero right shift (>>) :
# - shift right by pushing copies of the leftmost bit in from left , and the rightmost bits fall off.
# - ex: a >> 2.




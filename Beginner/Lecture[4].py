
                        # TOPIC : Type Casting in Python



# Type Casting : it is uses to convert a value from one data type to another.

# - int() : converts a value to an integer.
# - float() : converts a value to a floating-point.
# - str() : converts a value to a String.
# - list() , tuple() , set() , dict() and bool() .


a = 1  # type : int
print(type(a))

b = "1"  # type : str
# print(a+b)  # output: TypeError: unsupported operand type(s) for +: 'int' and 'str'

print( a + int(b) )  #output : 2

# ALL NUMERICAL TYPE CAN BE CAST INTO STR.

age = 20
name = "anubhav"

total = name + str(age)
print(total)  # output : anubhav20


a = 22.75
print(int(a))  # output : 22

b = 22
print(float(b))  # output : 22.0




# Implicit typecasting :- [coercion]
# - automatic done by python interepreter for Data loss or errors.

var1 = 10 # type : int
var2 = 15.5 # type : float
print(var1 + var2)  # output : 25.5 [float]


# explicit typecasting :

int_num = 101
str_num = str(int_num)

a0 = bool(0)
print(a0) #output : False
print(type(a0))

a1 = bool(1)
print(a1) #output : True
print(type(a1))
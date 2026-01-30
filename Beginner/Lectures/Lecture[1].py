                  
                        #   TOPIC : Variables in Python Programming.






a = "Anubhav"
print(a);



# VARIABLE IN PYTHON :-

# Syntax : variable_name = value
#          greeting = "Hello World"
#          print(greeting)  # Output: Hello World

a = 1     # integer number
print(a)
# Output: 1

b = 1.1357101   #decimal number
print(b)
# Output: 1.1357101

c = "Anubhav"   # word / sentence - use quotes
print(c)
# Output: Anubhav


d = anubhav
print(d)
# output :   d = anubhav
#         ^^^^^^^
# NameError: name 'anubhav' is not defined

anubhav = 14   #declare a variable using variable
d = anubhav
print(d)

x = 10  #adding a number to a variable
print(x+1)
# output : 11

p,q,r = 11,12,13  #assign multiple variables
print(p,q,r)
# output : 11 12 13 


# :: Ways to declare a variable name :
MyName = "Anubhav"  # Pascal case.
myName = "Anubhav"  # Camel case.
myname = "Anubhav"  # flat case.
my_name = "Anubhav" # snake case.


# :: NOTE : 
# Python primarily uses snake_case for variables, functions, methods, and module names, as recommended by PEP 8. For class names, Python uses PascalCase (or CapWords), and for constants, it uses screaming_snake_case (all uppercase with underscores). This convention improves readability and distinguishes between different types of identifiers.


# :: Basic rule to declare variable :-


# 1. variable name must start with : letter or _ .
# ex : 
my_name = "Anubhav"
_my_name = "Anubhav"

print(_my_name)

# 2. variable name can contain : letter , numerical value(numbers) , underscore (_).
# ex:
my_name = "Anubhav"
my_name123 = "Anubhav"
my_name_123 = "Anubhav"


# 3. variable are case sensetive.
# ex:
myname = "AnubhavPathak"
print(myName)

# output : error


# 4. variables name cant be a reserved word.
# ex:
for = 20 #-> not valid



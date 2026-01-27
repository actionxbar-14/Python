                         # TOPIC :  Variables in Python







# my_name = "Anubhav"
# print(type(my_name))  #output : <class 'str'>

# value = 100
# print(type(value))    #output : <class 'int'>


# BASIC DATA TYPE IN PYTHON :- 6

# 1. Numeric : int , float , complex
# 2. Sequence : String , List , Tuple
# 3. Mapping : Dictionary
# 4. Set : Set
# 5. Boolean : bool
# 6. Binary : Bytes , Bytearray , Memory.


# 1. Numeric : int , float , complex.

# ex :
a = 1
b = 1
print(a+b)  #output : 2 [int]
print(type(a+b))  #output : class<'int'>


c = 2.50
d = 3.40

print(c+d)  #output = 5.9 [float]
print(type(c+d)) #output = <class 'float'>

e = 3
f = 5
g = complex(3,5)  # 3+5j
print(g)  # output : (3+5j)
print(type(g))  #  <class 'complex'>


# 2. Sequence : String , List , Tuple.


# - STRING: " "

b1 = "Anubhav"
print(b1)  # output = Anubhav
print(type(b1)) # output = <class 'str'> 


# - LIST: []

b2 = [1 , True , "Anubhav"]
print(b2)  # output : [1, True, 'Anubhav']
print(type(b2)) # output : <class 'list'>

# - TUPLE : ( )

b3 = (1, True , "Anubhav")
print(b3) # output : (1, True, 'Anubhav')
print(type(b3))  # output : <class 'tuple'>  


#  3. Mapping : Dictionary - > {key , value} pair.
#  - Dictionary : {key : value }

my_dict = { 'name' : "Anubhav" , 'age' : 20 , 'city' : 'Rajpura'}
print(my_dict)  # output : {'name': 'Anubhav', 'age': 20, 'city': 'Rajpura'}
print(type(my_dict)) # output : <class 'dict'>


# 4. Set : Set
# - Set : {value1 , value2 , value3}

my_sets = {1,2,'anubhav'}
print(my_sets)  # output : {1, 2, 'anubhav'}
print(type(my_sets)) # output : <class 'set'>



# 5. Boolean : bool

bol_1 = True
bol_2 = False
print(bol_1)  # output : True
print(bol_2)  # output : False
print(type(bol_1)) # output : <class 'bool'>
print(type(bol_2)) # output : <class 'bool'>


# 6. Binary : Bytes , Bytearray , Memory.

byte_1 = b"anubhav"
byte_2 = bytearray(b"anubhav")
memory_1 = memoryview(b"anubhav")
print(byte_1)  # output : b'Anubhav'
print(byte_2)  # output : bytearray(b'Anubhav')
print(memory_1)  # output : memoryview(b'Anubhav')
print(type(byte_1)) # output : <class 'bytes'>
print(type(byte_2)) # output : <class 'bytearray'>
print(type(memory_1)) # output : <class 'memoryview'>

                                          # TOPIC : Dictionary in Python



# :: Dictionary in Python  :

# - A dictionary is a data structure in python that stores data in key-value pairs. Dictionary items ( key - value pair ) are ordered , changeable , and do not allow duplicates.

# Key : Must be unique and Immutable ( strings , numbers or tuples ).
# Value : Can be any data type and does not need to be unique.                                                                  


# : Example : Simple dictionary with three key-value pairs.

# student = {
#     "name" : "Anubhav",
#      age : 21,
#      "Section" : "y"
# }










# _____________________________________________________________________________________



# ::Create Dictionary in Python  :




# METHOD 1 : We Create a dictionary using curly braces{} and separating keys and values with a colon.


# : Syntax :

# my_dict = { "key1" : "value1" , "key2" : "value2" , .....}



# : Empty dictionary : 

# empty_dict = {}



# : Dictionary with data : 

# cohort = {
#     "course"  : "Python",
#     "instructor" : "Rishabh Mishra" ,
#     "Level" : "Beginner"
# }









# METHOD 2 : Using dict() constructor 

# - Pass key-Value pairs as keyword arguments to dict().


# Example:

# person = dict(name = "Anubhav" , age = 20, Section = "Y")
# print(person) 









# METHOD 3 : Using a List Of Tuples 

# - Pass a list of tuples , where each tuple contains a key-value pair.

# student = dict([ ("name", "Anubhav") , ("age", 20), ("grade" , "A") ])
# print(student)








# _____________________________________________________________________________________





# :: Access Dictionary Values : 

# - Access dictonary value by using the key name inside square brackets.

# Example : 

# student = {
#     1 : "Class-X" , 
#     "name" : "Madhav" , 
#     "age" : 20
# }



# ---> print value based on respective key-names.

# print(student["name"])   # Output : Madhav
# print(student["age"])    # Output : 20










# _____________________________________________________________________________________






# :: Dictionary Methods :

# - Python provides several built-in methods to use on dictionary.




#          METHODS                                                       DESCRIPTION




# 1.    values()                                              - Returns a list of all values in the dictionary
# 2.   fromkeys()                                             - Returns a dictionary with specified keys and value
# 3.   get()                                                  - Returns value of the specified key
# 4.   items()                                                - Returns a list containing tuple for each key value pair
# 5.   keys()                                                 - Returns a list containing the dictionary's keys
# 6.   update()                                               - updates the dictionary with the specified key-value pairs.
# 7.   pop()                                                  - Removes the element with the specified key
# 8.   popitem()                                              - Removes the last inserted key-value pair
# 9.   clear()                                                - Removes all the elements from the dictionary
# 10.  copy()                                                 - Returns a copy of the dictionary




# :--> Here are a few usefull methods : 

# 1. .keys() : Returns all keys in the dictionary.
# 2. .values()  : Returns all values in the dictionary.
# 3. .items()  :  Returns all key-value pairs.
# 4.  .get()   :  Returns value for a key ( with an optional default if key is missing ).



# :---->  Examples :

# print(student.keys())
# print(student.values())
# print(studen.items())


# print(student.get("name")) --->  # safe way to access a value. { agar name nahi milega toh ham default value bhi de skte hai , or output mai error ki jagah vo default value ayega }.


# student = {
#     1 : "Class-X" , 
#     "name" : "Madhav" , 
#     "age" : 20
# }


# print(student.get("class" , "nahi hai"))   # Output : nahi hai







# _____________________________________________________________________________________





# :: Dictionary - Add , modify and Remove Items : 



# 1. Add or Modify Item : Use assign-operator '=' to add/modify items in a dictionary.


# Adding a new key-value pair
# student["email"] = "madhav@gmail.com"


# #Modifying an existing value
# student["age"] = 25








# 2. Remove Item  : Use del or .pop()  to remove items from a dictionary.


# Remove with del
# del student["age"]


# # Remove with pop() and store the removed value

# email = student.pop("email")
# print(email)    # Output : madhav@example.com









# _____________________________________________________________________________________


# :: Dictionary Iterations : 

# - A dictionary can be iterated using for loop . we can loop through dictionaries by keys,values or both.



# # : Loop through keys :

# for key in student :
#     print(key)


# # : Loop through values :

# for value in student:
#     print(student[value])


# # : Loop through values : using values() method :

#  for values in student.values():
#     print(value)


# # : Loop Through both keys and Values : 

#  for key , value in student.items() :
#     print(key , value)








# _____________________________________________________________________________________





# ::  Nested Dictionary : 

# - Dictionary can contain other dictionaries , which is usefull for storing more complex data.

# nested dictinaries

# student = {
#     "student1" : {
#         "name"  : "madhav",
#         "age"  : 20,
#         "grade" : "A"
#     },
#     "student2"  :  {
#         "name"  : "Keshav" , 
#         "age"  : 21 , 
#         "grade"  : "B"

#     }
# }


# print(students["student1"]["name"])   # output : Madhav





# _____________________________________________________________________________________





# :: Dictionary Comprehensions : 

# - A dictinary Comprehensions allows you to create dictinaries in a concise way.


# Syntax : 

# new_dict =  

# {key_expression : value_expression for item in iterable if condition }



# Example : Creating a dictionary with square numbers

# squares =  { x : x*x for x in range(1,6)}
# print(squares)

# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}





# _____________________________________________________________________________________



# :: Dictionary Common Use Cases : 


# 1. User Profiles in Web Applications  : Store user details like name , email etc.

# 2. Product Inventory Management : keep track of stock levels for Products in an e-commerece system.

# 3. API Responses : Parse JSON data returned from APIs (e.g ., weather data ).

# 4. Grouping Data : organize data into categories .

# Example :

# grouped = {
#     "fruits": ["apple", "bannana"],
#     "veggies"  :["carrot"]
# }


# 5. Caching : Store computed result to reuse and imporve performance.

# Example : 

# cache = { "factorail_5" : 120}


# 6. Switch / Lookup Tables :  Simulate Switch - case for decision-making.

# Example : 

# actions = {
#     "start" : start_fn,
#     "stop" : stop_fn
# }

# actions["start"]()
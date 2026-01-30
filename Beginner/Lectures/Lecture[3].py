
                      # TOPIC  :  Assignment - 1  
 

# :: NOTE : 


print("hello world")
print('hello world')
print("you're a good man")
# print(" you're a "good" person") #output : SyntaxError: invalid syntax. #Perhaps you forgot a comma? 
print('''You're a "good" person''') #output : You're a "good" person





# Question 1: Write a python program that prints the following text exactly as it appears : 
# [  Python is fun.
# "Quotes" and 'single quotes' can be tricky. ]


# Answer 1:

print("[  Python is fun.\n\"Quotes\" and 'single quotes' can be tricky. ]")

print('''Python is fun.
"Quotes" and 'single quotes' can be tricky.''') 







# Question 2: For a bussiness create 3 variables to store - name , age and city.Then print a sentence that uses these variables.

# Answer 2:

name  = "Anubhav"
age = 20
city = "Rajpura"

print(name , "is" , age ,"years old and he lives in" , city) # output :Anubhav is 20 years old and he lives in Rajpura

print(f"my name is {name} from {city} and i am {age} years old")
# :: Function :- a Function is a block of code that perform a specific task.
# benifits of using Function : Increase code Readability & Reusability.

#Basic Concepts :

# > Create Function : use the 'def' keyword to define a function.
# > Call Function : use the function's name followed by ( ) to run it.
# > Parameter : The variable listed inside parentheses in function definition.
# > Argument : The actual value pass to function when you call it.


# Type of Function :-

# 1. Built - in library function :

# - These are the functions that are already available in python.
# ex: print() , input() , type() , sum() , max() etc.

# 2. User-defined function ( Custom ):
# - We can create our own functions based on our requirement.
# ex : create your own function.

# Syntax : def my_function(parameter):
        #      instruction-1
        #      instruction-2

        #  return result


# FUNCTION WITHOUT PARAMETERS :



#Create or Define Function-
# def greetings():
#     print("Welcome to python tutorial by rishabh")

# Use or call this Function-
# greetings()

#output : Welcome to python tutorial by rishabh.


# ex:

# def namaste_karo():
#     name = input("Enter you subh_name :")
#     print(f"ye function {name} ko tahe-dil se namaste krta hai")

# namaste_karo()



# FUNCTION WITH PARAMETERS :

# a = int(input("Enter value of a:"))
# b = int(input("Enter value of b:"))

# def Sum_numbers():
   
#     return a+b

# Sum = Sum_numbers()
# print(f"Sum of {a}+{b} is = {Sum}")


# function to adds two numbers & return result
# def Sum_numbers(a=2,b=4):  
    # return a+b  # after return statement the function stops.

# calling this function with arguments and storing the result in the variable sum
# Sum = Sum_numbers() #output: parameter value(a=2,b=4) total : 6.
# Sum = Sum_numbers(4,4) #output : parameter value(a=4,b=4) total : 8.
# print(f"Sum is = {Sum}")


# list = [1,8,4,2,7,6]
# def Finding_greatest_number(list):
#     return max(list)

# largest_num  = Finding_greatest_number(list)

# print(largest_num)


#Function to Convert Celsius to Fahrenheit: [ Fahrenheit = ( celsius * 9/5 ) + 32 ]

# def celsius_to_fahrenheit(celsius):
#     Fahrenheit = (celsius*9/5)+32
#     return Fahrenheit

# temp_f = celsius_to_fahrenheit(29)
# print(temp_f)

#NOTE : with return statement function ka type float/int ayega,
        # without return statement function ka type none ayega.



# ::PASS statement :-
# - The pass statement is a placeholder in a function or loop. it does nothing and is used when you need to write code that will be added later or to define an empty function

# ex:

# def my_function():
#     pass   #This does nothing for now.
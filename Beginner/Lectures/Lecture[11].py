                      
                        # TOPIC :  Basic Calculator





print("Python Mini Calculator :")


# step : 1 create function for Calculator
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

def avg(a,b):
    return (a+b)/2

# step : 2 User input
print("""enter the operation you want to perform:
          1.Additon
          2. Subtraction
          3. Division
          4. Multiplication
          5. Average
          """)

Select = int(input("select a opeartion:"))

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))

if Select == 1:
    print(f"The sum of {a} + {b} is = ",add(a,b))

elif Select == 2:
    print(f"The Subtraction of {a} - {b} is = ",subtract(a,b))

elif Select == 3:
    print(f"The division of {a} / {b} is = ",divide(a,b))

elif Select == 4:
    print(f"The Mulitplication of {a} * {b} is = ",multiply(a,b))

elif Select == 5:
    print(f"The avg of ({a} + {b})/2 is = ",avg(a,b))

else:
    print("Invalid input"0)











# a = int(input("Enter the Value of a:"))
# b = int(input("Enter the Value of b:"))

# operator = input("Enter the Operation of + , - , % ,*,avg:")

# if operator == '+':
#     print(f"you want to perform {operator} operation :")
#     print(f"The {a}+{b} is = {a+b}")

# elif operator == '-':
#     print(f"you want to perform {operator} operation :")
#     print(f"The {a}-{b} is = {a-b}")

# elif operator == '/':
#     print(f"you want to perform {operator} operation :")
#     print(f"The {a}/{b} is = {a/b}")

# elif operator == 'avg':
#     print(f"you want to perform {operator} operation :")
#     print(f"The avg of {a} and {b} is = {(a+b)/2}")
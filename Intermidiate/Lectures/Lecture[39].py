
# :: Youtube Playlist Content : 

# --> lecture-196 : OOPS-6.
# --> lecture-197 : OOPS-7. 
# --> lecture-198 : OOPS-8. 
# --> lecture-199 : OOPS-9. 
# --> lecture-200 : OOPS-10. 


# ___________________________________________________________________________________________________________________________________
# 



# :: Accessing Class Members Outside the Class :

# - Class members :- Attributes (variables) + Actions (Methods). 
# - We can access these variables using object outside the class. 

# - Syntax :

# Accessing attribute :- object_name.variable_name
# Accessing method :-  Object_name.method_name()


# - Ex : 

# class Employee:
#     def __init__(self , salery , age):
#         self.salary = salery 
#         self.age = age 

#     def display(self):
#         print(f"salery is :  {self.salary} and age is : {self.age}")


# e1 = Employee(24000 , 21)
# e2 = Employee(26000 , 26)


# print(e1.salary)  # output : 24000

# e1.display() # output :-  salery is :  24000 and age is : 21

# e2.salary # output : 26000

# e2.display()  # output :-  salery is :  26000 and age is : 26


# :--> re-assigning the value of salery :

# e1.salary =  250000

# print(e1.salary)  # output : 250000





# ___________________________________________________________________________________________________________________________________



# ::  Built-in Class Function :


# 1.) getattr(object_name , attribute_name)

# 2.) setattr(object_name , attribute_name , new_value)

# 3.) delattr(object_name , attribute_name) 

# 4.) hasattr(object_name , attribute_name) 






# 1.) getattr(object_name , attribute_name) : 

# - Ex : 

# class Employee:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age 

         
# e1 = Employee('raj' , 21)
# e2 = Employee('jay' , 22)

# print(getattr(e1 , 'age'))  # output : 21

# print(getattr(e1 , 'name')) # output : raj













# 2.)  setattr(object_name , attribute_name , new_value) :

# - Ex : 

# class Employee:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age 

         
# e1 = Employee('raj' , 21)
# e2 = Employee('jay' , 22)

# print(e1.name)  # output : raj

# setattr(e1 , 'name' , 'rajkumar')

# print(e1.name)  # output : rajkumar















# 3.) delattr(object_name , attribute_name)  : 


# - Ex :

# class Employee:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age 

         
# e1 = Employee('raj' , 21)
# e2 = Employee('jay' , 22)



# print(e1.__dict__)  # output :  {'name': 'raj', 'age': 21}


# delattr(e1,'age')


# print(e1.__dict__)   # output :  {'name': 'raj'}









# 4.) hasattr(object_name , attribute_name)  : 

# - Ex : 

# class Employee:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age 

         
# e1 = Employee('raj' , 21)
# e2 = Employee('jay' , 22)


# print(hasattr(e1 , 'age'))  # output : True

# print(hasattr(e1 , 'nm'))  # output : False




# ___________________________________________________________________________________________________________________________________



# :: built-in Class attributes : 


# 1.)  __dict__   :-  Dictionary containing class's namespace. 

# 2.) __doc__     :-  Class documentation string. 

# 3.) __name__    :-  Class Name.

# 4.) __module__  :-  Module name in which class is defined or imported. 

# 5.) __bases__   :-  List of bases classes. 





# - Ex :  


# class Employee:
#     '''This is employee class for maintaining employee data''' 

#     def __init__(self , name , age):
#         self.name = name 
#         self.age  = age 

#     def display(self):
#         print(f"name is : {self.name} and age is  {self.age}")


# e1 = Employee('jay' , 21)
# e2 = Employee('raj' , 22)



# __dict__ :
 
# print(Employee.__dict__)  # output :  {'__module__': '__main__', '__firstlineno__': 220, '__doc__': 'This is employee class for maintaining employee data', '__init__': <function Employee.__init__ at 0x000002062B5D3690>, 'display': <function Employee.display at 0x000002062B5D37F0>, '__static_attributes__': ('age', 'name'), '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>}

# __doc__ :

# print(Employee.__doc__)  # output : This is employee class for maintaining employee data


# # __name__ :

# print(Employee.__name__)  # output : Employee


# # __module__ :

# print(Employee.__module__)  # output : __main__







# ___________________________________________________________________________________________________________________________________



# :: isinstance() function : 
# - It takes two argument in which first is object_name and second is class_name and it tells wheather the particular object is belong to the respective class or not. 
# - It returns True if particular object is belong to the respective class otherwise return False. 

# - Ex : 

# class Demo():
#     pass

# d1 = Demo()






# class Employee:
#     '''This is employee class for maintaining employee data''' 

#     def __init__(self , name , age):
#         self.name = name 
#         self.age  = age 

#     def display(self):
#         print(f"name is : {self.name} and age is  {self.age}")


# e1 = Employee('jay' , 21)
# e2 = Employee('raj' , 22)



# print(isinstance(e1 ,  Employee)) # output  : True
# print(isinstance(d1 , Employee))  # output  : False




# ___________________________________________________________________________________________________________________________________




# :: Instance Variables & Instance methods :

# - In OOPs there is two types of variables :- 

# 1.) Instance variables . 
# 2.) Class variables. 





# 1.) Instance variables :-
# - variables made for particular instance. 
# - Separate copy is created for every object. 
# - Values of variables differs from object to object. 
# - modification in one object won't effect other objects. 
# - we can create instance variable using __init__ method or also we can create it outside the class. 
# - we can also use instance method for creating the instance variable. 



# - Ex :


# class Student:
#     def __init__(self , name , marks):
#         self.name = name 
#         self.marks = marks   # --> Instance variable using __init__ method

#     def display(self):      
#         print(self.name , self.marks)


#     def change_data(self):
#         self.name =  input("Enter name :")
#         self.marks = input("Enter marks :")

      

# std1 = Student('Akshay' , 89)
# std2 = Student('Raj' , 89) 
# std3 = Student('jay' , 89) 

# # -->instance variable outside the class
# std1.age = 21 

# print(std1.__dict__) # output : {'name': 'Akshay', 'marks': 89, 'age': 21}
# print(std2.__dict__) # output : {'name': 'Akshay', 'marks': 89}

# std2.change_data()


# print(std2.__dict__)  # output :   {'name': 'abc', 'marks': 100}










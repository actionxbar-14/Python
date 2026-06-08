

# :: Youtube Playlist Content : 

# --> lecture-191 : OOPS-1.
# --> lecture-192 : OOPS-2. 
# --> lecture-193 : OOPS-3. 
# --> lecture-194 : OOPS-4. 
# --> lecture-195 : OOPS-5. 


# ________________________________________________________________________________________________________________________________________________________________________
# 

# :: OOPS in Python :   [ Object Oriented Programming ]

# --> Programming Paradigms : 
# - Ways of Organizing programs. 
# - Python supports basically three types of paradigms : 

# 1. Procedural oriented paradigm.   
# 2. Functional oriented paradigm. 
# 3. Object-oriented paradigm. 






# :--> Object : 
# - An object in OOP represents real-life objects.
# - Ex : Email , man , student , employee 

# - Every object has two properties :

# 1.). Attributes :
# -> heading , subject  , name , recipients list.      


# 2.)  Behaviours :
# -> sending , adding , attachments. 







# :--> What is Object-Oriented programming ( OOP ) :
# - Object-oriented programming is an approach of writiing programs by creating classess and objects. 
# - More focus is on data rather tha +nan logib. 




# :--> Why OOP ? 

# 1.) To Solve real-world problems effictively. 
# 2.) OOP provides some features :-
# -> Inheritance is used for reusability.
# -> encapsultaion is used for data security. 
# -> adstraction is used for data hiding. 





# ________________________________________________________________________________________________________________________________________________________________________

# :: Classes & Objects :


# :--> What is a Class : 

# - Class is a template / blueprint / prototype for creating objects. 
# - Every Object belong to some class. 
# - Class is an collection of attributes and methods. 
# - class is an collection of objects. 
# - Technically , class is an user-defined datatype. 




# - Ex : 

# x = 100
# print(type(x)) # output  : <class 'int'>





# - Ex :  if Email is an class then , email1 + email2  are objects. 

# NOTE : an email consists of the two things , attributes and methods : 

# # i) --> attributes :- ( class_1 )
#       heading
#       participants
#       attachments 
  

# #  ii) -->  methods :-  ( class_1 )
#       send()
#       save_as_draft()



# :--> Email_1 :  ( object_1 )
    #   heading :- taking leave 
    #   participant :- xyz
    #   attachments :- form.pdf




# :--> Email_2 :  ( object_2 )
    #   heading :- require help
    #   participant :- abc
    #   attachments :- pic.jpg






# :--> Creating Class and Objects :


# - Syntax : 

# class Class_name:
    #attributes
    #methods 


# obj1 = Class_name([args]) 
# obj2 = Class_name([args])



# - Ex : 

# class Email:
#     pass 



# e1 = Email()
# e2 = Email()


# print(type(e1))  # output : <class '__main__.Email'>



# - Ex :  ( implementing example )



# class Employee:
#     def __init__(self , name , age):
#         self.name = name 
#         self.age  = age 

#     def display(self):
#         print(self.name)




# e1 = Employee('raj' , 21)
# e2 = Employee('jay' , 22)






# class Employee:
#     def employee_details(self , name  , age , emp_id):
#         self.name = name
#         self.age = age 
#         self.emp_id = emp_id 

#     def display(self):
#         print("name of employee is :" , self.name)
#         print("age of employee is :" , self.age)
#         print("emp_id of employee is :" , self.emp_id)



# emp1 = Employee("anubhav" , 22 , 101)
# emp2 = Employee("div" , 23 , 102)







# ________________________________________________________________________________________________________________________________________________________________________




# ::  Constructor & types of Constructor : 

# - It is a type of Special method used for initializing objects with attributes. 
# - __init__() method is a constructor in Python Programming. 
# - first argument of __init__() method is 'self'. 
# - It is optional but without constructor object cannot be created , so when no constructor is created then default constructor(built-in) is passed. 


# - Ex : 

# class Employee:
#     def __init__(self):
#         self.salary = 22000
#         self.age = 21 


# e1 = Employee()
# e2 = Employee()

# print(e1.__dict__)





# :--> Types of Constructor : 

# 1.) Non-Parameterized Constructor.
# 2.) Parameterized Constructor. 
# 3.) Default Constructor. 




# 1.) Non-Parameterized Constructor : 
# - No other parameter passed only self is passed through the constructor. 
# - Ex :


# class Employee:
#     def __init__(self):  #--> Non-Parameterized Constructor 
#         self.salary = 22000
#         self.age = 21 


# e1 = Employee()
# e2 = Employee()

# print(e1.__dict__)





# 2.) Parameterized Constructor : 
# - Other parameter including self is passed through the constructor. 
# - Ex : 

# class Employee:
#     def __init__(self , salery , age):  #--> arameterized Constructor 
#         self.salary = salery
#         self.age = age


# e1 = Employee(22000, 21)
# e2 = Employee(25000, 24)

# print(e1.__dict__)
# print(e2.__dict__)




# ________________________________________________________________________________________________________________________________________________________________________








# :: Working of OOP & self variable :

# :--> Steps: 
# -> In OOP Programming , Firstly memory allocation for object happens ,
# -> Memory refrence returned to the object. 
# -> memory refrence automatically passed inside constructor. 
# -> Constructor creates / initialize variables at that memory refrence. 


# :--> Self :
# - it is just a variable that contains the memory address of current object.  


# - Ex : 


# class Employee:
#     def __init__(self , salery , age):  #--> arameterized Constructor 
#         self.salary = salery
#         self.age = age


# e1 = Employee(22000, 21)
# e2 = Employee(25000, 24)

# print(e1.__dict__)
# print(e2.__dict__)






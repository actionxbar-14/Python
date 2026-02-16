 
                                    # TOPIC : OOPS in Python

# :: There are mainly two ways of programming in Python : 

# 1. Procedural Programming.
# 2. OOPs 



# :- OOPs : Object Oriented Programming : 

# A way of organizing code by creating "blueprints" ( called classes ) to represent real - world things like student , car or house. These blueprints help you create objects ( individual examples of those things ) and define their behavior.



# :- Class : 
# - A Class is a blueprint or template for creating objects. 
# - It defines the properties (attributes) and actions/behavior (methods) that objects of this type will have.


# :- Object : 
# - An Object is a specific instance of a class.
# - It has actual data based on the blueprint defined by the class.



# ____________________________________________________________________________________________


# :: Why OOPs : 

# Ex: Creating student Records - lists.

# student_1 = ['madhav' , 10]
# student_2 = ['vishakha', 12]
# student_3 = 'keshav'


# student_1.append('A')
# print(student_1)


# print(f"{student_1[0]} is in class {student_1[1]}")








# :BENIFITS OF OOPS PROGRAMMING : 

# 1. Models Real - world Problems : 
# - Mimics real - world entities for easier understanding.


# 2. Code Reusability : 
# - Encourages reusable , modular and organized code.


# 3. Easier Maintenance : 
# - OOP Organizes code into small , managable parts ( classes and objects ). Changes in one part don't impact others , making it easier to maintain.


# 4. Encapsulation : 
# - Encapsulation protects data integrity and privacy by bundling data and methods into an class.

# 5. Flexibility and Scalability : 
# - OOP makes it easier to add new features without affecting existing code.


# ____________________________________________________________________________________________


# :: Using OOps Concepts to Create student records.


# Class - blueprint or template :

# class Student:
#     pass


# # object - instance of class :

# student1 = Student()
# print(student1)  # Output : <__main__.Student object at 0x000001B433EEF810>  





# Ex:1

# class Student :
#     name = "Anubhav"
#     age = 21


# student1 = Student()
# print(student1.name,student1.age)   # Output : Anubhav 21


# student2 = Student()
# print(student2.name,student2.age)   # Output : Anubhav 21







# -----> har time same name or age print ho rha hai isliiye ham is problem ko solve krne ke liye classes mai methods ko banate hai.
#NOTE : classes mai function ko hi method bolte hai.







#----> #  __init__ method - constructor , value initialized : fixed.
#----> #  refrence or connection build between class and object : fixed

# class Student :

# #----> # __init__  Method
#     def __init__(self , full_name , Curr_age, percentage,team):  
#         self.name = full_name   #--> attribute (variable)
#         self.age =  Curr_age    #--> attribute (variable)
#         self.percentage =  percentage    #--> attribute (variable)
#         self.team = team

# #----> # Custom Method  
#     def student_details(self):
#         print(f"{self.name} is {self.age} years old have {self.percentage} % and is in team {self.team}")



# team1 = 'A'
# team2 = 'B'
# #----> # Creating Objects
# student1 = Student("Anubhav" , 21, 99,team1)    


# print(student1.name , student1.age)   # Output : Anubhav 21
# student1.student_details()     # Output : Anubhav is 21 years old have 99 % and is in team A

# print(student1.__dict__)     # Output :    {'name': 'Anubhav', 'age': 21, 'percentage': 99, 'team': 'A'} 

# #---> Modify object property
# student1.percentage = 95
# student1.student_details()   # Output : Anubhav is 21 years old have 95 % 


# #----> delete object property
# # del student1.percentage
# # print(student1.__dict__)    # Output : {'name': 'Anubhav', 'age': 21} 



# #----> delete object itself 
# del student1
# print(student1)   # Output :   NameError: name 'student1' is not defined. Did you mean: 'Student'? 
   
       










#----> # Creating Objects
# student2 = Student("Neha" , 21, 90,team2)
# print(student2.name , student2.age)   # Output :  Neha 21
# student2.student_details()     # Output :   Neha is 21 years old have 90 %  and is in team B

# print(student2.__dict__)       # Output : {'name': 'Neha', 'age': 21, 'percentage': 90, 'team': 'B'}


# #---> Modify object property
# student2.percentage = 99
# student2.student_details()   # Output : Neha is 21 years old have 99 % 




#----> delete object property
# del student2.percentage
# print(student2.__dict__)    # Output : {'name': 'Neha', 'age': 21} 



# #----> delete object itself 
# del student2
# print(student2)   # Output :  NameError: name 'student1' is not defined. Did you mean: 'Student'?



# :----> Self parameter :  the self parameter is the refrence to the current instance of the class and is use to access variables that belong to the class. (class and object ke beech mai relation create krta hai)

# __________________________________________________________________________________________________________________




# :: 4 - features in OOPs :

# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism








# 1. Abstraction  : 
# - Hiding unnecessary details from users through class , methods.



# Ex:


# class Student:

#     def __init__(self , name , age ,  grade , percentage):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.percentage = percentage


#     def print_student_details(self):  # methon - abstraction
#         print(f"The name of student is {self.name} is {self.age} years old , got grade {self.grade} and {self.percentage + 1} %")




# # Object - instance of class
# student1 = Student("Anubhav" , 21 , 'A' , 95)
# student1.print_student_details()
# print(student1.__dict__)



# student2 = Student("Neha" , 21 , 'A+' , 97)
# student1.print_student_details()
# print(student2.__dict__)


















# 2. Encapsulation : Restrict access to certain attributes or methods to protect data and enforce controlled access.


# Ex:




# class Student:

#     def __init__(self , name , age ,  grade , percentage):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.__percentage = percentage   #---> Double underscore limit access ( private variable )


    
#     def get_percentage(self):

#         return self.__percentage



#     def print_student_details(self):  # methon - abstraction
#         print(f"The name of student is {self.name} is {self.age} years old , got grade {self.grade} and {self.percentage} %")

    



# Object - instance of class
# student1 = Student("Anubhav" , 21 , 'A' , 95)
# student1.print_student_details()
# print(student1.__dict__)



# print(student1.percentage)   # Output : AttributeError: 'Student' object has no attribute 'percentage'



# print(student1.__percentage)  # Output :  AttributeError: 'Student' object has no attribute 'percentage'
        #   ^^^^^^^^^^^^^^^^^^^     
# AttributeError: 'Student' object has no attribute 'percentage' 

# print(student1.get_percentage())   # Output : 95




# student2 = Student("Neha" , 21 , 'A+' , 97)
# student1.print_student_details()
# print(student2.__dict__)     




# print(student1.percentage)   # Output : AttributeError: 'Student' object has no attribute 'percentage'



# print(student1.__percentage)  # Output :  AttributeError: 'Student' object has no attribute 'percentage'
        #   ^^^^^^^^^^^^^^^^^^^     
# AttributeError: 'Student' object has no attribute 'percentage' 


# print(student2.get_percentage())  # Output : 97





























# 3. Inheritance : 
# - Allow one class ( child ) to reuse the prop and methods of another class ( parent ).




# Ex:


# #-----> this is parent class
# class Student:

#     def __init__(self , name , age ,  grade , percentage):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.percentage = percentage


#     def print_student_details(self):  # methon - abstraction
#         print(f"The name of student is {self.name} is {self.age} years old , got grade {self.grade} and {self.percentage + 1} %")




# # Object - instance of class
# student1 = Student("Anubhav" , 21 , 'A' , 95)
# # student1.print_student_details()
# # print(student1.__dict__)



# student2 = Student("Neha" , 21 , 'A+' , 97)
# # student1.print_student_details()
# # print(student2.__dict__)





# #-----> this is child class

# # Graduatestudent child class inherit prop and methods from Student Parent class
# class GraduateStudent(Student):

#     def __init__(self, name, age, grade, percentage, stream): # here we can take old parameters from parent class and new parameters in child class.
#         self.stream = stream  # new attribute in child class
#         super().__init__(name ,age, grade , percentage,)  #---> Super() calls the parent class init
        
   
#     def student_details(self):
#         super().print_student_details() # method from parent class -- > print(f"stream is {self.stream}")
        
     

# Grad_Student1 = GraduateStudent('keshav', 'A',22,  96, 'PCM')
# # print(Grad_Student1.name)   # Output : keshav
# # print(Grad_Student1.stream) # Output : PCM
# Grad_Student1.student_details() # Output : The name of student is keshav is A years old , got grade 22 and 97 %





















# 4. Polymorphism : 

# - Allow a method of one function use in another class with different or multiple functionality.



# Ex:





#-----> this is parent class
class Student:

    def __init__(self , name , age ,  grade , percentage):
        self.name = name
        self.age = age
        self.grade = grade
        self.percentage = percentage


    def print_student_detail(self):  # methon - abstraction
        print(f"The name of student is {self.name} is {self.age} years old , got grade {self.grade} and {self.percentage + 1} %")




# Object - instance of class
student1 = Student("Anubhav" , 21 , 'A' , 95)
# student1.print_student_details()
# print(student1.__dict__)



student2 = Student("Neha" , 21 , 'A+' , 97)
# student1.print_student_details()
# print(student2.__dict__)





#-----> this is child class

# Graduatestudent child class inherit prop and methods from Student Parent class
class GraduateStudent(Student):

    def __init__(self, name, age, grade, percentage, stream): 
        self.stream = stream  # new attribute in child class
        super().__init__(name ,age, grade , percentage,)  #---> Super() calls the parent class init
        
   
    def print_student_detail(self):   
        # super().print_student_details() # method from parent class -- > print(f"stream is {self.stream}")
        print("this is the method of child class")
        
     

Grad_Student1 = GraduateStudent('keshav', 'A',22,  96, 'PCM')
# print(Grad_Student1.name)   # Output : keshav
# print(Grad_Student1.stream) # Output : PCM
student1.print_student_detail()
Grad_Student1.print_student_detail() 





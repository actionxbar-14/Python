
# :: Youtube Playlist Content : 

# --> lecture-201 : OOPS-11.
# --> lecture-202 : OOPS-12. 
# --> lecture-203 : OOPS-13. 
# --> lecture-204 : OOPS-14. 
# --> lecture-205 : OOPS-15. 


# ________________________________________________________________________________________________________________________________________ 




# :: Class Variable : 

# - These are the variables made for entire class. ( all objects )
# - Only one copy is created and distributed to all objects. 
# - Modification in class variable impact on all objects. 

# - Ex : 


# class Employee:
#     company_name = "infosys"  #--> class variable 

#     def __init__(self , name , age):
#         self.name = name 
#         self.age  = age 

#     def display(self):
#         print(f"name is : {self.name} and age is  {self.age}")


# e1 = Employee('jay' , 21)
# e2 = Employee('raj' , 22)


# print(Employee.company_name)   # output : infosys    ( by class Refrence )
# print(e1.company_name)          # output : infosys   ( by object Refrence )
















# :--> How to modify Class variable : 

# - By using the class refrence. 


# - Ex:  



# class Employee:
#     company_name = "infosys"  #--> class variable 

#     def __init__(self , name , age):
#         self.name = name 
#         self.age  = age 

#     def display(self):
#         print(f"name is : {self.name} and age is  {self.age}")


# e1 = Employee('jay' , 21)
# e2 = Employee('raj' , 22)


# Employee.company_name = 'TCS'
# print(Employee.company_name)  # output : TCS



# # NOTE :  # - object refrence is not used for modification of class variable ,  because when we modify using the object refrence , it creates an instance variable for that particular object. 


# e2.company_name = 'TCS'

# print(e2.__dict__)  # output : {'name': 'raj', 'age': 22, 'company_name': 'TCS'}









# :: Class method :-  

# -> Method which works on class variables. 
# -> First arugment is class refrence. 
# -> Made using built-in decorator '@classmethod'.




# - Ex : 



# class Employee:
#     company_name = "infosys"  #--> class variable 

#     def __init__(self , name , age):
#         self.name = name 
#         self.age  = age 
    
#     @classmethod
#     def get_company_name(cls): #----> this is the class method for accessing the class variable
#         # print(f"Company name is :", cls.company_name)
#         cls.company_name = 'TCS'
#         print(cls.company_name)

# e1 = Employee('jay' , 21)
# e2 = Employee('raj' , 22)

# # Accessing the class variable
# Employee.get_company_name()  # output :-  Company name is : infosys


# # getting the modified variable 

# Employee.get_company_name()  # output : TCS







# ________________________________________________________________________________________________________________________________________ 

# :: Instance methods :

# 1.)  setter method :- set values of instance variables. 
# 2.)  getter method :- get values of instance variables. 



# - Ex : 

# class Employee:

#     def setName(self , nm):    #setter method
#         self.name = nm 

#     def getName(self):         #getter method
#         print("The name is( getter ):" , self.name)

# e1 = Employee()
# e2 = Employee()


# # setting the name using setter method 


# e1.setName(input("Enter the name e1 :"))
# e2.setName(input("Enter the name e2 :"))

# print("e1 object is :" , e1.__dict__)  # output : e1 object is : {'name': 'anu'}
# print("e2 object is :" , e2.__dict__)  # output : e2 object is : {'name': 'dev'}



# # getting the value by getter method : 

# e1.getName()  # output  : The name is( getter ): anu
# e2.getName()  # output  : The name is( getter ): dev








# ________________________________________________________________________________________________________________________________________ 



# :: static methods : 

# - methods which performs operations on external data. 
# - It can also perform operations on class data. 
# - No need to pass object or class refrence. 
# - Created using decorator '@staticmethod'. 


# NOTE : Class variables ko hi static variables bola jata hai. 

# -  Ex : 


# class Bank:
#     bank_name = 'BOI'
#     rate_of_interest = 12.25 

#     @staticmethod 
#     def simple_interest(prin , n):
#         si = (prin * n * Bank.rate_of_interest) / 100 
#         print(si)




# prin = float(input("Enter principle amount :"))
# n = int(input("Enter number of years :"))

# Bank.simple_interest(prin , n)











# ________________________________________________________________________________________________________________________________________ 




# :: Inheritance in Python : 
# - Deriving a new class from an existing class so that new class inherits all members ( attributes + methods ) of existing class is called as inheritance. 

# --> Old class ko hi ham Parent class , Base class , Existing class , Super Class bolte hai. 

# --> New class ko hi ham child class , sub class , derived class bolte hai. 

# --> Object class :- All classes in Python are derived from built-in 'object' class. 


# Creating child class :

# class Parent(object):
#     # attributes + methods 

# class Child(Parent):
      # attributes + methods 




# - Ex :  ( without inheritance )


# class Employee:
#     bonus  = 2000 

#     def display(self):
#         print("This is employee class method")



# class Manager: 
#     bonus1 = 5000 

#     def show(self):
#         print("This is manager class method") 


# e1 = Employee()
# m1 = Manager()

# e1.display()  # Output : This is employee class method
# m1.show()     # Output : This is manager class method


# print(m1.bonus1) # output :  5000




# print(m1.bonus)  # output :     print(m1.bonus)
#           ^^^^^^^^
# AttributeError: 'Manager' object has no attribute 'bonus'. Did you mean: 'bonus1'?








# - Ex : ( Using Inheritance )



# class Employee:
#     bonus  = 2000 

#     def display(self):
#         print("This is employee class method")



# class Manager(Employee):  # --> Manager class inherit the property of Employee class
#     bonus1 = 5000 

#     def show(self):
#         print("This is manager class method") 


# e1 = Employee()
# m1 = Manager()

# e1.display()  # Output : This is employee class method
# m1.show()     # Output : This is manager class method


# print(e1.bonus)  # output :  2000

# print(m1.bonus)   # output : 2000   

# ________________________________________________________________________________________________________________________________________ 





# ::  Why we use inheritance ? 

# -> For Code-reusability( write once use many times ).
# -> When you have relations among classes. 






# - Ex:  ( Bank Management System Without inheritance )


# class Customers:
#     SetPersonalDetails()
#     GetPersonalDetails()
#     SetEducationDetails()
#     GetEducationDetails()
#     SetBankAccount()



# class Employee:
#     SetPersonalDetails()   # --> repetition
#     GetPersonalDetails()   # --> repetition
#     SetEducationDetails()  # --> repetition
#     GetEducationDetails()  # --> repetition
#     SetBankAccount()       # --> repetition
#     SetSalery()
#     SetBonus()






# - Ex :  ( Bank Management System With inheritance )





# class Customers:
#     SetPersonalDetails()
#     GetPersonalDetails()
#     SetEducationDetails()
#     GetEducationDetails()
#     SetBankAccount()



# class Employee(Customers):
#     SetBankAccount()      
#     SetSalery()
#     SetBonus()








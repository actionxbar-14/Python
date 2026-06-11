
# :: Youtube Playlist Content : 

# --> lecture-206 : OOPS-16.
# --> lecture-207 : OOPS-17. 
# --> lecture-208 : OOPS-18. 
# --> lecture-209 : OOPS-19 
# --> lecture-210 : OOPS-20. 


# ___________________________________________________________________________________________________________________________________



# :: Constructor in Inheritance : 

# - By default , Constructor of parent class avialable to child class. 
# - If child class does not have any constructor then , it uses the father class constructor.
# - But if the child and father both class have its own constructor then , child class constructor is called , isiko constructor overriding kahte hai. 

# - Ex : 

# class Father:
#     def __init__(self):
#         print("father constructor called")
#         self.vehicle = 'scooter'

# class Son(Father):
#     pass


# s = Son() 

# print(s.__dict__)  # output :  father constructor called
                              # {'vehicle': 'scooter'}






# - Ex :  



# class Father:
#     def __init__(self):
#         print("father constructor called")
#         self.vehicle = 'scooter'


# class Son(Father):
#     def __init__(self):
#         print("son constructor called")
#         self.vehicle = "BMW"


# s =  Son()

# print(s.__dict__)   # output : son constructor called
                    #          {'vehicle': 'BMW'}









# ___________________________________________________________________________________________________________________________________




# :: super() In Python :  ( Watch video for revision )

# - Using super() function , we can access parent class properties in the child class. 
# - This function returns a temporary object which contains reference to parent class. 
# - It makes inheritance more manageble and extensible. 


# - Ex: 

# class Computer(object):
#     def __init__(self, ram , storage):
#         self.ram = '8gb'
#         self.storage = '512gb'
#         print("Computer class constructor called") 

    
    
# class Mobile(Computer):
#     def __init__(self , ram , storage):
#         super().__init__(ram , storage)   #---> yaha se hamne child class ka constructor hote hue bhi parent class ke constructor ko run karwayaa
#         self.model = 'iphone X'
#         print("Mobile class constructor called")


# Apple = Mobile('8gb' , '512gb')
# print(Apple.__dict__) 
# output :
# Computer class constructor called
# Mobile class constructor called
# {'ram': '8gb', 'storage': '512gb', 'model': 'iphone X'}








# ___________________________________________________________________________________________________________________________________





# ::  Types of Inheritance : 

# 1.) Single Inheritance 
# 2.) Mulit-level Inheritance 
# 3.) Hierarchical Inheritance 
# 4.) Multiple Inheritance 
# 5.) Hybrid Inheritance
# 6.) Cyclic Inheritance 








# 1.) Single Inheritance : 
# - One Parent and One Child class. 
# - hirarchy :  
# object ----> Parent ---->  child

# - Ex : all above example are single inheritance









# 2.) Multi-level Inheritance : 
# - In this , firstly Parent class is inherit from the child class and then child class is inherit another class grand_child , hence creating multiple levels. 
# - hirarchy :  
# object ----> Parent ---->  child --> grand_child

# - Ex : 



# Constructor in multi-level inheritance :  
# --> Manager employee and human_being ke constructor ko access krr skta hai. 

# class Human_being(object):
#     def __init__(self):
#         print("Human being constructor called") 
#         self.name = input("Enter your name :") 


# class Employee(Human_being):
#     def __init__(self):
#         print("Employee constructor called")
#         self.salary = float(input("Enter your salary :"))


# class Manager(Employee):
#     def __init__(self):
#         print("Manager constructor called")
#         self.bonus = float(input("Enter your bonus :"))


# m1 = Manager()


# NOTE :

# --> child are allow to access the property of parent but the parent are not allowed to access the property of child. 



         







# ___________________________________________________________________________________________________________________________________




# 3. Hierarchical Inheritance:  

# - one Parent and multiple child classes. 
# - object is inherited from the Parent and then multiple child are inherit the Parent class. 
# - inherited child are not allow to access the property of each other. 


# - Ex : 


# class Person:    #----> parent class
#     def __init__(self, nm , ag):
#         self.name = nm 
#         self.age = ag 

#     def display(self):
#         print("This is person display method")




# class Employee(Person):   #----> child class
#     def __init__(self ,nm , ag , sal):
#         super().__init__(nm ,ag)
#         self.salary = sal 
    
#     def display1(self):
#         print("This is Employee display method")




# class Student(Person):    #----> child class
#     def __init__(self , nm , ag , m):
#         super().__init__(nm , ag)
#         self.marks = m 
    
#     def display2(self):
#         print("This is Student display method")





# s1 = Student('jay' , 21 , 90)
# e1 = Employee('raj' , 24 , 40000)



# print(s1.__dict__)  # output : {'name': 'jay', 'age': 21, 'marks': 90}

# print(e1.__dict__)  # output :  {'name': 'raj', 'age': 24, 'salary': 40000}




# p1.display1()  # output : attribute-Error ( because parent class cannot access the value of child class )

# s1.display2()  # output : attribute-Error   ( because parent class cannot access the value of child class )










# ___________________________________________________________________________________________________________________________________




# 4.) Multiple inheritance : 
# - Class is derived from multiple base classes. 

# - Heirarchy :  object --> parent-1 , parent-2 ----> child. 

# - Syntax : 

# class Parent1(Object):
    #parent1 class properties 

# class Parent2(Object):
    #parent2 class properties 


# class Child(Parent1 , Parent2):
#     #child class properties





# - Ex :   

# class Country:
#     def __init__(self):
#         self.office = 'Delhi'

   


# class State:
#     def __init__(self):
#         self.office = 'Mumbai'


    

# class District(State , Country):  #--> priority search : State > Country
#     pass 



# d = District() 

# print(d.__dict__)  # output : {'office': 'Mumbai'}

# print(d.office)   # output : Mumbai






# 5.) Hybrid Inheritance : 
# - It contains multiple types of inheritance. 











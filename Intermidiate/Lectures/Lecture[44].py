
# :: Youtube Playlist Content : 

# --> lecture-221 : OOPS-31.
# --> lecture-222 : OOPS-32. 
# --> lecture-223 : OOPS-33. 
# --> lecture-224 : OOPS-34. 
# --> lecture-225 : OOPS-35. 


# _____________________________________________________________________________________________________________________________________ 




# :: Nested class : 
# - The class which is declared inside another class. 

# - Ex : 

# class University:
#     #University class members 
#     class College:
#         #College class members 

    



# :--> Why it is required : 
# - When one class object can't exist without another class object. 



# - Ex : 

# class Outer:
#     def __init__(self):
#         print("Outer class constructor called")

#     def display(self):
#         print("This is display method")

#     class Inner:
#         def __init__(self):
#             print("Inner constructor called")
        
#         def show(self):
#             print("This is show method")


# obj = Outer() 
# inn = obj.Inner() #----> Nested Inner class 


# inn.show()

# obj.display()

# output :  
# Outer class constructor called
# Inner constructor called
# This is show method
# This is display method



# NOTE : Outer class ka object ka use krke ham inner class ke methods ko access nahi krr skte hai.

# - Ex : 

# class Student:
#     def __init__(self , name , roll , dd , mm , yy):
#         self.name = name 
#         self.roll = roll 
#         self.dob = self.DOB(dd , mm , yy)
    
#     def display(self):
#         print(f" name is {self.name} and roll is {self.roll}")
#         self.dob.display()




#     class DOB:
#         def __init__(self , dd , mm , yy):
#             self.date = dd 
#             self.month = mm 
#             self.year = yy 


#         def display(self):
#             print(f"Date of birth is : {self.date} / {self.month} / {self.year}")


# s1 = Student('Ajay' , 101 , 26 , 3 , 1999) 

  
# s1.display()   # output :   name is Ajay and roll is 101
                           # Date of birth is : 26 / 3 / 1999







# _____________________________________________________________________________________________________________________________________ 



# :: How to access members of one class into another class : 


# NOTE : @staticmethod ( decorator ) ak aisa method hota hai  , Jo ki external data pr operations perform krta hai. 

# - Ex : 

# class Employee:
#     def __init__(self , eid , name , sal):
#         self.emp_id = eid 
#         self.emp_name = name 
#         self.emp_salary = sal 

#     def display(self):
#         print("Employee id : ", self.emp_id)
#         print("employee name :" , self.emp_name)
#         print("employee salary :" , self.emp_salary)


# class Changes:
#     @staticmethod
#     def increment(obj):
#        obj.emp_salary = obj.emp_salary + 2000
#        obj.display()





# e1 = Employee(101 , 'shantanu' , 50000)
# Changes.increment(e1)


# e1.display()
# output : 
# Employee id :  101
# employee name : shantanu
# employee salary : 52000











# _____________________________________________________________________________________________________________________________________ 




# :: Destructor In Python :   ( watch video )

# - In OOP , we have two terms , they two are completly Reverse of each other. :-
# 1.) Constructor    : __init__()
# 2.) Destructor     : __del__()





# :--> Destructor : 

# - A special method which destroys objects and releases resources tied to objects. 
# - Destructor is called automatically when object is destroyed. 
# PURPOSE :   Releasing objects tied to destroyed objects. 





# Explanation :  variable x , y ko garbage collector memory se delete kr dega but jo tied refrence database connection and file handelling mai hai usse dlt nhi krega , uske liye ham destructor ka use krenge. 
# - Ex : 

# x = 100 
# y = 200 

#--> dattabase connection performing 
#--> cache created 
#--> file handeling done











# :-->  Below are  two conditions when destructor is called :- 

# 1.) Reference counting reaches to 0. 

# 2.) When variable goes out of scope. 


# NOTE : In Python  , The special method __del__() is used to define a destructor. 















# :--> Object Creation & Deletion in Python : 

# 1. object creation :  

# emp = Employee('Jay', 50000)  #--> Arguments passed here for constructor to initialize variables. 



# 2. Inbuilt-methods executes : 

# --> Object is created using __new__() method. 

# --> Object is initialized using __init__() method. 




# 3.) Deletion of obj : 


# del emp ( inbuilt-method perform this functionality ) 




# 4.) use of destructor : 

# --> Destructor invoked using  __del__() method . 











# - Ex :  

# class Employee:
#     def __init__(self , nm , sal):
#         self.name = nm 
#         self.salary = sal 

#     def display(self):
#         print(f"name is  {self.name} \n salary is  : {self.salary} ")

    
#     # defining destructor : 
#     def __del__(self):
#         print("Destructor is called")


# e1 = Employee("Shantanu" , 50000)
# e1.display()


# del e1   # output :
# name is  Shantanu 
# salary is  : 50000 
# Destructor is called












# _________________________________________________________________________________________________________________________________




# :: Disadvantages of Destructor : 

# 1.)  Circular Refrencing :- 
# - When two objects refer to each other. 


# # - Ex : 

# import time 

# class Employee:
#     def __init__(self , obj2):
#         self.obj2 = obj2

#     def __del__(self):
#         print("Employee class destructor called")


# class Account:
#     def __init__(self , num):
#         self.account_number = num
#         self.obj1 = Employee(self)
        

#     def __del__(self):
#         print("account class destructor called")

        


# ac = Account(1234)

# del ac
# time.sleep(5)


# output :  
# account class destructor called
# Employee class destructor called





















# 2.) Exception occurs in __init__():

# - Destructor calls even if constructor (__init__() ) does not execute well.
# - Object is not initialized and destructor is clearing resources. 
# - May lead to another exception. 

# - Ex : 

# class NegativeAge(Exception):
#     pass 


# class Age:
#     def __init__(self , ag):
#         if ag < 0:
#             raise NegativeAge("age can't be Negative")
        

#     def __del__(self):
#         print("Destructor is called") 



# ag = Age(-10)

# output : 

# NegativeAge: age can't be Negative
# Destructor is called








# _________________________________________________________________________________________________________________________________




# :: Storing Object in list : 

# - Ex :  


# class Movie(object):
#     def __init__(self , title , mins , hero):
#         self.title = title 
#         self.runtime = mins
#         self.hero = hero 

#     def printer(self):
#         print(f"Title is : {self.title} \n runtime is : {self.runtime} \n hero is : {self.hero}")


# list_of_movies = []


# while True:
#     title = input("Enter the title of movie :")
#     mins =  input("Enter the runtime of movie :")
#     hero =  input("Enter the name of hero of movie :")
#     obj =  Movie(title ,mins , hero )

#     list_of_movies.append(obj)

#     print("Movie added to the list!")

#     ans = input("DO you want to add another movie(y/n) :")
#     if ans != 'y':
#         break 


# print("All movies information :")

# for obj in list_of_movies:
#     obj.printer()


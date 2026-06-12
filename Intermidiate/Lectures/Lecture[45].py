
# :: Youtube Playlist Content : 

# --> lecture-226 : OOPS-36.
# --> lecture-227 : OOPS-37. 
# --> lecture-228 : OOPS-38. 
# --> lecture-229 : OOPS-39. 
# --> lecture-230 : OOPS-40. 


# _____________________________________________________________________________________________________________________________________




# :: Types of decorators : 
 

# 1.) Function decorator
# 2.) Class decorator 




# 2.) -->  class Decorator : 

# - class decorator inculedes the use of callable methods ,  agar kisi class ke ander callable method hai toh uss class ke objects ko ham call krr skte hai. 

# - Ex : 

# class Decorator(object):
#     def __init__(self , func):
#         self.function = func

#     def __call__(self , a , b):     #--> __Call__ magic method is responsible for takinf obj as callable method. 
#         result =  self.function(a , b) # original functnality
#         return result ** 2 # square (additional functnality) 



# @Decorator
# def add(a , b):
#     return a + b

# print(add(1 , 2))   #-->  9    [  add.__call__(a , b)  ]














# :-->  Explanation : 




# 1. Class Decorator ka concept :

# Python mein agar kisi class ke andar __call__ method define ho, toh us class ke objects ko function ki tarah call kar sakte ho. Matlab object ko () ke saath use karoge toh __call__ method execute hoga.








# 2. Code Explanation :


# class Decorator(object):

#     def __init__(self , func):
#         self.function = func   # yeh original function ko store kar raha hai


#     def __call__(self , a , b):   # jab object ko call karenge toh yeh chalega
#         result = self.function(a , b)   # original function ko call kiya
#         return result ** 2              # aur uske result ka square return kiya



# __init__: jab decorator banega, usme original function (add) store ho jayega.

# __call__: jab object ko call karenge, toh pehle original function execute hoga, phir uske result ka square return hoga.








# 3. Decorator ka use : 




# @Decorator
# def add(a , b):
#     return a + b
# Yeh line ka matlab hai: add = Decorator(add)

# Matlab add ab ek Decorator class ka object ban gaya hai, jisme original add function store hai.








# 4. Execution :



# print(add(1 , 2))
# Jab add(1,2) call karte ho, toh actually Decorator class ka __call__ method run hota hai.

# self.function(a,b) → add(1,2) → 3

# return result ** 2 → 3 ** 2 = 9

# Output: 9






# 5. Summary :



# __call__ method ek object ko function ki tarah callable banata hai.

# Decorator class original function ko wrap karta hai aur uske result par extra functionality add karta hai (yaha square).

# Isliye add(1,2) ka result 9 aaya, na ki 3.











# _____________________________________________________________________________________________________________________________________




# ::   Class Decorator Example : 

# - Ex : 


# def add(*args):
#     sum1 = 0 
#     for num in args:
#         sum1 = sum1 + num 
#     return sum1 


# print(add(10 , 20 ,30))


# print(add(10 , '20' , 30))   # output : print(add(10 , '20' , 30))
#           ~~~^^^^^^^^^^^^^^^^
#   File "c:\Users\ANUBHAV\Program_Folders\Python\Intermidiate\Lectures\Lecture[45].py", line 172, in add
#     sum1 = sum1 + num
#            ~~~~~^~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'





# NOTE :  we see that execution has stopped beacuse of unsupported operand , now we have to use class decorator to modify the function and make the program as simple as that it continue the flow of execution and just give an error and does not break the flow of execution. 

# - Ex : 



# class Decorator(object):
#     def __init__(self , func):
#         self.function = func

#     def __call__(self , *args):
#         try:
#             if any([isinstance(i , str) for i in args]):  #--> [False , True , False]
#                 raise TypeError("Cannot pass string as arguments")
#             else:
#                 self.function(*args)
#         except Exception as obj:
#             return obj

        



# @Decorator   # --> it is equal to  : add = Decorator()
# def add(*args):
#     sum1 = 0 
#     for num in args:
#         sum1 = sum1 + num 
#     return sum1 


# print(add(10 , 20 ,30))


# print(add(10 , '20' , 30))
# output : 
# None
# Cannot pass string as arguments
# None
# Cannot pass string as arguments


# add(10 , '20' , 30)    #--> add.__call__()















# _____________________________________________________________________________________________________________________________________






# :: Built-in Decorators : 

# 1.) @classmethods - ( covered )
# 2.) @staticmethod - ( covered )
# 3.) @property 





# 3.) @property : 

# --> Need of property decorator : 

# - Ex : 

# class Employee:
#     def __init__(self , first , last):
#         self.firstname = first 
#         self.lastname = last 
#         self.mail = first + last + '@gmail.com'

#     def fullname(self):
#         return f'{self.firstname} {self.lastname}'
    

# e = Employee("shantanu" , "kejkar")
# e1 = Employee("rajandra", "jaiswal")
# e2 = Employee("Aman" , "thakur")



# e.firstname = 'Jay'
# print(e.firstname)
# print(e.mail)
# print(e.fullname())

# print('-' * 40)

# print(e1.firstname)
# print(e1.mail)
# print(e1.fullname())

# print('-' * 40)


# print(e2.firstname)
# print(e2.mail)
# print(e2.fullname())



# output : 

# Jay
# shantanukejkar@gmail.com
# Jay kejkar
# ----------------------------------------
# rajandra
# rajandrajaiswal@gmail.com
# rajandra jaiswal
# ----------------------------------------
# Aman
# Amanthakur@gmail.com
# Aman thakur


# NOTE :  As we see changing name of e does not give any effect of email , so we want if the name is changed  , it also updated the email.



# class Employee:
#     def __init__(self , first , last):
#         self.firstname = first 
#         self.lastname = last 
#         # self.mail = first + last + '@gmail.com'

#     def mail(self):
#         return f'{self.firstname} {self.lastname}@gmail.com'

#     def fullname(self):
#         return f'{self.firstname} {self.lastname}'
    

# e = Employee("shantanu" , "kejkar")
# e1 = Employee("rajandra", "jaiswal")
# e2 = Employee("Aman" , "thakur")



# e.firstname = 'anubhav'
# print(e.firstname)
# print(e.mail())
# print(e.fullname())

# print('-' * 40)

# print(e1.firstname)
# print(e1.mail())
# print(e1.fullname())

# print('-' * 40)


# print(e2.firstname)
# print(e2.mail())
# print(e2.fullname())




# NOTE : abb isme hame particular object mai kuch bhi change krna ho to barbar assign krna pad rha hai value for large data set we have to use @property method and remove the call method :



# - Ex : 




# class Employee:
#     def __init__(self , first , last):
#         self.firstname = first 
#         self.lastname = last 
#         # self.mail = first + last + '@gmail.com'

#     @property
#     def mail(self):
#         return f'{self.firstname} {self.lastname}@gmail.com'

#     def fullname(self):
#         return f'{self.firstname} {self.lastname}'
    

# e = Employee("shantanu" , "kejkar")
# e1 = Employee("rajandra", "jaiswal")
# e2 = Employee("Aman" , "thakur")



# e.firstname = 'anubhav'
# print(e.firstname)
# print(e.mail)   #--> using property method
# print(e.fullname())

# print('-' * 40)

# print(e1.firstname)
# print(e1.mail)   #--> using property method
# print(e1.fullname())

# print('-' * 40)


# print(e2.firstname)
# print(e2.mail)  #--> using property method
# print(e2.fullname())





















# :--> @getter and @setter with @property method :


# -->getter and setter ki help se hamne complete fullname ko change krne ka functionality create kiya
# # - Ex : 





# class Employee:
#     def __init__(self , first , last):
#         self.firstname = first 
#         self.lastname = last 
#         # self.mail = first + last + '@gmail.com'

#     @property
#     def mail(self):
#         return f'{self.firstname} {self.lastname}@gmail.com'

#     @property
#     def fullname(self):   #--> making this as :  @getter 
#         return f'{self.firstname} {self.lastname}'
    
#     @fullname.setter
#     def fullname(self , name):   #--> making this as :  @setter 
#         first , last = name.split()
#         self.firstname = first 
#         self.lastname = last

    
#     @fullname.deleter
#     def deleter(self):  # --> making this as : @deleter
#         self.firstname = None 
#         self.lastname = None

    

# e = Employee("shantanu" , "kejkar")
# e1 = Employee("rajandra", "jaiswal")
# e2 = Employee("Aman" , "thakur")



# e.firstname = 'anubhav'


# print(e.firstname)
# print(e.mail)   #--> using property method
# print(e.fullname)

# e.fullname = "anubhav pathak"

# print("after setting :")
# print(e.fullname)


# print(e.deleter)




# print('-' * 40)



# e1.firstname = "Jay"
# print(e1.firstname)
# print(e1.mail)   #--> using property method
# print(e1.fullname)

# print('-' * 40)


# print(e2.firstname)
# print(e2.mail)  #--> using property method
# print(e2.fullname)








# _____________________________________________________________________________________________________________________________________





# :: callable() and __call__() method : 


# :--> callable() :
# - it returns boolean True if passed object is callable and return False if passed object is not callable. 
# - Syntax : callable( Python_objects ). 


# :--> callable objects ?
# - Objects which can be called whenever required. 
# - Objects having __call__() method in their class. 



# - Ex : checking function are callable or not   : callable
 
# x = 100 

# def add(a , b):
#     return a + b 


# print(add(10 , 20))  # output : 30   [ add.__call___(10 , 20)]

# print(add.__call__(10 , 20)) # outout : 30 



# print(type(add))   # output : <class 'function'> 

 
# print(callable(x))  # output : False

# print(callable(add)) # output : True






# - Ex : checking classes or objects are callable or not  :   callable



# class Add(object):
#     def __init__(self , a , b):
#         self.a = a 
#         self.b = b 


# a1 = Add(10 , 20)


# print(callable(Add))  # output : True   ( so classes are callable )


# print(callable(a1))  # output : False  ( and object are non - callable )



# NOTE : for making the object callable we have to use magic method __call__() :




# class Add(object):
#     def __init__(self , a , b):
#         self.a = a 
#         self.b = b 

#     def __call__(self , a , b):
#         return a + b 
    
# a1 = Add(10  , 20)      #--> a1.__call__(10 , 20)
# print(a1(10 , 20))   # output : 30
# print(callable(a1))  # output : True


# print(a1(100 , 500))  # outout : 600








# _____________________________________________________________________________________________________________________________________





# ::  Abstraction - Interface in Python : ( watch video )

# - The Process by which data and functions are defined in such a Way that only essential details can be seen and unnecessary implementations are hidden is called Data Abstraction. 

# - Hiding complex implementation details and showing only signatures(functionality) to users. 


# :--> How abstraction achieved in Python :- 

# - By using abc module :- ABC class  (abstractmethod) 

# - Inherit your class from ABC class

# - Create abstract methods in your abstract class. 



# :--> Syntax : 

# from abc import ABC , abstractmethod 

# class Employee(ABC):
#     #abstract methods 
#     #conrete methods



# Abstract methods :- methods that has a declaration but does not have an implementation. 

# Concrete methods :- Normal methods.  




# - Ex : 


# from abc import ABC , abstractmethod 




# class Car(ABC):
#     @abstractmethod
#     def mileage(self):
#         pass 

#     def color(self):
#         print("white")



# class Maruti_Suzuki(Car):
#     def mileage(self):
#         print("mileage is 30kmph")


# class TATA(Car):
#     def mileage(self):
#         print("mileage is 35kmph")


# class Dustor(Car):
#     def mileage(self):
#         print("mileage is 40kmph")


# # c1 = Car()

# m1 = Maruti_Suzuki()
# t1 = TATA()
# d1 = Dustor()

# m1.mileage()  # output : mileage is 30kmph
# t1.mileage()  # output : mileage is 30kmph
# d1.mileage()










# :--> Abstract class :- 

# -> A class which contains one or more abstract methods and concrete methods. 
# -> Abstract class must have at least one abstract method. 
# -> An abstract class can be considered as a blueprint for other classse. 
# -> A class which is inherited from ABC class. 



# NOTE :  

# 1.) You can't instantiate abstract classes. 
# 2.) Abstract class requires at least one method abstract. 
# 3.) All abstract methods present in abstract class must be implemented in child classes. Else , child class becomes abstract. 
# 4.) If there is abstract method in class , that class must be abstract class. 







# :--> Uses of abstraction :- 

# 1.) When we have large code and functionalities. 

# 2.) Your abstract class is like an API for other subclasses. 

# 3.) used when a third party is going to provide implementations. 

# 4.) When we have different implementations for different objects for same component. 

# 5.) For creating interfaces : interfaces are that class which contain only abstract methods no concrete methods are present.  Ex : CMD ( command prompt )


# - Ex:   ( 2nd point )



# ATM :- 

# 1. withdraw()
# 2. deposit()
# 3. show_balance()
# 4. receipt()
# 5. PIN_change 




# SERVER :  Child_class 


## Withdraw money code 

## deposit money code 

## Show_balance code 

## receipt creation code 

## PIN change code

# :: Youtube Playlist Content : 

# --> lecture-211 : OOPS-21.
# --> lecture-212 : OOPS-22. 
# --> lecture-213 : OOPS-23. 
# --> lecture-214 : OOPS-24 [part- 1 and part - 2]. 
# --> lecture-215 : OOPS-25. 


# _____________________________________________________________________________________________________________________________________


# :: MRO ( Method Resolution Order ) :

# - MRO represents how properties ( attributes + methods ) are searched in inheritance. 


# :-> Rule_01 : 
# - Python first search in child class and then goes to parent class. 
# - Priority is to child class. 




# :-> Rule_02 :   ( See Diagram in the video )
# - MRO Follows 'Depth First Left to Right approach'. 

# - MRO(o) : Object. 
# - MRO(A) : A , O. 
# - MRO(B) : B , O. 
# - MRO(C) : C , O.
# - MRO(X) : X , A , B , C , O. 
# - MRO(Y) : Y , B , C , O. 
# - MRO(P) : P , Y , X , Y , A , B , C , O.





# :-> Rule_03 : 
# - You can use MRO() method for knowing MRO of any class objects. 


# - Ex:  


# class A:
#     pass 

# class B:
#     pass 

# class C: 
#     pass 

# class X(A , B , C):
#     pass 


# class Y(B , C):
#     pass 


# class P(X , Y):
#     pass 



# print(P.mro())  # output :  [<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]









# _____________________________________________________________________________________________________________________________________



# :: Encapsulation in Python : 

# - Wrapping up data and methods working on data together in a single unit ( i.e class ) is called as Encapsulation. 

# - Ex : 

# class Emploeyee:
#     def __init__(self , name , salary):
#         self.name = name 
#         self.salary = salary 

#     def display(self):
#         print(f"name is :{self.name} and salary is: {self.salary}")


# :--> Need of Encapsulation : 


# class Finance: 
#     def __init__(self):
#         self.revenue = 100000 
#         self.number_of_sales = 114 


# f1 = Finance()


# class HR:
#     def __init__(self):
#         self.number_of_emp = 32 
#         print(f1.revenue)   #--> Here Encapsulation must needed to protect this variable

# h1 = HR()   # output :  100000  [ Finance class variable's value is directly access by the HR Class]


# print(f1.__dict__)  # output : {'revenue': 100000, 'number_of_sales': 114}











# NOTE: For these types of problems we Use Access modidiers For providing Encapsulation in Python. 







# :: Access Modifiers in Python : 

# - Generally , we restrict data access outside the class in encapsulation. 
# - Encapsulation can be achieved by declaring the data members and methods of a class as private. 
# - There are Three access specifiers :
# 1.) public 
# 2.) Private 
# 3.) Protected (less used). 





# 1.)  Public members :- 
# - Accessible anywhere by using object reference. 



# 2.) Private members :- 
# - Accessible within the class , Accessible via methods only. 
# - Ex : self.__variablename  ( this is the syntax of private members ) 




# 3.) Protected member :-
# - Acessible within class and it's subclassses. 
# - Ex : self._variablename ( this is the syntax of protected member )












# - Ex :   ( Creating private and protected data )


# class Finance:
#     def __init__(self):
#         self.__revenue = 100000  #----> private data 
#         self._number_of_sales = 114  #----> protected data 



# f1 = Finance() 
# print(f1.__dict__)


# class HR:
#     def __init__(self):
#         self.number_of_emp = 32 
#         print(f1.__revenue)



# h1 = HR()  # output :     print(f1.__revenue)
# #           ^^^^^^^^^^^^















# :----> Method to Access the Private members : 
# - by creating the method display()

# class Finance:
#     def __init__(self):
#         self.__revenue = 100000  #----> Private data 
#         self.__number_of_sales = 114  #----> Private data

#     def display(self):
#         print(f"revenue is : {self.__revenue} and number of sales : {self.__number_of_sales}")


    
# f1 = Finance()

# f1.display()  # output : revenue is : 100000 and number of sales : 114



# NOTE : Name handelling ka use hota hai private value ko store krne ke liye.  , Syntax :  _className__variableName

# print(f1.__dict__)  # output : {'_Finance__revenue': 100000, '_Finance__number_of_sales': 114} 







# :---> Creating the private method : 


# - Ex : 

# class Finance:
#     def __init__(self):
#         self.__revenue = 100000 #----> Private data 
#         self.__number_of_sales = 114 #----> Private data 


#     def __display(self):
#         print(self.__revenue)

# f1 = Finance()
# f1.__display()   # output :     f1.display()
# #     ^^^^^^^^^^
# AttributeError: 'Finance' object has no attribute 'display'





# :-> Advantages : 

# 1.) Security
# 2.) Prevents accidental modifications 
# 3.) Simplicity 




















# _____________________________________________________________________________________________________________________________________




# :: Polymorphism in Python : 

# - Polymorphism in Python is an ability of Python object to take many forms. 
# - If a variable , Object , method performs different behaviour according to situation is called as polymorphism. 


# - Ex :   ( + Operator :  Python Object )



# print(10 + 20)  # --> here it adds the specific inputs.

# print("hello" + "welcome")    #--> herer it concatenates the specific inputs. 









# - Ex :  len() Function 


# print(len("hello"))   # here it counts numbers of characters.

# print(len['h' , 'e' , 'llo'])   # count number of items.

# print(len(dictionary))  # here it give the number of keys.






# _____________________________________________________________________________________________________________________________________




# :: Polymorphism with inheritance : 

# - Ex : 


# class Vehicle:

#     def __init__(self , name , color , price):
#         self.name = name 
#         self.color = color 
#         self.price = price 

#     def get_details(self):
#         print("name is : " , self.name)
#         print("color is :",  self.color)
#         print("price is :",  self.price)
    
#     def max_speed(self):
#         print("maximum speed limit is 100")

#     def gear(self):
#         print("gear change is : 6")



# class Car(Vehicle): 
#     def max_speed(self):
#         print("maximum speed limit is 140")

#     def gear(self):
#         print("gear change is 7")



# v1 = Vehicle("Truck" , 'red' , 20000000)
# c1 = Car("Car" , "white" , 7000000)

# v1.get_details()
# v1.max_speed()

# print('-' * 50)

# c1.get_details()
# c1.max_speed()




# output :  
# name is :  Truck
# color is : red
# price is : 20000000
# maximum speed limit is 100
# --------------------------------------------------
# name is :  Car
# color is : white
# price is : 7000000
# maximum speed limit is 140











# _____________________________________________________________________________________________________________________________________






# :: Over-riding built-in functions : 

# NOTE : print() function ak in-built magic methods __str__ ka use krti hai value ko print krne ke liye . jbb bhi c1 object ko print ke ander likha jayega then voh sbse pahle cart class ke ander search karega , so ham cart class ke ander __str__ ki value ko override krr denge. 

# - Ex : 

# class Cart:
#     def __str__(self):
#         return "This is cart class object"
    
# c1 = Cart()

# print(c1)  # output : This is cart class object










# - Ex :  overriding the len() function for the Cart class.   ( without overriding )




# class Cart: 
#     def __init__(self , basket1 , basket2 , basket3):
#         self.clothes = basket1 
#         self.electronics = basket2
#         self.other = basket3



# anubhav = Cart(['pant' , 'shirt' , 't-shirt'] , ['earphone' , 'mobile'] , ['chair'])

# print(len(anubhav))  # output :     print(len(anubhav))
#           ~~~^^^^^^^^^
# TypeError: object of type 'Cart' has no len()




# - Ex :  overriding the len() function for the Cart class.   ( with overriding )




# class Cart: 
#     def __init__(self , basket1 , basket2 , basket3):
#         self.clothes = basket1 
#         self.electronics = basket2
#         self.other = basket3

#     def __len__(self):
#         print("Total number of items in cart :")
#         return len(self.clothes) + len(self.electronics) + len(self.other)
          



# anubhav = Cart(['pant' , 'shirt' , 't-shirt'] , ['earphone' , 'mobile'] , ['chair'])

# print(len(anubhav))  # output :  Total number of items in cart : 6



# _____________________________________________________________________________________________________________________________________





# :: Polymorphism in functions and objects : 

# - Ex : 


# class BMW:
#     def fuel_type(self):
#         print("Diesel")

#     def max_speed(self):
#         print("max speed is 200")


# class Ferrari:
#     def fuel_type(self):
#         print("Petrol")

#     def max_speed(self):
#         print("max speed is 180")


# def car_details(obj):
#     obj.fuel_type()
#     obj.max_speed()

    

# bmw = BMW()
# ferrari = Ferrari() 



# car_details(bmw)
# print('-' * 40)
# car_details(ferrari)

# output : 
# Diesel
# max speed is 200
# ----------------------------------------
# Petrol
# max speed is 180
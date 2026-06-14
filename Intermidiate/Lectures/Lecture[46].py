
# :: Youtube Playlist Content : 

# --> lecture-231 : what is ADT.
# --> lecture-232 : Top 21 Magic Methods and Attributes in Python. 
# --> lecture-233 : Docstring in Python. 
# --> lecture-234 : Revision. 
# --> lecture-235 : Revision. 


# ______________________________________________________________________________________________________________________________________



# :: What is ADT ( Abstract Data Type ) : 
# -  ADT's are like user defined datatypes which define operations on values using function without specifying what is there inside a function and how operations are performed. 
# - You can think ADT as a black box which hides inner structure and design of datatypes from user. 




# - Ex: 

# list_1 = [10 , 20 , 'kamli' , 20.4]

# --> Find the length of above list : len(list)

# Explanation :  You don't know the actual or internal implementation of len() function. 





# STACK ADT : 


# :--> Operations :- 

# 1.) Initialise :- create an instance of stack. 
# 2.) Push :- adds an element at the end. 
# 3.) Pop :- removes element from stack. 
# 4.) IsEmpty :- Checks stack is empty or not.
# 5.) IsFull :- Checks stack is full or not.







# :: Advantages :- 

# 1. Implementation of stack : List , array  , linked list , numpy array. 

# 2. Reduce development time because of pre-defined implementations. 

# 3. Less bugs and Helps in debugging. 

# 4. Easy to change implementations. 





# ______________________________________________________________________________________________________________________________________





# :: Top 21 Magic Methods and Attributes : 


# :--> What are magic methods ?

# -A method that is called implicitly by Python to execute a certain operation on a type , such as addition. Such methods have names starting and ending with double unuderscores. 


# - Magic methods are special methods in Python that have double underscores(dunder) on both sides of the method. 
# - Naming Convention :- __methodname__ 

# - We don't need to call magic methods explicitely. Python automatically calls magic methods as a response to certain operations , such as instantiation. 


# :--> All 21 magic methods and attributes : 

# NOTE : There are 14 magic methods and 7 magic attributes. 

# ::14 magic methods :-

# 1.) __init__()
# 2.) __new__() 
# 3.) __str__()
# 4.) __repr__()
# 5.) __len__()
# 6.) __call__()
# 7.) __getitem__()
# 8.) __setitem__()
# 9.) __delitem__()
# 10.) __contains__()
# 11.) __iter__()
# 12.) __add__() 
# 13.) __eq__()
# 14.) __gt__()




# :: 7 magic attributes :-
# 1.) __all__
# 2.) __module__ 
# 3.) __bases__ 
# 4.) __defaults__ 
# 5.) __name__ 
# 6.) __doc__ 
# 7.) __dict__ 








# _______________________________________________________________________________________________________________________________________



# 1.) __init__(self) method : 

# - This method is called automatically to initialize attributes when an object is created. 
# - It's act like an constructor. 

# - Ex :

# class Bank:
#     def __init__(self , balance , aadhar , acc_no , name):
#         print("Init is running")
#         self.bank_balance = balance 
#         self.aadhar_number = aadhar 
#         self.account_number = acc_no 
#         self.customer_name = name 


# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , "shantanu kejkar") 

# print("bank balance is :" , b1.bank_balance)  # output : bank balance is : 100

# b1.bank_balance = b1.bank_balance + 1000 

# print("bank balance is :" , b1.bank_balance)  # output : bank balance is : 1100















# _______________________________________________________________________________________________________________________________________



# 2.) __dict__ attribute : 

# - It gives a dictionary containing instances variables and thier values if you call it with object. 
# - It gives a dictionary containing class variables and methods and their value if you call it with object. 
# - Basically it returns a namespace of object and class. 

# - Ex:  

# class Bank: 
#     def __init__(self , balance , aadhar , acc_no , name):
#         print("init is running")
#         self.bank_balance = balance 
#         self.aadhar_number = aadhar 
#         self.account_number = acc_no 
#         self.customer_name = name  




# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , "shantanu kejkar") 


# using __dict__ attribute with class :
# print(Bank.__dict__) 
# output : {'__module__': '__main__', '__firstlineno__': 179, '__init__': <function Bank.__init__ at 0x0000019CA3EE3690>, '__static_attributes__': ('aadhar_number', 'account_number', 'bank_balance', 'customer_name'), '__dict__': <attribute '__dict__' of 'Bank' objects>, '__weakref__': <attribute '__weakref__' of 'Bank' objects>, '__doc__': None}



# using __dict__ attribute with object : 
# print(b1.__dict__)
# output : {'bank_balance': 100, 'aadhar_number': '8976 5678 9091', 'account_number': 'IBH7890', 'customer_name': 'shantanu kejkar'}










# _______________________________________________________________________________________________________________________________________



# 3.) __new__() method : 

# - Python implicitly calls the .__new__() method as the first step in the instantiation process. 
# - Purpose : object ke liye memory allocate krna and instantiation process ko start krna. 

# - Ex : 

# class Bank:
#     bank_name = 'BOI'
#     def __init__(self , balance , aadhar , acc_no , name):
#         print("init is running")
        # self.bank_balance = balance 
        # self.aadhar_number = aadhar 
        # self.account_number = acc_no 
        # self.customer_name = name 
        
#     def display(self):
#         pass 

# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , "shantanu kejkar") 



# :--> Execution proces : __new__() method calls automatically starts the process instantiation ( process of creating object ) and then allocate the memory for the object and then object mai variable create krne ka kam hota hai -- __init__() method ka. 








# _______________________________________________________________________________________________________________________________________



# 4.) __str__():

# - In Python , the __str__() method is a special method used to define a string representation of an object. 
# - Purpose : basically agar ham object ko directly uske naming convention se print karate hai toh voh kya print krega usse ham control krr skte hai __str__() method ka use krke , by creating an external function inside the class and it only return a string value. 

# - Ex : 

# class Bank:
#     bank_name = 'BOI'
#     def __init__(self , balance , aadhar , acc_no , name):
#         print("init is running")
#         self.bank_balance = balance 
#         self.aadhar_number = aadhar 
#         self.account_number = acc_no 
#         self.customer_name = name
#     # def __str__(self):
#     #     return str(self.bank_balance)
    


# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , 'Shantanu Kejkar')

# print(b1) #--> it calls like this :  # b1.__str__()
# output: <__main__.Bank object at 0x00000204B2468C20>


        






# _______________________________________________________________________________________________________________________________________




# 5.) __repr__():

# - In Python , the __repr__() method is a special method used to define a string representation of an object. 
# - Purpose : basically agar ham object ko directly uske naming convention se print karate hai toh voh kya print krega usse ham control krr skte hai __repr__() method ka use krke , by creating an external function inside the class and it only return a string value. 
# NOTE: 
# - __str__() and __repr__() working are same but proiority of str > repr. 
# - __str__() ka use ham directly production mai krte hai , but debugging and testing in the dev enviornment ke liye __repr__() ka hi use hota hai. 

# - Ex : 

# class Bank:
#     bank_name = 'BOI'
#     def __init__(self , balance , aadhar , acc_no , name):
#         print("init is running")   # output : init is running
#         self.bank_balance = balance 
#         self.aadhar_number = aadhar 
#         self.account_number = acc_no 
#         self.customer_name = name
#     def __str__(self):
#         print("ye __str__ run hua!")
#         return str(self.bank_balance) 
#     def __repr__(self):
#         print("ye __repr__ run hua!")
#         return str(self.bank_balance)
    
    


# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , 'Shantanu Kejkar')

# print(b1)  # str wala mthod run hua. (100)



# #--> it calls like this :  # b1.__str__()
# output: <__main__.Bank object at 0x00000204B2468C20>










# _______________________________________________________________________________________________________________________________________


# 6. __len__():

# - In Python , the __len__() method used to define the length of an object. 

# - Ex : 


# class Bank:
#     bank_name = 'BOI'
#     def __init__(self , balance , aadhar , acc_no , name):
#         print("init is running")
#         self.bank_balance = balance 
#         self.aadhar_number = aadhar 
#         self.account_number = acc_no 
#         self.customer_name = name
    
   
    


# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , 'Shantanu Kejkar')



# print(len([10 , 20 , 30 , 40 , 50]))   # --> datatype : built-in class list -> __len__()


# print(len(b1))  # output :   print(len(b1))
#           ~~~^^^^
# TypeError: object of type 'Bank' has no len()




# NOTE :  we have tp create __len__() methof then it is able to giver the len output. 



# - Ex:  



# class Bank:
#     bank_name = 'BOI'
#     def __init__(self , balance , aadhar , acc_no , name):
#         print("init is running")
#         self.bank_balance = balance 
#         self.aadhar_number = aadhar 
#         self.account_number = acc_no 
#         self.customer_name = name

  

#     def __len__(self):
#         lenght = len(self.__dict__)
#         return lenght
    


    


# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , 'Shantanu Kejkar')

# print(len(b1))  # output : 4
# print(b1.__dict__)  # output : {'bank_balance': 100, 'aadhar_number': '8976 5678 9091', 'account_number': 'IBH7890', 'customer_name': 'Shantanu Kejkar'}


















# _______________________________________________________________________________________________________________________________________



# 7. __getitem__() :

# - In Python , the __getitem__() method is a special method that enables instances of a class to be accessed using the indexing syntax ([]). 

# - Ex : 

# class Bank: 
#     bank_name = 'BOI'
#     def __init__(self , balance, aadhar , acc_no , name):
#         print("init is running")
#         self.bank_balance = balance 
#         self.aadhar_number = aadhar 
#         self.account_number = acc_no 
#         self.customer_name = name 


# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , 'Shantanu Kejkar')


# # --> Ex :  list indexing 

# data = [10 ,20 , 30 , 40]    #list contains  --> __getitem__ to print object values by the use of indexing. 
# print(data[2])   # data.__getitem__(2) gives the answer = 30.






# print(b1[2])  #--> output :  print(b1[2])  #--> output :
# #           ~~^^^
# TypeError: 'Bank' object is not subscriptable







# NOTE : To access the object value by the object indexing method we must create , __getitem__() in the class itself . 



# - Ex : 


# class Bank: 
#     bank_name = 'BOI'
#     def __init__(self , balance, aadhar , acc_no , name):
#         print("init is running")
#         self.bank_balance = balance 
#         self.aadhar_number = aadhar 
#         self.account_number = acc_no 
#         self.customer_name = name 

#     def __getitem__(self ,key ):  #b1
#         return self.__dict__[key]
    


# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , 'Shantanu Kejkar')

# # print(b1[2])  #--> it runs like this :   b1.__getitem__()  


# print(b1['aadhar_number'])    #--> b1.__getitem__('aadhar_number')  gives answer : 8976 5678 9091



# print(b1.__dict__['bank_balance']) #--> b1.__getitem__('bank_balance')













# _______________________________________________________________________________________________________________________________________






# 8.  __setitem__() method : 

# - In Python , the __setitem__() is a special method that enables instances of a classs to support assignment using the indexing syntax ([]). 

# - Ex : 



# class Bank: 
#     bank_name = 'BOI'
#     def __init__(self , balance, aadhar , acc_no , name):
#         print("init is running")
#         self.bank_balance = balance 
#         self.aadhar_number = aadhar 
#         self.account_number = acc_no 
#         self.customer_name = name 

#     def __getitem__(self ,key ):  #b1
#         return self.__dict__[key]
    


# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , 'Shantanu Kejkar')


# b1['bank_balance'] = 1000   # output : b1['bank_balance'] = 1000
# #     ~~^^^^^^^^^^^^^^^^
# # TypeError: 'Bank' object does not support item assignment


# # NOTE : object indexing does not support the assigning , so we have to put an __setitem__() method for this in the class. 



# - Ex : 

# NOTE: when assignin key in dictionary it works internally :

# dictname[keyname] = new_value   #--> dictname.__setitem__(self , keyname  , new_value)




class Bank: 
    bank_name = 'BOI'
    def __init__(self , balance, aadhar , acc_no , name):
        print("init is running")
        self.bank_balance = balance 
        self.aadhar_number = aadhar 
        self.account_number = acc_no 
        self.customer_name = name 
    
    def __setitem__(self, instance_var, new_value):
        self.__dict__[instance_var] = new_value

    


b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , 'Shantanu Kejkar')

  
print(b1.__dict__)  # output : {'bank_balance': 100, 'aadhar_number': '8976 5678 9091', 'account_number': 'IBH7890', 'customer_name': 'Shantanu Kejkar'}

b1['bank_balance'] = 1000 # it runs like this : b1.__setitem__(self , instance , var , new_value)


print(b1.__dict__)  # output : {'bank_balance': 1000, 'aadhar_number': '8976 5678 9091', 'account_number': 'IBH7890', 'customer_name': 'Shantanu Kejkar'}



# :--> Fetching the previous value and perform operations on that : 




# class Bank: 
#     bank_name = 'BOI'
#     def __init__(self , balance, aadhar , acc_no , name):
#         print("init is running")
#         self.bank_balance = balance 
#         self.aadhar_number = aadhar 
#         self.account_number = acc_no 
#         self.customer_name = name 

#     def __getitem__(self, instance_var):
#         return self.__dict__[instance_var]
    
#     def __setitem__(self, instance_var, new_value):
#         self.__dict__[instance_var] = new_value

    


# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , 'Shantanu Kejkar')

# b1['bank_balance'] = b1['bank_balance'] + 1000

# print(b1.__dict__)  # output :  {'bank_balance': 1100, 'aadhar_number': '8976 5678 9091', 'account_number': 'IBH7890', 'customer_name': 'Shantanu Kejkar'}












# _______________________________________________________________________________________________________________________________________



# 10. __delitem__():

# - In Python , the __delitem__() method is a special method that enables instances of a class to support deletion of items using the del statements. 

# - Ex : 

# class Bank:
#     def __init__(self , balance , aadhar , acc_no , name):
#         print("init is running")
#         self.bank_balance = balance
#         self.aadhar_number = aadhar 
#         self.account_number  = acc_no
#         self.customer_name = name 



# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , 'Shantanu Kejkar')


# del b1.bank_balance 
# print(b1.__dict__)  # Output:  {'aadhar_number': '8976 5678 9091', 'account_number': 'IBH7890', 'customer_name': 'Shantanu Kejkar'}





# del b1['bank_balance']  # output :  del b1['bank_balance']  # output :
#         ~~^^^^^^^^^^^^^^^^
# TypeError: 'Bank' object does not support item deletion


# NOTE : normal del keyword can easily delete object values and their entire object. but the object indexing method is not able to delete and perform  the same , to solve this we have to create an __delitem__() method in the class. 


# - Ex :  





# class Bank:
#     def __init__(self , balance , aadhar , acc_no , name):
#         print("init is running")
#         self.bank_balance = balance
#         self.aadhar_number = aadhar 
#         self.account_number  = acc_no
#         self.customer_name = name 
    
#     def __delitem__(self, instance_var):
#         del self.__dict__[instance_var]    #--> self.'bank_balanace'



# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , 'Shantanu Kejkar')


# print(b1.__dict__) # output : {'bank_balance': 100, 'aadhar_number': '8976 5678 9091', 'account_number': 'IBH7890', 'customer_name': 'Shantanu Kejkar'}


# del b1['bank_balance'] 

# print(b1.__dict__)  # output : {'aadhar_number': '8976 5678 9091', 'account_number': 'IBH7890', 'customer_name': 'Shantanu Kejkar'}








# _______________________________________________________________________________________________________________________________________




# 11.  __contains__() method : 

# - In Python , the __contains__() method is a speacial method that enables instances of a class to support membership testing using the in operator. 

# - Ex : 

# class Bank:
#     def __init__(self , balance , aadhar , acc_no , name):
#         print("init is running")
#         self.bank_balance = balance 
#         self.aadhar_number = aadhar 
#         self.account_number = acc_no 
#         self.customer_name = name 




# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , 'Shantanu Kejkar')



# print('bank_balance' in b1)  # it runs like this : b1.__contains(self , instance_var)
# output :  b1.__contains(self , instance_var)
#           ^^^^^^^^^^^^^^^^^^^^
# TypeError: argument of type 'Bank' is not a container or iterable



# NOTE :  b1 object mai agar hame iterate karke in operator ka use krna hai agar toh hamko uss class ke ander __contains__() method ko banana pdega. 






# class Bank:
#     def __init__(self , balance , aadhar , acc_no , name):
#         print("init is running")
#         self.bank_balance = balance 
#         self.aadhar_number = aadhar 
#         self.account_number = acc_no 
#         self.customer_name = name 
    
#     def __contains__(self, instance_var):
#         return instance_var in self.__dict__     #--> { '' : val }




# b1 = Bank(100 , '8976 5678 9091' , 'IBH7890' , 'Shantanu Kejkar')


# print('bank_balance' in b1)  # b1.__contains__(self , instance_var)  # True








# _______________________________________________________________________________________________________________________________________



# 12.  __call__() method in Python : 

# - In Python , the __call__() method is a special method that allows an object to be called as if it were a function. 





















# _______________________________________________________________________________________________________________________________________

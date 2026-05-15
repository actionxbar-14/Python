
# :: Youtube Playlist Content : 

# --> lecture-91 : All about tuple() data structure.
# --> lecture-92 : Difference Between List and Tuple. 
# --> lecture-93 : Python Interview Questions and Answers. 
# --> lecture-94 : a+=b not always equal to a= a+b. 


# _______________________________________________________________________________________________________________________ 



# :: Tuple in Python :

# - Collection of items of different types. 
# - It is unchangeable ( Immutable ). 
# - It is nearly similar to the list. 


# - Ex : 

# data = ('shantanu' , 1 , 23.4 , 2+4j , ['cricket' , 'chess'])

# print(data)  # output : ('shantanu', 1, 23.4, (2+4j), ['cricket', 'chess'])













# :--> How to Create Tuples in Python : 
# - There are basically three ways to create tuples. 


# 1.) Using paranthesis (). 
# 2.) Using tuple() function. 
# 3.) Separating items by commma. 






# 1.  Using paranthesis () : 

# - Ex :

# tuple_data = ('shantanu' , 1 , 23.4 , 2+4j , ['cricket' , 'chess'])
# print(tuple_data)





# 2.) Using tuple() function :

# - Ex : 

# data = ['shantanu' , 2 , 78.9 , 'pune']
# tuple_data = tuple(data)

# print(tuple_data)  # output : ('shantanu', 2, 78.9, 'pune')

# print(type(tuple_data))  # output : <class 'tuple'>



# - Ex : 


# tuple_data = tuple("Anubhav")

# print(tuple_data)  # output : ('A', 'n', 'u', 'b', 'h', 'a', 'v')

# print(type(tuple_data))  # output :   <class 'tuple'>







# 3.) Sepearating items by comma : 


# - Ex : 

# tuple_data = 'shantanu' , 101 , 90.6 , 'pune'
# print(tuple_data)  # output : ('shantanu', 101, 90.6, 'pune')

# print(type(tuple_data))  # output :  <class 'tuple'>








# NOTE :  



# 1.)  Creating empty tuple :

# - Ex : 

# tuple_data = ()

# print(tuple_data)   # output : ()

# print(type(tuple_data))  # output : <class 'tuple'>






# 2.)  Creating tuple of length one :

# - Ex : 


# tuple_data = (20 ,)
# print(tuple_data)  # output: (20,)

# print(type(tuple_data)) # output:  <class 'tuple'>






















# :--> Characteristics of tuple :

# - there are basicly 7 characterstics. 

# 1.) Immutable ( Unchangeable )
# 2.) Heterogeneous 
# 3.) Contains Duplicates 
# 4.) We can pack and unpack tuple 
# 5.) all elements can be of same type 
# 6.) Can't add or delete elements 
# 7.) We can have nested tuple 







# 1.) Immutable ( Unchangeable ) :
# - We can not update and add elements. 

# - Ex: 

# data = (101 , 'shantanu' , 90.2 , 'A+' , 'shantanu')

# print(data)
# print(type(data))

# data[2] = 88   # TypeError: 'tuple' object does not support item assignment

# data.append(10)   #AttributeError: 'tuple' object has no attribute 'append' 





# 4.) packing and unpacking tuple : 

# - Ex : 


# data = (101 , 'shantanu' , 90.2 , 'A+' , 'shantanu')  #--> packing

# rollno , name1_ , marks , grade , name2_ = data  #--> unpacking 

# print(rollno)  #--> 101
# print(name1_)  #--> shantanu
# print(marks)   #--> 90.2
# print(grade)   #--> A+
# print(name2_)  #--> shantanu 

















# :--> Operations on tuple :

# 1.) Concatenation of tuples 
# 2.) Repetation of tuple 
# 3.) Deleting entire tuple 
# 4.) membership in tuple 
# 5.) Iterating a Tuple 
# 6.) Length of a Tuple 











# 1.) Concatenation of tuple : 

# - Ex : 

# personal_data = ('shantanu', 'pune' , True)

# academics_data  = (101 , 90.2 , 'A' , 'Pass')

# details = personal_data  + academics_data 

# print(details)   # output : ('shantanu', 'pune', True, 101, 90.2, 'A', 'Pass')
# print(type(details))  # <class 'tuple'>







# 2.) Repetation of tuple : 

# - Ex : 

# personal_data = ('shantanu', 'pune' , True)

# print(personal_data * 3)  # output : ('shantanu', 'pune', True, 'shantanu', 'pune', True, 'shantanu', 'pune', True)

# print( personal_data)







# 3.) Deleting entire tuple : 

# - Ex : 

# personal_data = ('shantanu', 'pune' , True)

# del personal_data 

# print(personal_data)  # output :    print(personal_data)
#           ^^^^^^^^^^^^^
# NameError: name 'personal_data' is not defined










# 4.) membership in tuple : 

# - Ex : 

# personal_data = ('shantanu', 'pune' , True)

# print('pune' in personal_data) # putput : True

# print('pune' not in personal_data) # output : False







# 5.)  Iterating a Tuple : 

# - Ex :  ( for loop )


# personal_data = ('shantanu', 'pune' , True)

# for element in personal_data:
#     print(element)


 
# - Ex :   ( while loop )

# personal_data = ('shantanu', 'pune' , True)

# index = 0
# while index < 3 :
#     print(personal_data[index])
#     index +=1
    
    










# 6.) Length of a Tuple : 

# - Ex : 

# personal_data = ('shantanu', 'pune' , True)

# print(len(personal_data))  # output : 3












# :--> Accessing items of a Tuple : 

# 1.) Indexing 
# 2.) Slicing 






# 1.) Indexing : agar ak element of tuple access krna hai toh indexing use krenge. 
# - Syntax : variable_name[index]

# - Ex : 


# personal_data = ('shantanu', 'pune' , True)

# print(personal_data[0]) # output : shantanu






# 2. Slicing : agar range of elements or multiple elements access krne hai toh Slicing ka use krenge.
# - Syntax : variable_name[start , stop , step]

# - Ex : 

# personal = ('shantanu' , 'pune' , True , 10 , 20,4)

# print(personal[1:4:1])



















# :-- Important methods of tuple :


# 1.) index(item, [start] , [end])
# 2.) count()





# 1.) index(item, [start] , [end]) :
# - Search for a certain item in a tuple. 
# - returns index of first match. 


# - Ex : 

# data = (10 , 20 , 30 , 40 , 50 , 20 , 40  , 30 , 20 , 10)

# print(data.index(30))  # output : 2


# - Ex : ( with start index )


# data = (10 , 20 , 30 , 40 , 50 , 20 , 40  , 30 , 20 , 10)

# print(data.index(30, 3))  # output : 7



# - Ex : ( with start and end index )


# data = (10 , 20 , 30 , 40 , 50 , 20 , 40  , 30 , 20 , 10)

# print(data.index(30 , 0 , 5))  # output : 2









# 2.) count() :
# - To count number of occurences. 

# - Ex : 

# data = (10 , 20 , 30 , 40 , 50 , 20 , 40  , 30 , 20 , 10)


# print(data.count(20))  # output : 3
























# :--> Python built-in function on Tuple :

# 1.) min()
# 2.) max()
# 3.) sum()






# 1.) min() : 


# - Ex : 

# data = (10 , 20 , 30 , 40 , 50 , 20 , 40  , 30 , 20 , 10)

# print("Minimum :" , min(data))  # output : Minimum : 10



# - Ex : 
# NOTE : it checks the ORD value in a string based tuple

# data = ("shantanu" , "raj" , 'Yash' , 'yash' , 'yashraj' , 'kiran')

# print("Minimun : " , min(data))  # output :- Minimun :  Yash



# # - Ex : 

# # NOTE : for checking based on length we have to give len as a key. 

# data = ("shantanu" , "Raj" , 'Yash' , 'yash' , 'yashraj' , 'kiran')

# print("Minimum :" , min(data , key=len))  # output :-  Minimum : Raj











# # 2.) max() :

# # - Ex :
# print("Maximum :" , max(data))  # output : Maximum : 50



# - Ex : 
# NOTE : it checks the ORD value in a string based tuple

# data = ("shantanu" , "raj" , 'Yash' , 'yash' , 'yashraj' , 'kiran')

# print("Maximum : " , max(data))  # output :- Maximum :  yashraj



# # # - Ex : 

# # # NOTE : for checking based on length we have to give len as a key. 

# data = ("shantanu" , "Raj" , 'Yash' , 'yash' , 'yashraj' , 'kiran')

# print("Maximum :" , max(data , key=len))  # output :- Maximum : shantanu









# # 3.) sum() :

# # - Ex :
# print("Sum :" , sum(data))  # output : Sum : 270





























# :-->  Some important function in tuple : 


# 1.) all()
# 2.) any() 
# 3.) sorted() 




# 1.) all() :
# - In the case of all() function , the return value be true when all the values inside are true. 

# - Ex : 

# tuple1 = (1 , 1, True)

# print(all(tuple1))  # output : True


# - Ex : 

# tuple2 = ()
# print(all(tuple2))  # output : True












# 2.) any() :
# - The any() method will return true if there is at least one true value. In the case of the empty tuple , it will return false. 



# - Ex : 

# tuple1 = (0 , 0 , 1)
# print(any(tuple1))  # output : True



# - Ex : 

# tuple2 = ()
# print(any(tuple2))  # output : False










# 3.) sorted() :
# - The sorted() function returns a new sorted list containing all elements from the tuple. 

# - Ex : 

# tuple1 = (10 , 46 , 23 , 45, 1 ,9 , -4)

# print(sorted(tuple1))  # output : [-4, 1, 9, 10, 23, 45, 46]


# - Ex :   ( using list ) 

# list1 = [10 , 46 , 23 , 45, 1 ,9 , -4] 
# print(tuple(sorted(list1))) # output : [-4, 1, 9, 10, 23, 45, 46]











# NOTE : 
# :-- > Modify nested items of a tuple :
# - If one of the items is itself a mutable data type as a list , then we can change that items values. 

# # - Ex : 

# tuple1 = (30 , 40  , [35 , 13 , 16])

# print("tuple before change: ",tuple1)   # output : tuple before change:  (30, 40, [35, 13, 16])

# print(id(tuple1))  # output : 1911210567168

# tuple1[-1][0] = 100


# print("tuple after change :", tuple1)  # output : tuple after change : (30, 40, [100, 13, 16])

# print(id(tuple1))  # output : 1911210567168
















# _______________________________________________________________________________________________________________________ 




# :: difference between List and tuple : 




# 1.) Creation : 

# - List is a comma seperated values in square brackets [] , and square bracket is mandatory. 
# - Ex : 

# Data = ['jay' , 23 , 30000]
# print(Data)



# - Tuple is a comma separated values in parenthesis () , and parenthesis is optional. 
# - Ex : 

# Data = ('jay' , 23 , 30000)
# Data = 'jay' , 23 , 30000
# print(Data)










# 2.) Mutability :

# - List is Mutable. 

# - tuple is Unmutable. 











# 3.) Memory Consumption :

# - Tuple object takes less memory than list object for same data. 

# - List is slow in execution than tuple. 

# - List is less efficient in memory utilization than tuple. 



# - Ex :  

# import sys

# list1 = ['hello' , 12 , True , 0]


# tuple1 = ('hello' , 12 , True , 0)


# print(sys.getsizeof(list1))  # output : 88
# print(sys.getsizeof(tuple1))  # output : 72









# 4.) Comprehension Concept : 

# - Comprehension concept is applicable only for list and not for tuple. 



# 5. )  Packing and Unpacking :

# - List supports packing but not support unpacking. 

# - Tuple supports both packking and unpacking. 














# _______________________________________________________________________________________________________________________




# :: Python Tricky Question : 



# Ques :-  Predict the Output : 

# x = ['a' , 'b', 'c'  ,'d']

# for x[-1] in x:
#     print(x[-1] , end = "")
    
    
# a.) dddd
# b.) abcc  [right]
# c.) abcd 
# d.) error



# Ans :  { watch the video for revision [lecture] - 93 }





# _______________________________________________________________________________________________________________________



# :: Mystery :- (Be carefull while using a += b)


# - In integer , complex no. etc , the compount operator behaves same - naya object banega and refrence naye object ka banega , original object mai koi change nahi hoga. 


# # - Ex :  

# a = 10 

# print("Value of a : " , a)  # output : Value of a :  10
# print("id of a :" , id(a))  # output : id of a : 140705931846728

# a = a + 10

# print("Value of a : " , a)   # output : Value of a :  20
# print("id of a :", id(a))    # output : id of a : 140705931847048

# a += 10 
# print("Value of a : " , a)   # output : Value of a :  20
# print("id of a :", id(a))    # output : id of a : 140705931847048









# - but list is immutable collective data type , so ye different behave krega :


# a = [10 , 20 , 30]
# print("Value of a : " , a)    # output : Value of a :  [10, 20, 30]
# print("id of a :", id(a))     # output : id of a : 1904436466816



# a = a + [40 , 50]
# print("Value of a : " , a)   # output : Value of a :  [10, 20, 30, 40, 50]
# print("id of a :", id(a))    # output : id of a : 1904437918272






# - in compound operator : 

# a = [10 , 20 , 30]
# print("Value of a : " , a)    # output : Value of a :  [10, 20, 30]
# print("id of a :", id(a))     # output : id of a : 1904436466816

# a += [40 , 50]
# print("Value of a : " , a)    # output : Value of a :  [10, 20, 30, 40, 50]
# print("id of a :", id(a))     # output : id of a : 1904436466816




# NOTE: 
# :: REASON 

# --> a1 += [3]       :-      Uses__iadd__  (this method is called)
# --> b1 = b1 + [3]   :-      Uses__add__   (this method is called)
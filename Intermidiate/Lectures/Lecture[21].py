
# :: Youtube Playlist Content : 

# --> lecture-106 : Deleting Operation of dictionary - 1.
# --> lecture-107 : Deleting Operation of dictionary - 2. 
# --> lecture-108 : Update Method in dictionary. 
# --> lecture-109 : Add multiple items in dictionary. 
# --> lecture-110 : Making dynamic dictionary. 


# _______________________________________________________________________________________________________________________ 


# :: Deleting Operation of dictionary - 1 : 

# 1.) Using 'del' keyword . 
# 2.) Using clear() method. 
# 3.) Using pop() method. 
# 4.) Using popitem() method. 
# 5.) Using dictionary comprehension with items(). 













# :--> 1.) Using 'del' Keyword : 

# - This method remove a dictionary item. 
# - Syntax : del dict_name[key]   or    del dict_name





# - Ex : 

# student = {'gabbar' : 20000 , 'thakur' : 15000 , 'basanti' : 14000 , 'viru' : 10000 }
# print('Before delettion : ', student)

# del student

# print('After deletion : ',  student)

# output : Before delettion :  {'gabbar': 20000, 'thakur': 15000, 'basanti': 14000, 'viru': 10000}
# Traceback (most recent call last):
#   File "c:\Users\hp\OneDrive\Desktop\Python\Intermidiate\Lectures\tempCodeRunnerFile.py", line 6, in <module>
#     print('After deletion : ',  student)
#                                 ^^^^^^^
# NameError: name 'student' is not defined





# - Ex : 


# student = {'gabbar' : 20000 , 'thakur' : 15000 , 'basanti' : 14000 , 'viru' : 10000 }
# print('Before delettion : ', student)


# del student['basanti']

# print('After deletion :', student)


# Output : Before delettion :  {'gabbar': 20000, 'thakur': 15000, 'basanti': 14000, 'viru': 10000}
# After deletion : {'gabbar': 20000, 'thakur': 15000, 'viru': 10000}




# NOTE :  It will give an keyError when an key is given to delete which is not exist in the dictionary. 

















# :--> 2. Using clear() method : 

# - Delete all the items from dictionary. 
# - It return empty dictionary. 
# - Syntax : dict_name.clear()



# - Ex : 

# student = {'gabbar' : 20000 , 'thakur' : 15000 , 'basanti' : 14000 , 'viru' : 10000 }
# print('Before delettion : ', student)


# student.clear()

# print('After deletion :', student)


# output : Before delettion :  {'gabbar': 20000, 'thakur': 15000, 'basanti': 14000, 'viru': 10000}
# After deletion : {}





# _______________________________________________________________________________________________________________________ 





# :--> Using pop() method : 

# - Python pop() method can be used to delete a key and a value associated with it. 
# - Syntax : dict_name.pop(key , value [if key not found] )  ,  key is mandatory and value is optional . 
# - It returns the deleted value of the key. 


# - Ex : 

# lottery = {'raj' : 101 , 'jay' : 104 , 'mahesh' : 110} 
# print('before deletion : ' , lottery)  # output : before deletion :  {'raj': 101, 'jay': 104, 'mahesh': 110}

# deleted_value = lottery.pop('jay' , 'not found')
# print('after deletion : ', lottery)  # output : after deletion :  {'raj': 101, 'mahesh': 110}

# print('deleted value is :' , deleted_value)  # output : deleted value is : 104

 





















# :--> popitem() method : 
# - it delete a random key from the dictionary. 
# - It does not take any argument. 
# - it returns the deleted key , value pair in a tuple. 
# - Syntax : dict_name.popitem()

# - Ex:   



# lottery = {'raj' : 101 , 'jay' : 104 , 'mahesh' : 110} 
# print('before deletion : ' , lottery)  # output : before deletion :  {'raj': 101, 'jay': 104, 'mahesh': 110}

# deleted_value = lottery.popitem()
# print('after deletion : ', lottery)  # output :   {'raj': 101, 'jay': 104}
# print('deleted value is :' , deleted_value)  # output : deleted value is :  ('mahesh', 110)

 




# _______________________________________________________________________________________________________________________ 




# :: update in dictionary :

# 1.) Using update() method. 
# 2.) manual programming. 






# 1.) Using update() method :
 
# - it update the key-value pair in existing dictionary. 
# - if key - value is not present than it creates a new entry in the dictionary. 
# - Syntax : dict_name.update({'jay : 30000})

# - Ex:   

# student = { 'raj' : 10000 , 'jay' : 20000}
# print('before updation : ' , student)  # output : before updation :  {'raj': 10000, 'jay': 20000}

# student.update({'jay ': 30000})
# print('after updation : ' , student) #output : after updation :  {'raj': 10000, 'jay': 20000, 'jay ': 30000}














# :-->  Adding multiple items :


# - Ex : 

# student = {'raj' : 10000}
# print('before adding : ' , student)   # output : before adding :  {'raj': 10000}

# student.update({'jay' : 11000 , 'rohan' : 12000 , 'prajwal' : 14000})

# print('after adding : ' , student)  # output :  after adding :  {'raj': 10000, 'jay': 11000, 'rohan': 12000, 'prajwal': 14000}




















# 2.) By Manual Prgramming : 

# - Ex : 

# student = {}

# n = int(input("How many number of students? :"))

# for i in range(n) :
#    roll  = input("Enter roll number of student :")
#    marks = float(input(f"Enter marks of {roll} :"))
#    if roll not in student:
#        student[roll] = marks 
       
#    else:
#        print(f'{roll} number is already present')
       
       
# print('student data is : ', student)
       
       
       
       
       
       
# NOTE : Using while loop to solve logical error.





# student = {}

# n = int(input("How many number of students? :"))

# while len(student)  < n :
#     roll  = input("Enter roll number of student :")
#     marks = float(input(f"Enter marks of {roll} :"))
#     if roll not in student:
#        student[roll] = marks 
       
#     else:
#        print(f'{roll} number is already present')
    
       
# print('student data is : ', student)
       









# _______________________________________________________________________________________________________________________ 




# :: Making Dynamic dictionary : 




# student = {}

# n = int(input("How many number of students? :"))

# while True:
#     roll  = input("Enter roll number of student :")
#     marks = float(input(f"Enter marks of {roll} :"))
#     if roll not in student:
#        student[roll] = marks 
       
#     else:
#        print(f'{roll} number is already present')
    
#     ans = input("Do you want to continue(y/n) : ")
#     if ans != 'y':
#         break
       
# print('student data is : ', student)
       



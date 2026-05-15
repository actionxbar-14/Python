
# :: Youtube Playlist Content : 

# --> lecture-86 : extend() in List in Python.
# --> lecture-87 : insertion in List Python. 
# --> lecture-88 : Remove() Method in List Python. 
# --> lecture-89 : Removing List Contents. 
# --> lecture-90 : 4 Ways to remove duplicates from List. 


# _______________________________________________________________________________________________________________

# :: extend() in List :

# - The extend() method extends by appending all items from iterable , iterable can be list , tuple , set etc. 
# - This method does not return any value rather modifies the list. Means , it returns 'None'. 
# - Syntax : list1.extend(iterable)




# Ex :  without using extend() method (manually) 

# lang1 = ['marathi' , 'hindi' , 'gujrati' , 'urdo']
# lang2 = ['english', 'french' , 'japanese']
# # print(lang1)

# for lang in lang2:
#     lang1.append(lang)
    
# print(lang1)  # output : ['marathi', 'hindi', 'gujrati', 'urdo', 'english', 'french', 'japanese']



# Ex : using extend() method 



# lang1 = ['marathi' , 'hindi' , 'gujrati' , 'urdo']
# lang2 = ['english', 'french' , 'japanese']


# lang1.extend(lang2)


# print(lang1)   # output : ['marathi', 'hindi', 'gujrati', 'urdo', 'english', 'french', 'japanese']




# :--> Interview Question :


# Q1 : what is difference between append() and extend() in list ? 
# Q2 : how will you append multiple elements in list ?







# _______________________________________________________________________________________________________________


# :: Insertion in List by using insert() method :

# - The insert() method insert an element to list at specified index. 
# - Syntax :  list.insert(index , element)

# - element can be of any type. 
# - This methods does not return any value rather modifies the list. Means , it returns 'None'. 



# # - Ex :  

# batsmans = ['rohit', 'dhawan' , 'virat' , 'kl rahul' , 'pandya']
# batsmans.insert(1 , 'dhoni')

# print(batsmans)  # output : ['rohit', 'dhoni', 'dhawan', 'virat', 'kl rahul', 'pandya']





# _______________________________________________________________________________________________________________




# ::  Remove() method in List :

# - removes the first occurrence of the specified element. 
# - Syntax :  list1.remove(element)

# - This methods does not return any value rather modifies the list. Means , it returns 'None'.  


# - Ex :  

# cart = ['mobile' , 'earphone' , 'laptop' , 'microphone' , 'laptop']
# cart.remove('laptop')

# print(cart) # output : ['mobile', 'earphone', 'microphone', 'laptop']



# - Ex : it gives valueError if element given is not in the list


# cart = ['mobile' , 'earphone' , 'laptop' , 'microphone' , 'laptop']
# cart.remove('pendrive')

# print(cart) # output :    cart.remove('pendrive')
# # ValueError: list.remove(x): x not in list





# _______________________________________________________________________________________________________________________




# :: Removing List contents :

# - For removing list contents we use three functions :-

# 1.) pop()
# 2.) clear()
# 3.) del keyword





# 1.)  pop() :
# - This method removes one element from list. 
# - Syntax : listname.pop(index)  [where, index is position of item]. 
# - Pop method returns deleted item for future use. 
# - Index is optional , Default value is -1. 

# - Ex : 






# 2.) clear() :
# - This method removes all items from list. 
# - Syntax : listname.clear() 
# - It does not take any argument. 


# - Ex : 





# 3.) del keyword :
# - It is used to delete the list or list items completly from the memory. 
# - Syntax : del listname / del listname[index] . 


# - Ex : del list element 

# cart = ['mobile' , 'earphone' , 'laptop' , 'microphone']

# del cart[0] #--> 'mobile' 

# print("updated list :", cart)  # output : updated list : ['earphone', 'laptop', 'microphone']





# ____________________________________________________________________________________________________________




# ::  4 - Ways to remove duplicates from list :



# :--> Way - 1 :
# - using set function. 


# - Ex : 

# data = [5 , 10 , 10 , 4 , 3 ,5 , 5, 3, 6]

# removed_duplicated_set = set(data)

# removed_duplicated_list = list(removed_duplicated_set)
# print(removed_duplicated_list)


# NOTE : In this method , order is not preserved. 













# :--> Way - 2 : 
# - Using for loop. 


# - Ex : ( without list comprehension )


# data_list = [5 , 10 , 10 , 4 , 3 ,5 , 5, 3, 6]
# removed_duplicate_list = []

# print("original list :",  data_list)

# for element in data_list :
#     if element not in removed_duplicate_list:
#         removed_duplicate_list.append(element)
        
# print(removed_duplicate_list)



# - Ex : ( with list comprehension )


# data_list = [5 , 10 , 10 , 4 , 3 ,5 , 5, 3, 6]
# removed_duplicate_list = []

# print("original list :",data_list)  #output :  [5, 10, 10, 4, 3, 5, 5, 3, 6]


# [removed_duplicate_list.append(element) for element in data_list if element not in removed_duplicate_list]   # output : [5, 10, 4, 3, 6]



# print(removed_duplicate_list)




# NOTE : order is preserved   , but new list is created. 














# :--> Way - 3 : 
# - Using enumerate() built-in function. 





# - Ex : using enumerate() without list comprehension. 


# data_list = [5 , 10 , 10 , 4 , 3 ,5 , 5, 3, 6]
# removed_duplicate_list = []

# print("original list :",  data_list)

# print(enumerate(data_list))  # output : <enumerate object at 0x0000015268F42F70>


# print(list(enumerate(data_list)))  # output :[(0, 5), (1, 10), (2, 10), (3, 4), (4, 3), (5, 5), (6, 5), (7, 3), (8, 6)]


# for index , element in enumerate(data_list):
#     if element not in data_list[:index]:
#         removed_duplicate_list.append(element)
        
        
# print(removed_duplicate_list)  # output : [5, 10, 4, 3, 6]






# - Ex : Using enumerate() with list comprehension. 



# data_list = [5 , 10 , 10 , 4 , 3 ,5 , 5, 3, 6]
# removed_duplicate_list = []

# print("original list :",  data_list)


# [removed_duplicate_list.append(element) for index, element in enumerate(data_list) if element not in data_list[:index]]


# print(removed_duplicate_list)   # output : [5, 10, 4, 3, 6]












# :--> Way - 4: 
# - Using dictionary concept. 
# - dictionary always contain unique keys. 
# - for ex :
# { '1' : val1 , '1' : val2 } =  {'1' : val2 } [ so iss case mai python only ak hi '1' ko as a key consider krega and uski value ko val2 manega.]



## -->fromkeys() method : it gives  unique keys with value inside an dictionary , if value is not given then it assign none to all keys.



# Ex:  


# data_list = [5 , 10 , 10 , 4 , 3 ,5 , 5, 3, 6]

# print("orginal list :", data_list )

# removed_duplicate_list = list(dict.fromkeys(data_list))   # --> { 5 : none , 10 : None , 4 : None , 3 : None ....}




# print(removed_duplicate_list)  # output  : [5, 10, 4, 3, 6]




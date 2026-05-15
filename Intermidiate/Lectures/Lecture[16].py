
# :: Youtube Playlist Content : 

# --> lecture-81 : len() in Python.
# --> lecture-82 : max() function in Python. 
# --> lecture-83 : min() function in Python. 
# --> lecture-84 : Max and Min in List Python. 
# --> lecture-85 : Append single & Multiple elements. 


# _______________________________________________________________________________________________________________________ 



# :: Length of list : 

# 1.) by len() function :

# Ex:-

# l1 = [12 , 12.3 , 2+3j , 'hello' , [1,2,3]]

# print(len(l1))   # output : 5  
    
    
    
    
# 2.) by manualy writing  :

# Ex :-

# l1 = [12 , 12.3 , 2+3j , 'hello' , [1,2,3]]

# count = 0
 
# for i in l1:
#     count +=1
    
# print(f"length of list : {count}")    # output : 5   
    
    
    
    
# _______________________________________________________________________________________________________________________ 


# :: max() function in Python :

# - To find maximun in list , we use an inbuilt method of list. i.e --> max(). 
# NOTE: for strings as a argument it checks the ascii value of first character. 


# - Syntax : max(iterable , key , default)

# :--> iterable : an iterable such as list. 
# :--> Key (optional) : basic for comparsion. 
# :--> Default : default value is given iterable is empty. 



# - Ex : ( greatest number in list )

# numbers = [3, 2 ,8, 5, 10.8 , 6]
# print(max(numbers))  # output : 10.8



# - Ex : ( getting largest string in a list )

# Name = ['Shantanu' , 'Rohan' , 'Aditya' , 'Zebra']
# print(max(Name))  #--> Zebra ( because 'z' ka ascii value sabse jada hai)



# - Ex : (using key)

# Name = ['Shantanu' , 'Rohan' , 'Aditya' , 'Zebra']
# print(max(Name , key = len)) # output : Shantanu


#NOTE :  ( key  = len ) dene se ascii value ki jagah len jiski jada hai uss
# name ko return kiya.


# - Ex : (using default value)

# Name = []

# print(max(Name, key = len , default = 'Empty'))  # Output : Empty




# _______________________________________________________________________________________________________________________ 
 
 
# :: min() function in Python :

# - To find minimum in list , we use an in-built method of list.  ----> min()
# - Syntax : min(iterable , key , default) . 

# :--> iterable : an iterable such as list. 
# :--> Key (optional) : basic for comparison. 
# :--> Default : default value is given iterable is empty. 




# - Ex : 

# numbers = [40 ,20 , 70 , 45.2 , 16, 31]

# print(min(numbers))  # output : 16


# - Ex : ( using key )

# names = ['shantanu' , 'soham' , 'yuvraj' , 'raj']

# print(min(names))  # output : raj (kyuki r ka ascii value sabse kam hai)




# - Ex : ( using key )

# names = ['shantanu' , 'soham' , 'yuvraj' , 'rajkumar']


# print(min(names, key = len))  # output : soham






# - Ex : (using default value)

# Name = []

# print(min(Name, key = len , default = 'Empty'))  # Output : Empty



# _______________________________________________________________________________________________________________________



# :: Maximum and minimum in List ( manually ) :

# - Ex :  ( max )


# numbers = [45, 78 , 12 , 46, 98 , 66 , 53 , 21, 63 , 87, 89 , 91]


# # max_num = min(numbers)
# # max_num = numbers[0]
# max_num = 0

# for num in numbers:
#     # print(num)
#     if num > max_num:
#         max_num = num
        
# print(max_num)  # output : 98




# - Ex : ( min )


# numbers = [45, 78 , 12 , 46, 98 , 66 , 53 , 21, 63 , 87, 89 , 91]


# min_num = max(numbers)
## min_num = numbers[0]


# for num in numbers:
#     # print(num)
#     if num > min_num:
#         min_num = num
        
# print(min_num)  # output : 12




# _______________________________________________________________________________________________________________________




# :: append() method in list :

# - The append() method adds a single item to list. 
# - It appends an element by modifying list. 
# - Item can be of any type.
# :- Syntax : list.append(item) 

# NOTE:  
# 1.) This methods does not return any value rather modifies the list. Means , it returns 'None'. 
# 2.) It append the value at the end of the list. 




# - Ex :


# bowlers = ['Ishant' , 'bumrah' , 'ashwin']
# bowlers.append('jadeja')

# print(bowlers.append('jadeja'))   # output : None

# print(bowlers)  # output : ['Ishant', 'bumrah', 'ashwin', 'jadeja']



# - Ex : Adding multiple items in list 

# bowlers = []

# for bowler in range(4):
#     bowler_name = input("Enter the name of bowler :")
#     bowlers.append(bowler_name)
    
# print(bowlers)


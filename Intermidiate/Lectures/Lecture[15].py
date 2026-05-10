
# :: Youtube Playlist Content : 

# --> lecture-76 : Printing a table of Entered number.
# --> lecture-77 : Menu Driven Program in Python. 
# --> lecture-78 : What is List in Python. 
# --> lecture-79 : Indexing in List. 
# --> lecture-80 : Operations on List in Python. 


# ___________________________________________________________________________________________________________________________________


# ::  Prnting a table of Entered number :




# while True:
#     input_num = int(input("Enter the num :"))
#     print(f"The table of {input_num} is :")


#     for num in range(1,11):
#        print(f"{input_num} x {num} = {num * input_num}")
      
    
    
#     continue_option = input("Do you want to continue(yes/no) :")
#     if continue_option.lower() == 'no':
#         print("Thanks for using this progam!!")
#         break
    
    




    
    
    




       
    

# ___________________________________________________________________________________________________________________________________




# :: Menu Driven Program in Python :

# - choice based program is called Menu driven program. 

# - Ex : Simple banking system. 


# print("______________SIMPLE BANKING MANAGEMENT_______________")


# while True:
    
#     actual_balance = 12800
#     actual_pin = 1234
#     user_pin = int(input("Enter the ATM pin :"))
    
#     def check_balance():
#         print(f"The current balance is : {actual_balance}rs")
    
    
    
    

#     def withdraw_money():  
#         withdraw_amount = int(input("Enter the amount you want to withdraw :"))
#         actual_balance = 12800
#         print(actual_balance)
#         actual_balance = actual_balance-withdraw_amount
#         print(f"The remaining balance is :{actual_balance}")
        
        
        
    
#     def reset_pin():
#         current_pin = int(input("Entet your current pin :"))
#         actual_pin = 1234
#         if current_pin == actual_pin:
#             new_pin = int(input("Enter new pin : "))
#             actual_pin = new_pin
#             print(f"ATM pin succusssfully changed!")
#         else:
#             print("your current pin does not match actual pin!")
    
    
    
    
#     if user_pin == actual_pin:   
#         print('''
          
#         1. Check balance
#         2. Witdraw money
#         3. Change pin
#         4. Exit
        
#         ''')
        
#         user_choice = input("Enter your choice(1- 4) : ")
        
#         if user_choice == '1':
#             check_balance()
#             break
        
#         if user_choice == '2':
#             withdraw_money()
#             break
                    
            
#         if user_choice == '3':
#             reset_pin()
#             break
        
#         if user_choice == '4':
#             print("Thanks for using ATM system!!")
#             break
        
        
        
        
#     else:
#         print("You Entered wrong pin!!")
#         break



    





# ___________________________________________________________________________________________________________________________________




# :: What is List in Python : 

# - A list is a collection of values or items of different types. 
# - It is ordered collection. 



# :-> Creating list :-

# - The items in list are seperated by (,) comma and inclosed within square brackets [].  
# - Ex : 

# data = [20 , 12.4 , 'india' , 2+5j]
# print(data)

# print(type(data))




# NOTE :  list and array are not same. 



# :--> How to impliment array ? 

# - By using array module. 
# - By using numpy package. 








# ___________________________________________________________________________________________________________________________________



 

# ::  Accessing elements in List :

# - Two ways :-

# 1.) Indexing
# 2.) Slicing


# :->  Indexing : Used to access individual(single) element of list. 
# :->  Slicing  : used to access group of elements of a list. We can access range of elements using slicing. 





# ___________________________________________________________________________________________________________________________________





# ::  Different Operations on list : 


# - Concatenation of lists 
# - Multiplication of lists 
# - Iteration through list 
# - Membership of list 
# - Deletion of list 






# 1.) Concatenation of lists : 

# Ex :  


# l1 = [10 , 20 , 30.4 , 'hello'] 
# l2 = [40 , 50 , 60 , 'bye'] 

# print(l1 + l2)  #-->  [10, 20, 30.4, 'hello', 40, 50, 60, 'bye']


# print(id(l1))    #-->  1888077305088
# print(id(l2))    #-->  1888079805120
# print(id(l1+l2)) #--> 1888079964032






# 2.) Multiplication of list : 

# Ex : 




# l1 = [10 , 20 , 30.4 , 'hello'] 

# print((l1*3))  #--> [10, 20, 30.4, 'hello', 10, 20, 30.4, 'hello', 10, 20, 30.4, 'hello']

# print(id(l1))    #--> 1958041113856
# print(id(l1*3))  #--> 1958041113856








# 3.) Iteration through list :

# Ex : 

# l1 = [10 , 20 , 30.4 , 'hello']

# for item in l1:
#     print(item)

# output :
    
# 10
# 20
# 30.4
# hello




# Ex : 

# l2 = [10 , 20 , 30 , 40]
# for item in l2:
#     print(item+1)


    
# output : 

# 11
# 21
# 31
# 41





# 4.) membership in Python :

# Ex : 


# l1 = [10 , 20 , 30.4 , 'hello']

# if 'hello' in l1:
#     print("present")  #--> present
    
# else:
#     print("not present")




# 5.) deletion of list: 


# Ex : 


# l1 = [10 , 20 , 30.4 , 'hello']

# print(l1)

# del l1 

# print(l1)  #--> 
# NameError: name 'l1' is not defined

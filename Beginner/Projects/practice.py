

# # import  re


# # def check_password_strength(password):

# #     if len(password) < 8 :
# #         return "Weak : Password must contain length atleast 8 character"


# #     if not any(char.isdigit() for char in password):
# #         return "Weak : Password must contain a digit/numeric value"


# #     if not any(char.islower() for char in password):
# #         return "Weak : Password must contain a lower character"


# #     if not any(char.isupper() for char in password):
# #         return "Weak : Password must have a upper character"


# #     if not re.search(r'[!@#$%^&*()<>{}?,.]', password):
# #         return "Medium , Your password should contain an special character"


# #     return "Strong : Your Password is secured"

         




# # def password_checker():

# #     print("Welcome to the Password strength checker , Here You can search the Strength of Your Password:")

# #     while True:

# #         password = input("Enter Your Password or press exit to Quit : ")

# #         if password.lower() == "exit":
# #             print("Thanks for using this tool")
# #             break


# #         result = check_password_strength(password)
# #         print(result)




# # if __name__ == "__main__":
# #     password_checker()

       


 
# import re    




# def check_password_strength(password):
    
#     if len(password) < 8:
#         return " Weak : Password must contain atleat 8 character "

#     if not any(char.isdigit() for char in password):
#         return " Weak : Password must contain a digit/numeric value "


#     if not any(char.islower() for char in password):
#         return " Weak : Password must contain a lower character "

#     if not any(char.isupper() for char in password):
#         return " Weak : Password must contain a upper character "

    
#     if not re.search(r'[!@#$%^&*(){}<>,.?/\]]',password):
#         return " Medium : Password should have an special character "


#     return " Strong : Your Password is secured "



# def password_checker():

#     print("Welcome to the Password Strength Checker , Here You Can Search the Strength Of Your Password")


#     while True:

#         password = input("Enter Your PassWord or (Press exit to quit) :")

#         if password.lower() == 'exit':
#             print("Thnaks for using the tool")
#             break

        
#         result = check_password_strength(password)
#         print(result)





# if __name__ == "__main__":
#     password_checker()

   




   

# WORKFLOW OF THE PROJECT : 

#--> user input between three choices: rock , paper, scissor.
#--> computer choices between three ( randomly ) by random module.


# CASES:

# --> A - Rock

# Rock - Rock = Match tie.
# Rock - Paper = Paper wins.
# Rock - Scissor = Rock wins.


# --> B - Scissor


# Scissor - Scissor = Match tie.
# Scissor - Rock =  Rock wins.
# Scissor - Paper = Scissor wins.



# --> C - Paper 

# Paper - Paper = Match tie.
# Paper - Scissor = Scissor wins.
# Paper - Rock = Paper wins.


import random

item_list = ["Rock" , "Paper" , "Scissor"]

user_choice = input("Enter the choice between : Rock , Paper , Scissor :")
computer_choice =  random.choice(item_list)

print(f"user_choice is : {user_choice} and computer_choice is : {computer_choice}")




if user_choice == computer_choice:
    print("Both Choses Same Options : Match Tied.")


elif user_choice == 'Rock':

    if computer_choice == 'Paper':
        print("Paper Covers Rock : Computer wins")

    else:
        print("Rock smashes the Scissor : You wins")




elif user_choice == 'Paper':

    if computer_choice == 'Scissor':
        print("Scissor cuts the paper : Computer wins")

    else:
        print("Paper Covers Rock : You Wins")



elif user_choice == 'Scissor':

    if computer_choice == 'Rock':
        print("Rock smashes Scissor : computer wins")

    else:
        print("Scissor cuts the paper : You wins")


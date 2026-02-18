

# import  re


# def check_password_strength(password):

#     if len(password) < 8 :
#         return "Weak : Password must contain length atleast 8 character"


#     if not any(char.isdigit() for char in password):
#         return "Weak : Password must contain a digit/numeric value"


#     if not any(char.islower() for char in password):
#         return "Weak : Password must contain a lower character"


#     if not any(char.isupper() for char in password):
#         return "Weak : Password must have a upper character"


#     if not re.search(r'[!@#$%^&*()<>{}?,.]', password):
#         return "Medium , Your password should contain an special character"


#     return "Strong : Your Password is secured"

         




# def password_checker():

#     print("Welcome to the Password strength checker , Here You can search the Strength of Your Password:")

#     while True:

#         password = input("Enter Your Password or press exit to Quit : ")

#         if password.lower() == "exit":
#             print("Thanks for using this tool")
#             break


#         result = check_password_strength(password)
#         print(result)




# if __name__ == "__main__":
#     password_checker()

       


 
        






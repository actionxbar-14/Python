
#                                                     #    PASSWORD STRENGTH CHECKER



# # :: Objective : 

# # - The Objective of this project is to build a Password Strength Checker that evaluates the Strength of user-provided passwords based on common Security criteria. The program helps users create secure passwords by providing feedback on password quality and suggesting imporvements.




# # :: Topics Covered in This Project : 

# # - Function
# # - Conditional statements 
# # - Loops 
# # - Input and output handelling
# # - String Manipulation.
# # - import Library ( Regular Expressions )
# # - Logic Validation









# # ___________________________________________________________________________________________________________________________________________ 




# # :: PASSWORD STRENGTH CHECKER:

import re    # ----> regular expression module



#--> Password strength check conditions:
# - min 8 chars , digit , upperCase , lowerCase , special characters.

def check_password_strength(password):


    # lenght of password
    if len(password) < 8:
        return "Weak : Password must be atleast 8 characters"

    #checking if digit/numerical value is present or not
    if not any(char.isdigit() for char in password):
        return "Weak : Password must contain a digit/numerical value"


    # checking if upperCase is present or not
    if not any(char.isupper() for char in password):
        return "Weak : Password must have an upper character"


    
    
    # checking if lowerCase is present or not
    if not any(char.islower() for char in password):
        return "Weak : Password must have an lower character"



    #checking if special characters are present or not
    if not re.search(r'[!@#$%^&*(){}<>.?,]' ,  password):
        return "Medium : Password must have a speacial character"


    return "Strong : Your password is secured!"





def password_checker():

    print("Welcome , Here You can Check Your strength of password")


    while True:
        password = input("Enter your password (or type 'exit' to quit) : ")

        if password.lower() == 'exit':
            print("Thanks for using this password strength checker!!")
            break


        result = check_password_strength(password)
        print(result)




# Run the password checker function


if __name__ == "__main__":
    password_checker()



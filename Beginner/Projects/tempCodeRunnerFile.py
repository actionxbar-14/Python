


import re


def password_strength_checker(password):

    if len(password) < 8 :
        return " Weak : Password must have length atleast 8 "


    if not any(char.isdigit() for char in password):
        return " Weak : Password must have a digit/numerical value "


    if not any(char.islower() for char in password):
        return " Weak : Password must have a lower character "

  
    if not any(char.isupper() for char in password):
        return " Weak : Password must have a upper character "


    if not re.search(r'[!@#$%^&*()?><,.?]',password):
        return " Medium : Password must have a special characters "


    return " Strong , Your Password is secured "




def password_checker():

    print("Welcome to the Password Strength Checker , Here You can check the Strength of Your Password:")


    while True:

        password = input(" Please Enter Your Password or Press exit or quit to terminate: ")


        if password.lower() == 'exit':
            print("Thanks for Using the tool")
            break


        result = password_strength_checker(password)
        print(result)





if __name__ == "__main__":
    password_checker()

    
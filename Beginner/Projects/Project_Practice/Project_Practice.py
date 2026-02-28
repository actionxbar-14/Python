

# # # import  re


# # # def check_password_strength(password):

# # #     if len(password) < 8 :
# # #         return "Weak : Password must contain length atleast 8 character"


# # #     if not any(char.isdigit() for char in password):
# # #         return "Weak : Password must contain a digit/numeric value"


# # #     if not any(char.islower() for char in password):
# # #         return "Weak : Password must contain a lower character"


# # #     if not any(char.isupper() for char in password):
# # #         return "Weak : Password must have a upper character"


# # #     if not re.search(r'[!@#$%^&*()<>{}?,.]', password):
# # #         return "Medium , Your password should contain an special character"


# # #     return "Strong : Your Password is secured"

         




# # # def password_checker():

# # #     print("Welcome to the Password strength checker , Here You can search the Strength of Your Password:")

# # #     while True:

# # #         password = input("Enter Your Password or press exit to Quit : ")

# # #         if password.lower() == "exit":
# # #             print("Thanks for using this tool")
# # #             break


# # #         result = check_password_strength(password)
# # #         print(result)




# # # if __name__ == "__main__":
# # #     password_checker()

       


 
# # import re    




# # def check_password_strength(password):
    
# #     if len(password) < 8:
# #         return " Weak : Password must contain atleat 8 character "

# #     if not any(char.isdigit() for char in password):
# #         return " Weak : Password must contain a digit/numeric value "


# #     if not any(char.islower() for char in password):
# #         return " Weak : Password must contain a lower character "

# #     if not any(char.isupper() for char in password):
# #         return " Weak : Password must contain a upper character "

    
# #     if not re.search(r'[!@#$%^&*(){}<>,.?/\]]',password):
# #         return " Medium : Password should have an special character "


# #     return " Strong : Your Password is secured "



# # def password_checker():

# #     print("Welcome to the Password Strength Checker , Here You Can Search the Strength Of Your Password")


# #     while True:

# #         password = input("Enter Your PassWord or (Press exit to quit) :")

# #         if password.lower() == 'exit':
# #             print("Thnaks for using the tool")
# #             break

        
# #         result = check_password_strength(password)
# #         print(result)





# # if __name__ == "__main__":
# #     password_checker()

   




   

# # WORKFLOW OF THE PROJECT : 

# #--> user input between three choices: rock , paper, scissor.
# #--> computer choices between three ( randomly ) by random module.


# # CASES:

# # --> A - Rock

# # Rock - Rock = Match tie.
# # Rock - Paper = Paper wins.
# # Rock - Scissor = Rock wins.


# # --> B - Scissor


# # Scissor - Scissor = Match tie.
# # Scissor - Rock =  Rock wins.
# # Scissor - Paper = Scissor wins.



# # --> C - Paper 

# # Paper - Paper = Match tie.
# # Paper - Scissor = Scissor wins.
# # Paper - Rock = Paper wins.


# # import random

# # item_list = ["Rock" , "Paper" , "Scissor"]

# # user_choice = input("Enter the choice between : Rock , Paper , Scissor :")
# # computer_choice =  random.choice(item_list)

# # print(f"user_choice is : {user_choice} and computer_choice is : {computer_choice}")




# # if user_choice == computer_choice:
# #     print("Both Choses Same Options : Match Tied.")


# # elif user_choice == 'Rock':

# #     if computer_choice == 'Paper':
# #         print("Paper Covers Rock : Computer wins")

# #     else:
# #         print("Rock smashes the Scissor : You wins")




# # elif user_choice == 'Paper':

# #     if computer_choice == 'Scissor':
# #         print("Scissor cuts the paper : Computer wins")

# #     else:
# #         print("Paper Covers Rock : You Wins")



# # elif user_choice == 'Scissor':

# #     if computer_choice == 'Rock':
# #         print("Rock smashes Scissor : computer wins")

# #     else:
# #         print("Scissor cuts the paper : You wins")








# print("_______Welcome to the Task Manager App_________")



# def task_manager():
#     task_list = []

#     task_no = int(input("Enter Your total task:"))
#     for i in range(1, task_no+1):
#         task_name = input("Enter the task name:")
#         task_list.append(task_name)

#     print(f"Your today daily tasks are : \n {task_list}")

#     while True:

#         operation = int(input("Enter 1 --> Add \n  Enter 2 --> update \n  Enter 3 --> delete \n  Enter 4 --> View \n  Enter 5 --> Exit/ Terminate : "))


#         if operation == 1:
#             add_task = input("Enter the task you want to add:")
#             task_list.append(add_task)
#             print(f"{add_task} is added succusfully!!")


#         elif operation == 2:
#             update_task = input("Enter the task you want to update:")
#             if update_task in task_list:
#                 new_task = input("Enter the new task:")
#                 task_index = task_list.index(update_task)
#                 task_list[task_index] = new_task
#                 print(f"{new_task} is updated!!")

        
#         elif operation == 3:
#             del_task = input("Enter the task you want to delete:")
#             if del_task in task_list:
#                 del_task_index = task_list.index(del_task)
#                 del task_list[del_task_index]
#                 print(f"{del_task} is deleted!!")


#         elif operation == 4:
#             print(f"Your today tasks are : {task_list}")


#         elif operation == 5:
#             print("Task manager closing. Thanks for using the task manager app!!")


# #         else:
# #             print("invalid input")



# # task_manager()












# print("____Welcome to the Student Management System____")


# student_grades =  { }

# # add student

# def add_student(name , grade):
#     # student_grades['name'] = grade --> ERROR KRA TUNE ISME 
#     student_grades[name] = grade 

#     print(f"{name} is added with grade :{grade}")



# # update student 

# def update_student(name , grade):
#     if name in student_grades:
#         student_grades['name'] = grade

#         print(f"{name} is updated!!")



# # delete student

# def delete_student(name):
#     if name in student_grades:
#         del student_grades['name']

# # display student_grades

# def display_all_students():
#     if student_grades:
#         for name, grade in student_grades.items():
#             print(f"{name} : {grade}")


#     else:
#          print("No students found/added")





# def main():

#     while True:
#         print("1. Add")
#         print("2. Update")
#         print("3. Delete")
#         print("4. View")
#         print("5. Exit")

#         choice = int(input("Enter Your Choice:"))

#         if choice == 1:
#             name = input("Enter the name:")
#             grade = input("Enter the grade:")
#             add_student(name , grade)


#         elif choice == 2:
#             name = input("Enter the name :")
#             grade = input("Enter the grade:")
#             update_student(name, grade)


#         elif choice == 3:
#             name = input("Enter the name:")
#             delete_student(name)


#         elif choice == 4:
#             display_all_students()
          

#         elif choice == 5:
#             print("Closing the program")
#             break 


#         else:
#             print("invalid input")



# main()




import os 


# function to create file

def create_file(filename):
    try:
        with open(filename , 'x') as f:
            print(f"filname : {filename} is created succussfully!")


    except FileExistsError:
        print(f"filname : {filename} already exists!")


    except Exception as E:
        print("an error occured!")



# function to view files in a directory


def view_all_files():
    files = os.listdir()
    
    if not files:
        print(f"file not found")

    else:
        print("files in directory:")
        for file in files:
            print(file)



# function to delete file

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"filename : {filename} is deleted succussfully!")


    except FileNotFoundError:
        print(f"{filename} does not found")


    except Exception as E:
        print("an error occurred!")




# function to edit file

def edit_file(filename):
    try:
        with open(filename , 'x') as f:
            content = input("Enter the text You want to add:")
            file.write(content + "\n")
            print("content added succussfully!")


    except FileNotFoundError:
        print(f"{filename} not found!")

    except Exception as E:
        print("an Error occurred!")




# function to read file

# def read_file(filename):
#     try:
#         with open(filename , 'x') as f:
#             content = f.read()
#             print(f"the content of file is :{filename}")

    
#     except FileNotFoundError:
#         print(f"{filename} not found!")

#     except Exception as E:
#         print("an Error occurred!")









# def main():

#     while True:

#         print("___FILE MANAGER____")

#         print("1. Create File ")
#         print("2. Read File ")
#         print("3. Delete File ")
#         print("4. Edit File ")
#         print("5. View File ")
#         print("6. Exit Program ")



#         choice = input("Enter the task you want to perform ( 1 - 6 ) : ")

#         if choice == '1':
#             filename = input("Enter the file-name you want to create : ")
#             create_file(filename)


#         elif choice == '2':
#             filename = input("Enter the file-name you want to create : ")
#             read_file(filename)


        
#         elif choice == '3':
#             filename = input("Enter the file-name you want to delete : ")
#             delete_file(filename)


        
#         elif choice == '4':
#             filename = input("Enter the file-name you want to edit : ")
#             edit_file(filename)


        
#         elif choice == '5':
#             view_all_files()


#         elif choice == '6':
#             print("Closing the program.....")
#             break


#         else:
#             print("Invalid input")





# main()











   














# """

# Add
# update
# delete
# view
# Exit



# """


# Create a dictinary : 

# student = {
#     'paras' : 100,
#     'Gopal' : 200
# }

# # Accessing a element 

# print(student['paras'])

# # update a element

# student['Gopal'] = 400
# print(student)

# # delete

# del student['paras']
# print(student)








# ____________________________________________________________________________________________________________________________________________________________



student_grades = { }

# Add a new student

def add_student(name,grade):
    student_grades[name] = grade   #----> [sagar] = 100

    print(f"Added {name} with a grade = {grade}")


# Update a student
def update_student(name , grade):
    if name in student_grades:
        student_grades[name] = grade  #----> Sagar = 200

        print(f"{name} with marks are updated {grade}")


    else:
        print(f"{name} is not found")



# Delete a student

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been succussfully deleted")

    else:
        print(f"{name} is not found!")



# Viwe Students

def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")


    else:
         print("No students found/added")





# main logic :


def main():
    
    while True:
        print('\n_________ Student Grades Management System___________')
        print('1. Add Student')
        print('2. Update Student')
        print('3. Delete Student')
        print('4. View Student')
        print('5. Exit')

        choice = int(input("Enter Your choice  = "))



        if choice == 1:
            name = input("Enter student name:")
            grade = int(input("Enter student grade = "))
            add_student(name, grade)


        elif choice == 2:
            name = input("Enter student name :")
            grade = int(input("Enter student grade:"))
            update_student(name , grade)



        elif choice == 3:
            name = input("Enter student name = ")
            delete_student(name)


        elif choice == 4:
            display_all_students()
            # print("No student added")



        elif choice == 5:
            print("Closing the program.....")
            break


        else:
            print("Invalid Choice")






main()
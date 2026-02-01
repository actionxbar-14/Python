
                      # TOPIC : Assignment - 2

#Question 1 : write a program to input student name and marks of 3 subjects and print name and percentage.

# name = input("Enter you name :")
# sub1_maths = input("enter your marks is maths:")
# sub2_science = input("enter your marks is science:")
# sub3_english = input("enter your marks is english:")

# total = (int(sub1_maths)+int(sub2_science)+int(sub3_english)/300*100)
# print(f"name is secured {sub1_maths} is maths and {sub2_science} in science and {sub3_english} in english and total percentage is {total}%")


# name = int(input("Enter you name :"))
# sub1_maths = int(input("enter your marks is maths:"))
# sub2_science = int(input("enter your marks is science:"))
# sub3_english = int(input("enter your marks is english:"))

# total = ((sub1_maths)+(sub2_science)+(sub3_english)/300*100)
# print(f"name is secured {sub1_maths} is maths and {sub2_science} in science and {sub3_english} in english and total percentage is {total}%")




#Question 2 : Writre a Python Program that collects multiple types of data ( e.g ., name , age , height , and student status ) from user input , stores them in a dictionary , and then prints out the collected data? )




# print("Please give you details below :")
# name = input("Enter your name : ")
# age = input("Enter your age : ")
# height = input("Enter your height :")
# student_status = input("Offline / Online:")

# student_record = {
#     "name" : name,
#     "age" : age,
#     "height" : height,
#     "student_status" : student_status
# }
# print(f"the details of the given student named as {name} is {student_record}")






#Another method :


# student_record = {
#     "name" : name,
#     "age" : age,
#     "height" : height,
#     "student_status" : student_status
# }
# print(f"the details of the given student named as {name} is {student_record}")

# student_record = {}

# student_record['name'] = input("Enter your name : ")
# student_record['age'] = int(input("Enter your age : "))
# student_record['height'] = float(input("Enter your height : "))
# student_record['student_status'] = input("Offline / Online : ")


# print(student_record)
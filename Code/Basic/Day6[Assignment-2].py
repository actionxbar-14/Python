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

#another method :

student_record = {}

student_record['name'] = input("Enter your name : ")
student_record['age'] = int(input("Enter your age : "))
student_record['height'] = float(input("Enter your height : "))
student_record['student_status'] = input("Offline / Online : ")


print(student_record)
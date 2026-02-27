
file = open(r"C:\Users\hp\OneDrive\Desktop\PYTHON[ME]\Beginner\Projects\P11_File_Manager\sample.txt" , 'r')

content = file.read()

file.close()
print(f"Content of 'sample.txt' : {content}")


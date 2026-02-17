

# import os
# print(os.getcwd())


# open file

# file = open(r'C:\Users\hp\OneDrive\Desktop\PYTHON[ME]\Beginner\Lectures\Lecture[26]\example.txt', 'r')







# 1. read file : 

# file = open(r'C:\Users\hp\OneDrive\Desktop\PYTHON[ME]\Beginner\Lectures\Lecture[26]\example.txt', 'r')
# content =  file.read()
# print(content)
# file.close()  # Best practice to close afte every work complted.


# file = open(r'C:\Users\hp\OneDrive\Desktop\PYTHON[ME]\Beginner\Lectures\Lecture[26]\example.txt', 'r')

# content = file.readline() # Read first line
# print(content)
# file.close()


# content = file.read() # Read entire line 
# print(content)
# file.close()











# 2. Write file :

# file = open(r'C:\Users\hp\OneDrive\Desktop\PYTHON[ME]\Beginner\Lectures\Lecture[26]\example2.txt', 'w')

# file.write("Namaste!, Kaise ho")  # ye overwrite krr deta hai existing data ko
# file.close()


# :--> append mode:

# file = open(r'C:\Users\hp\OneDrive\Desktop\PYTHON[ME]\Beginner\Lectures\Lecture[26]\example2.txt', 'a')

# file.write("\nAcha hu.\n")  # ye jitni baar run kroge utni bar existing data me add krr deta hai
# file.close()


















# 3. Close a file :   ( Using With Statement )

with open(r'C:\Users\hp\OneDrive\Desktop\PYTHON[ME]\Beginner\Lectures\Lecture[26]\example2.txt', 'r') as file:
    content = file.read()
    print(content)



# output : 

# Namaste!, Kaise hoAcha hu.

# Acha hu.

# Acha hu.
# :: HERE ARE THE ALL POSSIBLE BASIC PATTERN OF MIX NUMBER AND ALPHABET OR STAR ARE PRESENT.



# :: 1 Square pattern:

# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#         j+=1
#     print("  ")
#     i+=1

# Output : 

# * * * * *   
# * * * * *   
# * * * * *   
# * * * * *   
# * * * * * 

# ___________________________________________________________________________

# :: 2 Right Angle Star Pattern:


# n = int(input("enter n:"))
# for i in range(n):
#     for j in range(i):
#           print(" * ", end = " ")
#           j+=1
#     i+=1
#     print("  ")

# output:

# *
# *   *
# *   *   *
# *   *   *   *

# ___________________________________________________________________________



# :: 3 Right Angle Pattern (Alphabet - 1) :

# n = int(input("enter n:"))
# for i in range(n):
#       for j in range(i):
#             print(i , end = " ")
#             j+=1
#       i+=1     
#       print("  ")

# Output:

# 1         
# 2 2       
# 3 3 3     
# 4 4 4 4 
            
# ___________________________________________________________________________



# :: 3 Right Angle Pattern (Alphabet - 2) :


# n = int(input("enter n:"))
# for i in range(n):
#       for j in range(i):
#             # print(j)
#             print(j+1 , end = " ")
#             j+=1
#       i+=1     
#       print("  ")

# Output : 

# 1
# 1 2       
# 1 2 3     
# 1 2 3 4 

# ___________________________________________________________________________



# :: 3 Right Angle Pattern (Alphabet - 3) :

# n = int(input("enter n:"))
# a = 1
# for i in range(n):
#       for j in range(i):
#            print(a , end = " ")
#            a+=1
#            j+=1
#       i+=1
#       print(" ")

# Output : 

# 1
# 2 3
# 4 5 6
# 7 8 9 10
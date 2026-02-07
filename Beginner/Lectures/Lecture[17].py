
                                    # TOPIC : Pattern Printing




# :: HERE ARE THE ALL POSSIBLE BASIC PATTERN OF MIX NUMBER AND ALPHABET OR STAR ARE PRESENT.



# :: 1 Square pattern:


# ----> METHOD 1:
# # n = int(input("enter n:"))
# m = int(input("enter m:"))

# for i in range(m):
#     print("* " * m)
# print()


# ----->  METHOD 2:

# n = int(input("enter n:"))
# # m = int(input("enter m:"))

# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()


# Output : 

# * * * * *   
# * * * * *   
# * * * * *   
# * * * * *   
# * * * * * 

# ___________________________________________________________________________

# :: 2 Right Angle Star Pattern:


# -----> METHOD 1 :

# n = int(input("Enter n:"))
 
# for i in range(n):
#     for j in range(i+1):
#         print("*" , end = " ")
#     print()



# -----> METHOD 2:

# n = int(input("Enter n:"))

# for i in range(n):
#     print("* " * (i+1))
# print()



# output:

# *       
# * *     
# * * *   
# * * * * 
# * * * * *


# ___________________________________________________________________________



# :: 3 Right Angle Pattern (Alphabet - 1) :



# -----> METHOD 1:

# n = int(input("Enter n:"))
 
# for i in range(1,n):
#     for j in range(i):
#         print(i , end = " ")
#     print()




# 1         
# 2 2       
# 3 3 3     
# 4 4 4 4 




# :NOTE  when we place j in print function instead of i then:

n = int(input("Enter n:"))
 
for i in range(1,n):
    for j in range(i):
        print(j , end = " ")
    print()

0 
# 0 1
# 0 1 2
# 0 1 2 3


            
# ___________________________________________________________________________



# :: 4 Right Angle Pattern (Alphabet - 2) :



# n = int(input("enter n:"))

# for i in range(n):
#     for j in range(i):
#         print(j+1,end=" ")
#     print()

# Output : 

# 1
# 1 2       
# 1 2 3     
# 1 2 3 4 

# ___________________________________________________________________________



# :: 5 Right Angle Pattern (Alphabet - 3) :


# n = int(input("enter n:"))
# a = 1

# for i in range(1,n):
#     for j in range(i):
#         print(a,end=" ")
#         a+=1
#     print()





# Output : for n = 5

# 1
# 2 3
# 4 5 6
# 7 8 9 10



# ___________________________________________________________________________


# :: 5 Inverted Right Angle Pattern  :



# n = int(input("Enter n:"))

# for i in range(n):
#     for j in range(n-i):
#         print("*", end = " ")

#     print()




# * * * * * 
# * * * *   
# * * *     
# * *       
# *
# ___________________________________________________________________________


# 6.  Inverted Right Angle Pattern [Alphabet - 1] :

 


# n = int(input("Enter n:"))

# for i in range(1,n+1):
#     for j in range(n-i):
#         print(i, end = " ")

#     print()




# 1 1 1 1
# 2 2 2
# 3 3
# 4



#  ___________________________________________________________________________


# 6.  Inverted Right Angle Pattern [Alphabet - 2] :





# n = int(input("Enter n:"))

# for i in range(n):
#     for j in range(n-i):
#         print(j+1, end = " ")

#     print()


# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# ____________________________________________________________________________



# 7. Equilateral Star Triangle : 

# :: Hint : 2n-1 star in each line  1 then 3 then 5......




# n = int(input("Enter n:"))

# for i in range(1,n+1):
#     print(" " * (n-i) ,end = "")
#     print("*" * (2*i - 1))



#     *
#    ***
#   *****
#  *******
# *********
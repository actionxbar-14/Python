

# name = 'anubhav' 

# print(name * 2) 



n = int(input("enter n:"))

for i in range(n+1):
    for j in range(n-i):
        print('', end = " ")
        
    for k in range(i):
        print('*', end = " ")
        
    print()
   
    
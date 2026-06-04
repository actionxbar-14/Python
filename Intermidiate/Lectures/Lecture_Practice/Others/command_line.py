
# f1 =  open(r'C:\Users\hp\OneDrive\Desktop\Python\Intermidiate\Lectures\Lecture_Practice\Others\one.txt' , mode = 'r')
# f2 =  open(r'C:\Users\hp\OneDrive\Desktop\Python\Intermidiate\Lectures\Lecture_Practice\Others\two.txt' , mode = 'a')


# data = f1.read()
# f2.write(data)

# f1.close()
# f2.close()






# NOTE : We can also use the command line argument. 
# - Ex : 



import sys
f1 =  open(sys.argv[1] , mode = 'r')
f2 =  open(sys.argv[2] , mode = 'a')


data = f1.read()
f2.write(data)

f1.close()
f2.close()
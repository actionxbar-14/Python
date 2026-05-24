ms = [1, 2 ,3 ,4 ,5]
my_dict = {}

for num in nums:
    if num%2 == 0:
        my_dict[num] = num**2
 
print(my_dict)  # output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


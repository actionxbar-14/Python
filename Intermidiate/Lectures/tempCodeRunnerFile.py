nums = [3 , 6 ,8 , 12 , 14 ,15]
sq_num = []

for num in nums:
    if num%2 == 0:
        if num%3 == 0:
             sq_num.append(num*num)

print(sq_num)  # output : [36, 64, 144, 196]

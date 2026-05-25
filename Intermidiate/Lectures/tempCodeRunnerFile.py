
my_str =  "a ,a ,a ,b ,b ,c ,c ,c"  
my_list = my_str.split(',')

visited = []
final_list = []

for ch in my_list:
    if ch not in visited:
        final_list.append(f"{ch} : {my_list.count(ch)}")
        visited.append(ch)
        
print(final_list)
print(", ".join(final_list))
  

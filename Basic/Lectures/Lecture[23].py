
                                                               # TOPIC  :   Assignment - 6 



# ::  Lambda Function : 

# - A Lambda function in Python is a small , anonymous function defined using the lambda keyword. It can have any number of arguments, but only one expression , which is evaluated and returned.

# - Lambda function are often used for short , simple operations without needing to define a full function using def.

# : Syntax : 

# lambda arguments : expression

   # --> arguments : input to the function.
   # --> Expression : A single statement or operation that the lamda function.


# - Example : 

# 1. Add two numbers using a regular function : 

# def add(x , y):
#     return x + y

  
   
# print(add(3,5))   # Output : 8



# 2.  Add two numbers using a lambda function : 

# add = lambda x , y : x + y
# print(add(3,5))     # Output : 8



# 3.  Custom Sorting : Sort a list of tuples by second element : 

# data = [(1,'b') , (2,'a') , (3,'c')]

# sorted_data = sorted(data , key = lambda x : x[1])

# print(sorted_data)   # output : [ (3,'a'), (1,'b'), (2,'c') ]







# _______________________________________________________________________________________________________________________










# :: Questions :  


# 1. Find the Intersection ( common elements ) of Two Lists.
# 2. Find the Most Frequent Element in a List.
# 3. Find Cummulative Sum of a List.
# 4. Remove Duplicates from a List.
# 5. Find the index of an Element in a tuple.
# 6. Find the Most Frequent Value in a dictionary.
# 7. Merge Dictionaries with Summation.
# 8. Flatten a Nested Dictionary.
# 9. Sort a Dictionary by Values.
# 10. Access values from a nested dictionary.







# Question : 1  Find the Intersection ( common elements ) of Two Lists.

# Answer  : 

# :--> Method 1: converting list into set() using typecasting and applying set intersection method then again convert it into list by list() method.

# List_1 = set([1,2,4,5])
# List_2 = set([2,4,6,7])

# common_elements = list(List_1 & List_2)
# print(common_elements)   # Output : [2, 4]



# :--> Method 2 :  using for loop

# List_1 = [1,2,4,5]
# List_2 = [2,4,6,7]

# def intersection_loop(lst1,lst2):
#    common_list = []
#    for item in lst1:
#       if item in lst2 and item not in common_list:
#          common_list.append(item)

#    return common_list


# print(intersection_loop(List_1,List_2))    # Output : [2, 4]
   



# :--> Method 3 : using List Comprehension

# List_1 = [1,2,4,5]
# List_2 = [2,4,6,7]


# def intersection_Comp(lst1,lst2):
#    return [item for item in lst1 if item in lst2]


# common_list = intersection_Comp(List_1,List_2)
# print(common_list)   # Output : [2, 4]



























# Question : 2   Find the Most Frequent Element in a List.

# Answer  : 

# my_list = []
# num = int(input("Enter How many numbers you want in your list:"))
# for i in range(1,num+1):
#        List_item = int(input(f"enter List Element {i}:"))
#        my_list.append(List_item)




# def Frequent_element(lst):
     
#    max_count = 0
#    most_frequent = None
#    for item in lst:
#       count = lst.count(item)
#       if count > max_count:
#          max_count = count 
#          most_frequent = item

#    return most_frequent


# FreqElem_list = Frequent_element(my_list)
# print(f"The most frequent Element is:{FreqElem_list}") 


























# Question : 3  Find Cummulative Sum of a List.

# Answer :  Cummulative sum like 1+2 = 3, then 3+3 = 6 , then 6+4 = 10. 
# -->for list [1,2,3,4].
# 1

# 1+2 = 3

# 1+2+3 = 6

# 1+2+3+4 = 10







# ----> Method 1 : 

# numbers = [1,2,3,4]

# def Cummulative_sum(lst):
#    CummSum_result = []
#    total = 0
#    for num in lst:
#      total += num
#      CummSum_result.append(total)
#    return CummSum_result

# print(Cummulative_sum(numbers))  # Output : [1, 3, 6, 10]




# ----> Method 2 : 


# numbers = [1,2,3,4]

# Cummulative_sum = [sum(numbers[:i+1]) for i in range(len(numbers))]

# print(Cummulative_sum)    # Output : [1, 3, 6, 10]


































# Question : 4  Remove Duplicates from a List 

# Answer:



# :--> Method 1 : 

# fruits = ["apple" ,"banana","cherry","banana"]
# print(fruits)

# def remove_duplicates(lst):
#    unique = []
#    seen  = set()
#    for item in lst:
#       if item  not in seen:
#          unique.append(item)
#          seen.add(item)
      
#    return unique


# print(f"After removing duplicates : {remove_duplicates(fruits)}")





#NOTE: we can also do this without seen methon. for ex:



# fruits = ["apple" ,"banana","cherry","banana"]
# print(fruits)

# def remove_duplicates(lst):
#    unique = []
#    for item in lst:
#       if item not in unique:
#          unique.append(item)
         
      
#    return unique


# print(f"After removing duplicates : {remove_duplicates(fruits)}")




# :: Conclusion : set( ) is fastly executed then the list , that's why for the large data we assign all values of list into set.






# --->  Method 2:  Using Set Constructor.


# fruits = ["apple" ,"banana","cherry","banana"]
 
# print(list(set(fruits)))   # output : ['banana', 'apple', 'cherry']































# Question : 5 Find the index of an Element in a tuple.

# Answer:


# my_tuple = (1,2,3,4)

# def Find_index(tup , elem):
#    return tup.index(elem) if elem in tup else print("No. not present in tuple")



# print(Find_index(my_tuple,2))  # Output : 1
# print(Find_index(my_tuple,0))  # Output : No. not present in tuple
#                                         # None


























# Question : 6    Find the Most Frequent Value in a dictionary.

# Answer : 


# data = {
#    'a' : 1,
#    'b' : 2,
#    'c' : 1,
#    'd' : 3,
#    'e' : 1
# }



# def most_freq(dct):
#    frequency = {}
#    for value in dct.values():
#       if value not in frequency:
#          frequency[value] = 0
      
#       frequency[value] += 1

#    max_value = max(frequency , key = frequency.get)
#    return max_value



# print(most_freq(data))   # Output : 1




















































# Question : 7  Merge Dictionaries with Summation.

# Answer:

# dict1 = { 'a' : 10, 'b': 20 , 'c' : 30}
# dict2 = { 'b' : 15, 'c': 35 , 'd' : 25}

# def merge_dict(dict1 , dict2):
#    result = dict1.copy()
#    for key,value in dict2.items():

#       if key in result:
#          result[key] += value

#       else:
#          result[key] = value

#    return result



# print(merge_dict(dict1,dict2))    # Output : {'a': 10, 'b': 35, 'c': 65, 'd': 25}















































# Question 8 : Flatten a Nested Dictionary.

# Answer :

# data = { 'a' : {'b' :{'c': 42 } , 'd' : 7 } , 'e' : 10 }

# # We want output as :  {a.b.c : 42 , a.d : 7 , e : 10}



# def flatten_dict(data, parent_key = '', sep = '.'):
#    items = {}  # initialize empty dict to store flattened items

#    for key , value in data.items():
        # combine current key with parent key
#       new_key = f"{parent_key}{sep}{key}" if parent_key else key 

#       if isinstance(value , dict):    # check if value converted into dict or not
#          items.update(flatten_dict(value, new_key, sep))   # recursive flatten the nested dict

#       else:
           # adding key-value to flatten dict
#          items[new_key] = value

#    return items 

# print(flatten_dict(data))   # Output : {'a.b.c': 42, 'a.d': 7, 'e': 10}


































#  Question : 9 Sort a Dictionary by Values.

# Answer:

# :-  ASCENDING ORDER :

# data = { 'a' : 5 , 'b'  : 9 , 'c'  : 2 , 'd'  : 7}
 
# print(data.items())   # Output : dict_items([('a', 5), ('b', 9), ('c', 2), ('d', 7)])

# def sort_by_values(data):
#    sorted_items = sorted(data.items() , key = lambda item: item[1])

#    return {key:value for key , value in sorted_items}





# print(sort_by_values(data))   # Output : {'c': 2, 'a': 5, 'd': 7, 'b': 9}




# :-  DESCENDING ORDER :

# def sort_by_values(data):
#    sorted_items = sorted(data.items() , key = lambda item: item[1], reverse = True)

#    return {key:value for key , value in sorted_items}


# print(sort_by_values(data))   # Output : {'b': 9, 'd': 7, 'a': 5, 'c': 2}












# Question : 10  Access values from a nested dictionary.

# Answer : 


data = {
   "level1" : {
      "level2" : {
         "level3" : {
            "value1" : 10,
            "value2" : [1 , 2 , {"deep_key" : 42}],
            "value3" : {"inner_key" : "target"}
         },
         "other_key" : 99
      },
      "list_key" : [
         {"list_inner_key1" : 88},
         {"list_inner_key2" : {"deep_list_key": 77}}
      ]
   }
}



print(data["level1"]["level2"]["level3"]["value2"][2]["deep_key"])  # Output : 42

print(data["level1"]["level2"]["level3"]["value3"]["inner_key"])  # Output : target

print(data["level1"]["list_key"][1]["list_inner_key2"]["deep_list_key"])  # Output : 77


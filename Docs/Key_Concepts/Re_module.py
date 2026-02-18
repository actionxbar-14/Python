



# Resource : https://chatgpt.com/share/699568ba-7d24-800c-90a4-2451c5f9977e






# ::Regular Expressions Module :

# - Regular expression ek pattern hota hai jo text me match karta hai.

# Example:

# 1.Email check karna

# 2.Phone number validate karna

# 3.Kisi sentence me numbers dhundhna

# 4.Password rule check karna





# :: Three methods of re:


# 1. search
# 2. findall
# 3. match









# ___________________________________________________________________________________________________________________________________________





# 1. re.search() → Pattern dhundhne ke liye

# # Ex:


# import re

# text = "My number is 9876543210"
# result = re.search(r"\d+", text)

# print(result.group())


# Output:

# 9876543210


# :--->Explanation:

# \d = digit

# + = ek ya zyada digits

# r"" = raw string (regex me important hota hai)












# 2. re.findall() → Sab matches ki list.



# # Ex:



# import re

# text = "There are 12 apples and 30 mangoes"
# numbers = re.findall(r"\d+", text)

# print(numbers)


# Output:

# ['12', '30']














# 3. re.match() → Sirf beginning check karta hai



# # Ex: 


# import re

# text = "Hello World"
# result = re.match(r"Hello", text)

# print(result.group())


# Ye sirf tab kaam karega jab pattern starting me ho.





# ___________________________________________________________________________________________________________________________________________




# :--->Common Regex Symbols (Beginner Level):


# Symbol	                                   Meaning
# \d	                                    digit (0–9)
# \D                                     	non-digit
# \w                              	word character (a-z, A-Z, 0-9, _)
# \s	                                     space
# .	                                koi bhi character
# +	                                 1 ya zyada
# *	                                 0 ya zyada
# ^	                                   start
# $	                                    end

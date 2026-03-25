
                       #  TOPIC :       Strings[ Part - 2 ]
                          #       [ Indexing , Slicing , Methods ]
                        




# :: String Indexing : 

# - You can access individual characters in a string using their index. Python uses Zero-based indexing , meaning the first character has an index of 0.
# Index : Position of the character.

# syntax : string[index_value]

# Example :  

# name = "Anubhav"

# name[0] , name[-7] = 'A'
# name[1] , name[-6] = 'n'
# name[2] , name[-5] = 'u'
# name[3] , name[-4] = 'b'
# name[4] , name[-3] = 'h'
# name[5] , name[-2] = 'a'
# name[6] , name[-1] = 'v'
# print(name)  # Output : Anubhav

# print(name)  # Output : Anubhav





#NOTE : Space are also counted as a index by the string indexing.

# Ex:
# name = "Anubhav "
# print(name[-1]) #output : <blanck space>
















# :: String Slicing :-

# - Slicing in Python is a feature that enables accesssing parts of the sequence. String Slicing allow you to get 'subset' of characters from a string using a specified range of indices.

# syntax : string[start : end  : step]

# --> start :- The index to start Slicing(inclusive). Default value is 0.
# --> end :- The index to stop Slicing(exclusive). Default value is length of string.
# --> Step :- How much to incriment the index after each character. Default value is 1.

# Ex:
    #   A   N   U   B   H   A   V 
    #   0   1   2   3   4   5   6   

# name = "Anubhav"
# print(name[0:4]) #output : Anubh ( h -> exclusive) : Anub.

# print(name[0:6:2]) #output : Auh(v -> exclusive, jump by 2 index.)


# Ex:

# name = "Anubhav"
# # nick_name = name[0:3] #output : Anu
# print(f"My name is {name} and people genrally call me as {nick_name}")  #output : My name is Anubhav and people 
# genrally call me as Anu  



# print(name[5:]) #output : [v] last letter.
# print(name[-1:]) #output : [v] last letter.
# print(name[-2:]) #output :[av] last 2 char.
# print(name[-3:]) #output : [hav] last 3 char.
# print(name[0:5:2]) #Output : [Auhv] every second char.
# print(name[0::2]) #Output : [Auhv] every second char.
# print(name[:]) / print(name[::]) #output : [Anubhav] all characters.
# print(name[::-1]) #output : [vahbunA] reversing the string.























#:: String Methods :-

# 1. len() : returns the length of a string(the number of characters).
# ex:

# name = "Anubhav"
# print(name) #output : Anubhav
# print(len(name)) #output : 7


# 2. upper() : Converts a string into upper case.
# ex:

# name = "Anubhav"
# Capital_name = name.upper()
# print(Capital_name)  #output: ANUBHAV


# 3. lower() : Converts a string into lower case.
# ex:

# name = "ANUBHAV"
# lower_name = name.lower()
# print(lower_name)  #output: anubhav


# 4. strip() : Removes any landing and trailing whitespace(including spaces ,tabs,or newline characters).
# ex:

# name = "  Anubhav  "
# print(name.strip()) #output :  Anubhav



# 5. count() : Returns the number of times a specified value occour in a string.
# ex:

# name = "Anubhav"
# a_occour = name.count('a')
# print(a_occour) #output : 2


# 6. find() : Searches the string for a specified value and returns the Position of where it was.
# ex:

# name = "Anubhav"
# print(name.find('u')) #output : 3


# 7. title() : Converts the first character of each word to upper case.
# ex:

# name = "anubhav"
# Capital_name = name.title()
# print(Capital_name)  #output: Anubhav



# 8. split(): Splits the string at the specified separator and returns a list.

# name = "Hello Anubhav"
# split_name = name.split(',')
# print(split_name)  #output : ['Hello Anubhav']



# 9. replace(old, new) : Replace all occurrences of a substring with a new substring.
# ex:

# name = "Anubhav"
# replace_name = name.replace('A', 'a')
# print(replace_name)  #output : anubhav


# 10. Join() :
# This function is used to join the elements of a list into a string.

# words = ("Anubhav" , "is" , "Great")
# print(" ".join(words))  #output : Anubhav is Great
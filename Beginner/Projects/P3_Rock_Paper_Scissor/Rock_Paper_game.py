
                                                                 # Rock Paper Scissor



# ::  WORKFLOW OF PROJECT :

# 1. Input from user(Rock , Paper , Scissor).
# 2. Computer choice ( Computer will choose randomly not conditionally ).
# 3. Result print 



# :--> Cases :




# A - Rock :-

# Rock - Rock = tie
# Rock - Paper = Paper Win
# Rock - Scissor = Rock Win




# B - Paper :-

# Paper - Paper = tie 
# Paper - Rock = Paper Win 
# Paper - Scissor = Scissor Win 




# C - Scissor :-

# Scissor - Scissor =  tie 
# Scissor - Rock =  Rock Win
# Scissor - Paper = Scissor Win




import random 


item_list = ["Rock" , "Paper" , "Scissor"]

user_choice = input("Enter Your move = Rock , Paper , Scissor  : ")
computer_choice = random.choice(item_list)

print(f" User Choice is : {user_choice} and computer_choice is : {computer_choice}")



if user_choice == computer_choice:
    print(f"Both chooses same : = Match tie")




elif user_choice == 'Rock':
    if computer_choice == 'Paper':
        print("Paper Covers Rock : Computer Wins")

    else:
        print("Rock Smashes Scissor : You Win")





elif user_choice == 'Paper':
    if computer_choice == 'Scissor':
        print("Scissor cuts paper : Computer wins")

    else:
        print("paper covers the rock : You win")





elif user_choice == 'Scissor':
    if computer_choice == 'Paper':
        print("Scissor Cuts the paper: You Win")

    else:
        print("Rock smashes the scissor : Computer wins")
    
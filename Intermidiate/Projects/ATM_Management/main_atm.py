

import time


print("-" * 15 ,'ATM MANAGEMENT SYSTEM', "-" * 15)


class ATM_MANAGEMENT:
    # USER_PIN = 1234
    # USER_BALANCE = 12800



    def __init__(self):
        self.USER_PIN = 1234
        self.USER_BALANCE = 12800


    def __call__(self, *args, **kwds):
        pass

        

    def Balance_Inquiry(self):
        print(f"Fetching Your Current Account Balance!  ")
        time.sleep(1)
        print(f"Your Current Bank balance is :{self.USER_BALANCE}")


    def Cash_Withdrawal(self):
        withdrawel_input = int(input("Enter Amount to Withdraw :"))
        self.USER_BALANCE = self.USER_BALANCE - withdrawel_input
        print(f"{withdrawel_input}rs is Successfully debited!")
        time.sleep(0.5)
        print(f"Current balance is : , {self.USER_BALANCE}")

    def Deposit_Money(self):
        Add_Amount = int(input("Enter Amount to Add :"))
        self.USER_BALANCE = self.USER_BALANCE + Add_Amount
        print(f"{Add_Amount}rs is Successfully Added!")
        time.sleep(0.5)
        print(f"Current balance is : , {self.USER_BALANCE}rs")


    def Change_PIN(self):
        input_pin = int(input("Enter your Current pin :"))
        if input_pin ==  self.USER_PIN:
            new_pin = int(input("Enter your new pin :"))
            self.USER_PIN = new_pin
            print(f"PIn Successfully changed!!")
        else:
            A1()





A1 = ATM_MANAGEMENT()




while True:
    USER_PIN = 1234
    USER_BALANCE = 12800
            
    input_pin = int(input("Enter Your 4-digit PIN :"))
    if input_pin == USER_PIN:

        USER_CHOICE = int(input('''
            Enter Your Choice :
            1.  Balance Inquiry
            2.  Cash Withdrawal
            3.  Deposit Money
            4.  Change PIN 
         ''' ))

        if USER_CHOICE == 1:
            A1.Balance_Inquiry()

        elif USER_CHOICE == 2:
           A1.Cash_Withdrawal()
        #    print(f" Rs. {}")

        elif USER_CHOICE == 3:
           A1.Deposit_Money()

        elif USER_CHOICE == 4:
            A1.Change_PIN()



    else:
        print("You Entered Wrong PIN!!")
        A1()



        
    ans = input("Press 'X' to exit! , 'Y' to Continue :")
    if ans.lower() == 'y':
       A1()
    elif ans.lower() == 'x':
       print("Thanks For Using the ATM MANAGEMENT SYSTEM!!")
       break      
    else:
        print("Invalid Input") 
                
     





        


























       

    
     
#James Dumitru
#ITM 313

import getpass
import sys

account_balance=float(0.00) #Starting balance is 0, you have to deposit money, so go crazy.
interest=float(0.01)
#exit
def exit(): # If you exit, it will display interest accrued, and automatically added into account.
    print("Thank You!\n Have A Nice Day!\n Total Interest: $%.2f\n Your New Balance: $%.2f" % (calculate_interest(), account_balance+calculate_interest()))
    sys.exit() 
#interest attempt
def calculate_interest():
    global account_balance
    return account_balance * interest
#Withdraw
def withdraw():
    global account_balance
    withdrawl_amount=float(input("Please Enter The Amount You Would Like To Withdraw: "))
    if withdrawl_amount<0:
        print("No Negative Numbers Allowed!")
        menu()
    elif withdrawl_amount>account_balance:
        print("Not Enough! Check Your Balance Again!")
        menu()
    else:
        account_balance = account_balance - withdrawl_amount
        print("Witdraw Amount: $%.2f\nTotal Balance: $%.2f" % (withdrawl_amount,account_balance))
        menu()
#Deposit
def deposit():
    global account_balance
    deposit_amount=float(input("Please Enter The Amount You Want To Deposit: "))
    if deposit_amount<0:
        print("No Negative Numbers Allowed!")
        menu()
    else:
        account_balance = account_balance + deposit_amount
        print("Amount Deposited: $%.2f\n *** New Balance: $%.2f ***" % (deposit_amount,account_balance))
        menu()
#Login
def login():
    username=str(input("Please Enter Your Username: ")) #pick a username
    password=getpass.getpass("Please Enter Your Password: ") #pick a password
    if password==password: #if you have a password and want to check error, change to "password" and test it. It will say error if not "password". 
        print("Hello %s!\n*** Your Current Account Balance is: $%.2f ***\n Total Interest: $%.2f\n" % (username,account_balance,calculate_interest()))
        menu()
    #error check
    else:
        print("wrong password try again") #wrong password, try again
        login()
#Navigation Menu
def menu():
    global account_balance
    choice=input("What Do You Want To Today?\n1. Withdraw From My Account.\n2. Deposit Into My Account.\n3. Exit The Menu.\n")
    if choice == "1":
        withdraw()      #withdraw money
    if choice == "2":
        deposit()       #deposit money
    #if choice == "3":
        #calculate_interest()     # The interest is displayed at the end of the code when you exit, it will say total interest along with total balance.
    else:
        exit() #if choose a different number than menu option, program ends.
#call.py file is needed to run this code!
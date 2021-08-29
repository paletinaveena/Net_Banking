# loading the dataset
#synthetic dataset

import pandas as pd
df=pd.read_csv('bank-details.csv')

df.index = df.index + 1

df

# checking the length of the dataframe
len(df)

#creating a list to store a particular attribute value after converting it to lower case 

df_name=[]
df_acco=[]
df_pin=[]
df_name=df.Name.str.lower()
df_acco=df.Account_no.str.lower()
df_pin=df.Pin

def checkName(name: str, j: int) -> bool:
    if name == df_name.iloc[j]:
        return True
    return False

def checkAcc(acc_num: str, j: int) -> bool:
    if acc_num == df_acco.iloc[j]:
        return True
    return False

def checkPin(pin: int, j: int) -> bool:
    if pin == df_pin.iloc[j]:
        return True
    return False

def check(detail, i):
    for j in range(0, len(df)):
        if i == 0:
            if checkName(detail, j):
                return j
        if i == 1:
            if checkAcc(detail, j):
                return j
        if i == 2:
            if checkPin(detail, j):
                return j
    return False

#Recursive function to input the username and to check if the entry is present in the dataset or not.

def details():
    while True:
        name = input("Enter your Name:")
        if check(name.lower(), i = 0) is not False:
            print("\033[1m  NAME VALIDATED\n" + "\033[0m")
            p1 = check(name.lower(), i = 0)
            account_num = input("Enter your Account Number:")
            if check(account_num.lower(), i = 1) is not False:
                print("\033[1m  ACCOUNT NUMBER VALIDATED\n" + "\033[0m")
                p2 = check(account_num.lower(), i = 1)
                pin = int(input("Enter your Pin Number:"))
                if check(pin, i = 2) is not False:
                    print("\033[1m  PIN NUMBER VALIDATED\n" + "\033[0m")
                    p3 = check(pin, i = 2)
                    if p1 == p2 and p2 == p3:
                        return p1
                    else:
                        print("\033[1m  INVALID Details\n" + "\033[0m")
                else:
                    print("\033[1m  INVALID PIN NUMBER\n" + "\033[0m")
            else:
                print("\033[1m  INVALID ACCOUNT NUMBER\n" + "\033[0m")
        else:
            print("\033[1m  INVALID USERNAME\n" + "\033[0m")
            
def checkLength(phone_number: str) -> bool:
    if len(phone_number) == 10:
        return True
    return False

import random
def checkOTP():
    rand=random.randrange(1000,10000)
    print("\033[0;30mAn OTP from CACHE BANK:", rand)
    OTP = int(input("Enter the OTP received to check for authentication :"))
    if rand == OTP:
        print("\033[0;31m \t\t\t\t\t\t ACCESS GRANTED " +"\033[0;30m")
        return
    else:
        print("\033[0;31m \t\t\t\tINCORRECT OTP..TIME LAPSED..NEED TO LOGIN AGAIN" +"\033[0;30m")
        
#recursive function to input the phone number and to check if its valid combination or not.

def checkPhoneNumber():
    while True:
        phone_number=input("Enter you Phone Number : ")
        if checkLength(phone_number):
            print("\033[0;31m \t\t\t\t\t CAN PROCEED TO NEXT STEP\n\n" +"\033[0;30m")
            if checkOTP():
                print("\033[1m  PHONE NUMBER IS VALID\n"+ "\033[0m")
                return 
            return
        else:
            print("\033[1m  PERMISSION NOT GRANTED ...PLEASE RE-ENTER THE PHONE NUMBER\n" + "\033[0m")

def Verification():
    print("\033[0;30mx"*127)
    print("\033[1m \033[34m \033[4m \t\t\t\t\t\t\t CACHE BANK" +"\033[1m \033[34m \033[4m")
    print("\033[0;30mx"*127)
    print("\n")
    p = details()
    checkPhoneNumber()
    print("\n")
    print("\033[0;30mx"*127)
    return p

p = Verification() + 1

# to display date n time

import datetime
now=datetime.datetime.now()

def Menu():
    print("1. Credit Denomination\n2. Debit Denominaton\n3. Change your PIN\n4. Mini Statement\n5. Quit")
    
def credit(credit_amt):
    if credit_amt > 0:
        df.at[p, 'Balance'] += credit_amt
        amt = df.loc[p,'Balance']
        df.loc[p,'Balance'] = amt
        df.to_csv("bank-details.csv")
        print("Your amount has been successfully deposited to your account")
        print("Your current balance is:")
        print("Balance : " , df.loc[p]['Balance'])
        print("\033[1mThanks for using CACHE BANK" +"\033[1m")
    else:
        print("\033[1mIvalid amount to proceed...Operation Unsuccessful" +"\033[1m")
     
def debit(debit_amt):
    if debit_amt < (df.iloc[p]['Balance']):
        print("Collect your cash!")
        df.at[p,'Balance'] -= debit_amt
        amt = df.loc[p,'Balance']
        df.loc[p,'Balance'] = amt
        df.to_csv("bank-details.csv")
        print("Your current balance is:")
        print("Balance : " , df.loc[p]['Balance'])
        print("\033[1mThanks for using CACHE BANK" +"\033[1m")
    else:
        print("\033[1mNo sufficient balance...Operation Failed" +"\033[1m")
        
def changePin():
    print("\n"+"\033[0;30mx"*127)
    change_pin = input("\033[1mEnter new PIN here : " +"\033[1m");
    length = len(change_pin) 
    if length == 4:
        print("\033[1mYour PIN has been successfully changed..! " +"\033[1m")
        print("New PIN: "+change_pin)
        df.loc[p,'Pin'] = change_pin
        df.to_csv("bank-details.csv")
        print("\033[1mThanks for using CACHE BANK" +"\033[1m")
    else:
        print("\033[1mIvalid PIN to proceed....Operation Failed" +"\033[1m ")
        
def miniStatement():
    print("\033[1mDate and Time : " +"\033[1m " +now.strftime('%d - %m - %y %H:%M:%S'))
    print("\n"+"\033[0;30mx"*127)
    print("\033[1mPlease collect your mini statement" +"\033[1m ")
    print(df.loc[p])        
    print("\033[1mThanks for using CACHE BANK" +"\033[1m ")
    
#Net-Banking operations(credit,debit,to change PIN, to check balance and to quit)

print("\033[0;30mx"*127)
print("\033[1m \033[34m \033[4m \t\t\t\t\t\t\t CACHE BANK" +"\033[1m \033[34m \033[4m")
print("\033[0;30mx"*127)

def operations():
    while True:
        Menu()
        ch = int(input("\033[1m Select Operation:" +"\033[1m"))
        if ch == 1:
            print("\n"+"\033[0;30mx"*127)
            print("\033[1mBalance : "+"\033[1m" , df.loc[p]['Balance'])
            credit_amt = int(input("Enter your amount to be credited: " +"\033[1m"))
            credit(credit_amt)
            print("\n"+"\033[0;30mx"*127)
        elif ch == 2:
            print("\n"+"\033[0;30mx"*127)
            print("\033[1mBalance : " +"\033[1m", df.loc[p]['Balance'])
            debit_amt = int(input("Enter your amount to proceed:"))
            debit(debit_amt)
            print("\n"+"\033[0;30mx"*127)
        elif ch == 3:
            print("\n"+"\033[0;30mx"*127)
            changePin()
            Verification()
            print("\n"+"\033[0;30mx"*127)
        elif ch == 4:
            print("\n"+"\033[0;30mx"*127)
            miniStatement()
            print("\n"+"\033[0;30mx"*127)
        elif ch == 5:
            print("\n"+"\033[0;30mx"*127)
            quit1 = input("\033[1mPress Y to quit...!" +"\033[1m ")
            if quit1 == "Y":
                print("Quit")
                return
            else:
                print("\033[1mChoose any transaction please:"+"\033[1m ")
            print("\n"+"\033[0;30mx"*127)
        else:
            print("\033[1mInvalid Input" +"\033[1m ")
            return
operations()

df

## Data Analysis

#### Analysis of users, according to Branch wise

import seaborn as sns 
sns.countplot(x = 'Branch_no', data = df)

#### Analysis of users, on Gender and Branch no

sns.lineplot(x="Gender", y="Branch_no", data = df)

#### Analysis of users, on Gender basis

sns.countplot(x = 'Gender', data = df)

#### Analysis of users, on Gender and Age

sns.stripplot(x='Gender', y='Age', data=df)

# loading the dataset
#synthetic dataset

import pandas as pd
df=pd.read_csv('bank-details.csv')
df

#unique attriute

df["Name"]

#creating a list to store a particular attribute value after converting it to lower case 

name=[]
acco=[]
pin=[]
name=df.Name.str.lower()
acco=df.Account_no.str.lower()
pin=df.Pin

#checking the type of the list created

#name=name.values.tolist()
type(name)

#Recursive function to input the username and to check if the entry is present in the dataset or not.

def na():
    c=0
    nam=input("Enter your Name :")
    nam=nam.lower()
    f=False
    for i in range(0,len(name)):    
        if nam== name.iloc[i]:
            c=i
            f=True
            break
    if f:
        print("\033[1m  NAME VALIDATED\n" + "\033[0m")
        return c
    else:
        print("\033[1m  INVALID USERNAME\n" + "\033[0m")
        na()

c=na()

#storing the index number in 'p1'

p1=c

#Recursive function to input the account number and to check if the entry is present in the dataset or not.

def account():
    co=0
    acc=input("Enter your Account Number :")
    acc=acc.lower()
    f=False
    for i in range(0,len(acco)):    
        if acc==acco.iloc[i]:
            co=i
            f=True
            break
    if f:
        print("\033[1m  ACCOUNT NUMBER VALIDATED\n" + "\033[0m")
        return co
    else:
        print("\033[1m  INVALID ACCOUNT NUMBER\n" + "\033[0m")
        account()
co=account()

#storing the index number in 'p2'

p2=co

#Recursive function to input the PIN from the user and to check if the entry is present in the dataset or not.

def pn():
    cou=0
    p=int(input("Enter your Pin Number :"))
    f=False
    for i in range(0,len(pin)):    
        if p==pin.iloc[i]:
            cou=i
            f=True
            break
    if f:
        print("\033[1m  Pin NUMBER VALIDATED\n" + "\033[0m")
        return cou
    else:
        print("\033[1m  INVALID Pin NUMBER\n" + "\033[0m")
        pn()
cou=pn()

#storing the index number in 'p3'

p3=cou

#recursive function to input the phone number and to check if its valid combination or not.

def ph():
    phno=int(input("Enter you Phone Number : "))
    v=str(phno)
    v=len(v)
             
    if v<10 and v>10:
        print("\033[1m  PERMISSION NOT GRANTED ...PLEASE RE-ENTER THE PHONE NUMBER\n" + "\033[0m")
        ph()
    else:
        print("\033[1m  PHONE NUMBER IS VALID\n"+ "\033[0m")
        return phno
        
#index number for further operations

if p1==p2:
    if p2==p3:
        p=p2
        
#Recursive function to provide a user interface.

import random
def mai():
    print("\033[0;30mx"*127)
    print("\033[1m \033[34m \033[4m \t\t\t\t\t\t\t CACHE BANK" +"\033[1m \033[34m \033[4m")
    print("\033[0;30mx"*127)
    print("\n\n")
    c=na()
    co=account()
    cou=pn()
    phone=ph()
    if c==co:
        if co==cou:
            print("\033[0;31m \t\t\t\t\t CAN PROCEED TO NEXT STEP\n\n" +"\033[0;30m")
            
        else:
            print("\033[0;31m \t\t\t ACCOUNT NUMBER AND PIN MISMATCH..PLEASE LOGIN AGAIN" +"\033[0;30m")
            mai()
    else:
        print("\033[0;31m \t\t\t USERNAME AND ACCOUNT NUMBER MISMATCH..PLEASE LOGIN AGAIN" +"\033[0;30m")
        mai()
    
    
   
    
    rand=random.randrange(1000,10000)
    print("\033[0;30mAn OTP has been sent to your Phone number as displayed \n ", phone, " : ", rand)
    rando=int(input("Enter the OTP received to check for authentication :"))
    print("\n\n")
    if rand==rando:
        print("\033[0;31m \t\t\t\t\t\t ACCESS GRANTED " +"\033[0;30m")
    else:
        print("\033[0;31m \t\t\t\tINCORRECT OTP..TIME LAPSED..NEED TO LOGIN AGAIN" +"\033[0;30m")
        mai()
        print("\n\n")
    print("\033[0;30mx"*127)
    
mai()

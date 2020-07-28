#Souce code
print("Wellcome\n",
      "Mckinley and Rice\n")
while True:
       id = int(input("\nEnter account pin: "))
       while id < 1000 or id > 9999:
           id = int(input("\nInvalid Id.. Re-enter: "))
       break
print("Create an account\n")
name=input("Enter your name:\n ")
phone=input("Enter your phone number:\n ")
address=input("Enter your address:\n ")
print("Your account summary is:\n")
print("Name:" + name)
print("Phone Number:" + phone)       
print()
balance=float(input("Enter an amount to deposit into the account: "))
print()
print(name,", Thank you for creating an account.")
def printMenu():
    print()
    print("Please choose an option below:")
    print("""
    Enter b to Check your Balance
    Enter d to Deposit money into your Account
    Enter w to Withdraw money from your Account
    Enter q to Quit the Program """)
    print("")
def getTransaction():
    transaction=str(input("What would you like to do? "))
    return transaction

def withdraw(bal,amt):
    global balance
    balance=bal-amt
    notes = [2000, 500, 200, 100]
    noteCounter = [0, 0, 0, 0, 0]
    print ("Currency: ")   
    if balance<0:
           for i, j in zip(notes, noteCounter):
                  if amount >= i:
                         j = amount // i
                         amount = amount - j * i
    balance=balance-10

def formatCurrency(amt):
    return "$%.2f" %amt

printMenu()
command=str(getTransaction())

#main code

while command!="q":
    if (command=="b"):
        print(name,"Your current balance is",formatCurrency(balance))
        printMenu()
        command=str(getTransaction())
    elif (command=="d"):
        amount=float(input("Amount to deposit? "))
        balance=balance+amount
        printMenu()
        command=str(getTransaction())
    elif (command=="w"):
        amount=float(input("Amount to withdraw? "))
        withdraw(balance,amount)
        printMenu()
        command=str(getTransaction())
    else:
        print("Incorrect command. Please try again.")
        printMenu()
        command=str(getTransaction())

print(name,"Thank You! Mckinley and Rice")

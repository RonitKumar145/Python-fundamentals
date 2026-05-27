#menu driven atm

menu= input("""
            hi how can i help you?
            1. check balance
            2. withdraw
            3. deposit
            4. exit
            
            "enter the operation you want to perform: """)

if menu == "1":
    print("your balance is: 1000")
elif menu == "2":
    amount= int (input("enter the amount you want to withdraw: "))
    if amount > 1000:
        print("insufficient balance")
    else:
        print("please collect your cash")
elif menu == "3":
    amount= int (input("enter the amount you want to deposit: "))
    print("your new balance is: ",1000+amount)
elif menu == "4":
    print("thank you for using our services")
else:
    print("invalid operation")

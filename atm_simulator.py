print('welcome to the ATM simulator')
balance=int(input('enter initial balance:'))
while True:
    if balance<=0:
        print('your balance is 0')
        break
    print('MENU OPTIONS')
    print('1. Check Balance')
    print('2. Withdraw')
    print('3. Deposit')
    print('4. Exit')
    choice=int(input('enter your choice:'))
    if choice==1:
        print('your balance is:',balance)
    elif choice==2:
        amount=int(input('enter amount to withdraw:'))
        if amount>balance:
            print('insufficient balance')
        else:
            balance-=amount
            print('withdrawal successful')
    elif choice==3:
        amount=int(input('enter amount to deposit:'))
        balance+=amount
        print('deposit successful')
    elif choice==4:
        print('thank you for using the ATM simulator')
        break
    else:
        print('invalid choice, please try again')
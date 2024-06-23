def show_balance(balance): 
    print(f"your current balance is {float(balance)}")

def deposite(balance):     
    deposite_amount = float(input("Enter the ampount to deposite"))
    if deposite_amount < 0:
        print("Please enter valid ammount")
        return 0
    else:
        print("Ammount deposited successfully")
        return deposite_amount
        
    
def withdraw(balance):
    withdraw_amount = float(input("Enter the amount to withdraw"))
    if balance < withdraw_amount :
        print("You dont have sufficient fund to withdraw")
    else:
        print("Amount withdrawed successfully")
        return withdraw_amount

def main():
    balance = 0
    return_state = True
    print("*****************************")
    print("       BANK PROGRAM          ")
    print("*****************************")
    while return_state:
        print("**********************")
        print("1.SHOW BALANCE")
        print("2.DEPOSITE AMOUNT")
        print("3.WITHDRAW AMOUNT")
        print("4.EXIT")
        print("**********************")
        
        choice = input("Enter your choice")
        
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposite(balance)
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            return_state = False
        else:
            print("Please enter valid choice")

    print("*******************************")
    print("THANK YOU FOR BANKING WITH US")
    print("*********************************")
            
 
if __name__ == "__main__":
    main()
            
        

balance = int(input("Enter the balance: "))

while True:
    print("\n==== ATM Menu ======")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Your balance is:", balance)

        case 2:
            amount = int(input("Enter the amount: "))
            balance += amount
            print("Deposit Successful")
            print("Current balance:", balance)

        case 3:
            amount = int(input("Enter the withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful!")
                print("Current Balance:", balance)
            else:
                print("Insufficient Balance!")

        case 4:
            print("Thank you for using the ATM.")
            break

        case _:
            print("Invalid Choice! Try Again.")
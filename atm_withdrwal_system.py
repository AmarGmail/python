def atm_withdrwal(withdrwal_amount):

    current_balance = 5000

    if withdrwal_amount <= 0:
        print("Error: Withdrwal amount must be greater than 0.")
        return False

    if withdrwal_amount % 500 != 0:
        print("Error: Withdrwal amount must be multiple of 500.")
        return False
    
    if withdrwal_amount > current_balance:
        print(f"Error: Insufficient balance. Available {current_balance}.")
        return False
    
    remaining_balance = current_balance - withdrwal_amount
    print(f"Withdrwal successful! Amount: {withdrwal_amount}")
    print(f"Remaining balance: {remaining_balance}")
    return True


withdrwal = input("Enter the withdrwal amount:  ")

withdrwal_result = atm_withdrwal(int(withdrwal))

if withdrwal_result:
    print("Return: True")
    

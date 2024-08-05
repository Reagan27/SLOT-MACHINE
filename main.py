def deposit():
    while True:
        amount=input("What amount would you like to deposit?: $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("please enter a number.")
    return amount 

def main():
    balance = deposit()





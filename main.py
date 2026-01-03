#“This ATM simulation uses file handling to persist balance and transaction history, PIN authentication for security, and exception handling to prevent crashes due to invalid input.
#The program is modular, menu-driven, and mimics real ATM behavior.


pin = "8899"
balance_file = "balance_file.txt"
history_file = "transaction_history.txt"

def load_balance():
    try:
        with open(balance_file, "r") as f:
            return float(f.read())
    except:
        return 10000.0
def save_balance(balance):
    with open(balance_file,"w")as f:
        f.write(str(balance))

def log_transaction(message):
    with open("transaction_log.txt","a") as f:
        f.write(message + "\n")

balance = load_balance()

def check_balance():
    print(f"Your balance is: ${balance} ")
check_balance()
def deposit(amount):
    global balance
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount <=0:
            print("Deposit amount must be positive.")
        else:
            balance += amount
            print(f"{amount} deposited successfully.")
            print(f"New balance: ${balance}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def withdrawl(amount):
    try:
        amount = float(input("Enter the amount to be withdrawn: "))
        global balance
        if amount <=0:
            print("Withdrawal amount must be positive.")
        elif amount > balance:
            print("-------INSUFFICIENT BALANCE-------")
        else:
            balance -= amount
            print(f"{amount} withdrawn successfully.")
            print(f"New Balance: ${balance}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
def authenticate():
    attempts = 3
    
    while attempts > 0:
        entered_pin = input("Enter your pin: ")
        if entered_pin==pin:
            print("-----Authenticating-----")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN.")
            if attempts == 0:
                print("-----Too many incorrect attempts. Exiting.-----")
                return False
            else:
                print(f"You have {attempts} attempts left.")
def main():
    if not authenticate():
        return


def transaction_history():
    try:
        with open("transaction_history.txt", "r") as f:
            print("----Transaction History----")
            print(f.read())
    except FileNotFoundError:
        print("No transaction history found.")

def main():
    while True:
        print("\n---Welcome to the ATM---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdrawl")
        print("4. Transaction History")
        print("5. Exit")
        try:
            choice = input("Choose an action (1-4):")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit(amount=0)
        elif choice == '3':
            withdrawl(amount=0)
        elif choice == '4':
            transaction_history()


        elif choice == '5':
            print("-----Thankyou for using the ATM.-----")
            break
        else:
            print("Invalid Character. Please check again.")
authenticate()
if __name__ == "__main__":
    main()


    

    


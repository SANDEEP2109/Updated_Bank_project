class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def details(self):
        return f"Account details:\nAccount Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: {self.balance:.2f}"

    def show_balance(self):
        return f"Your balance is {self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit amount is {amount}. New balance is {self.balance:.2f}."
        else:
            return "Amount should be greater than 0."

    def debit(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"withdrawed amount {amount}. New balance is {self.balance:.2f}."
        else:
            return "Invalid amount."

def save_accounts(accounts, filename):
    with open(filename, 'w') as file:
        for account in accounts:
            file.write(f"{account.account_holder},{account.account_number},{account.balance}\n")

def load_accounts(filename):
    accounts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                acc_holder, acc_number, acc_balance = line.strip().split(',')
                accounts.append(BankAccount(acc_number, acc_holder, float(acc_balance)))
    except FileNotFoundError:
        pass  # If file doesn't exist, return empty list of accounts
    return accounts

# Main program
filename = 'bank_accounts.txt'
accounts = load_accounts(filename)

while True:
    print("\nSelect an option:")
    print("1. Create account")
    print("2. See account details")
    print("3. Deposit amount")
    print("4. Withdraw amount")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        acc_name = input("Enter your name: ")
        acc_number = input("Enter your account number: ")
        acc_balance = float(input("Enter your account balance: "))
        accounts.append(BankAccount(acc_number, acc_name, acc_balance))
        print("Account created successfully.")
        save_accounts(accounts, filename)
    elif choice == '2':
        acc_number = input("Enter account number to see details: ")
        found = False
        for account in accounts:
            if account.account_number == acc_number:
                print(account.details())
                found = True
                break
        if not found:
            print("Account not found.")
    elif choice == '3':
        acc_number = input("Enter account number to deposit: ")
        found = False
        for account in accounts:
            if account.account_number == acc_number:
                acc_deposit = float(input("Enter deposit amount: "))
                print(account.deposit(acc_deposit))
                save_accounts(accounts, filename)
                found = True
                break
        if not found:
            print("Account not found.")
    elif choice == '4':
        acc_number = input("Enter account number to withdraw: ")
        found = False
        for account in accounts:
            if account.account_number == acc_number:
                acc_debit = float(input("Enter withdraw amount: "))
                print(account.debit(acc_debit))
                save_accounts(accounts, filename)
                found = True
                break
        if not found:
            print("Account not found.")
    elif choice == '5':
        print("Thank you for using the banking system.")
        break
    else:
        print("Invalid option. Please select again.")

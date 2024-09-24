class BankAccount:
    def __init__(self, name, account_number, initial_balance):
        self.name = name
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")


def create_account():
    name = input("Enter your name: ")
    account_number = input("Enter your account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(name, account_number, initial_balance)


def main():
    accounts = []
    while True:
        print("\nChoose an option:")
        print("1. Create a new account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            account = create_account()
            accounts.append(account)
            print("Account created successfully!")
        elif choice == 2:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.deposit(amount)
                    break
            else:
                print("Account not found.")
        elif choice == 3:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.withdraw(amount)
                    break
            else:
                print("Account not found.")
        elif choice == 4:
            account_number = int(input("Enter account number: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.check_balance()
                    break
            else:
                print("Account not found.")
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

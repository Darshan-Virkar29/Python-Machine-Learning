class BankAccount:
    # Class variable initialized to 10.5
    ROI = 10.5 

    def __init__(self, Name, Amount):
        # Instance variables
        self.Name = Name
        self.Amount = float(Amount)

    def Display(self):
        print(f"Account Holder: {self.Name} | Current Balance: ${self.Amount:.2f}")

    def Deposit(self):
        try:
            deposit_amount = float(input(f"Enter amount to deposit for {self.Name}: "))
            if deposit_amount > 0:
                self.Amount += deposit_amount
                print(f"Successfully deposited ${deposit_amount:.2f}.")
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    def Withdraw(self):
        try:
            withdraw_amount = float(input(f"Enter amount to withdraw for {self.Name}: "))
            if withdraw_amount > self.Amount:
                print("Transaction Failed: Insufficient balance.")
            elif withdraw_amount <= 0:
                print("Withdrawal amount must be positive.")
            else:
                self.Amount -= withdraw_amount
                print(f"Successfully withdrew ${withdraw_amount:.2f}.")
        except ValueError:
             print("Invalid input. Please enter a numerical value.")

    def CalculateInterest(self):
        # Interest = (Amount * ROI) / 100
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


def main():
    print("--- BankAccount Object 1 ---")
    account1 = BankAccount("Alice", 1000.0)
    account1.Display()
    account1.Deposit()
    account1.Withdraw()
    account1.Display()
    print(f"Calculated Interest: ${account1.CalculateInterest():.2f}\n")

    print("--- BankAccount Object 2 ---")
    account2 = BankAccount("Bob", 500.0)
    account2.Display()
    account2.Deposit()
    account2.Withdraw()
    account2.Display()
    print(f"Calculated Interest: ${account2.CalculateInterest():.2f}\n")

if __name__ == "__main__":
    main()
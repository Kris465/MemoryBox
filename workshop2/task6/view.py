from controller import ATMController


class ATMView:
    def __init__(self, ATMController: ATMController):
        self.controller = ATMController

    def run(self):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                amount = int(input(
                    "Enter the amount to deposit (must be a multiple of 50): "
                    ))
                if amount % 50 != 0:
                    print("Amount must be a multiple of 50")
                    continue
                balance = self.controller.deposit(amount)
                print("New balance: {}".format(balance))
            elif choice == "2":
                amount = int(input(
                    "Enter the amount to withdraw (must be a multiple of 50): "
                    ))
                if amount % 50 != 0:
                    print("Amount must be a multiple of 50")
                    continue
                success, balance = self.controller.withdraw(amount)
                if success:
                    print("New balance: {}".format(balance))
                else:
                    print("Insufficient funds")
            elif choice == "3":
                break
            else:
                print("Invalid choice")

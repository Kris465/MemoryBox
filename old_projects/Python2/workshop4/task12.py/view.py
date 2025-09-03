from datetime import datetime
from controller import ATMController


class ATMView:
    def __init__(self, ATMController: ATMController):
        self.controller = ATMController
        self.history = []

    def run(self):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            print("4. History")
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    amount = int(input(
                        "Enter the amount to deposit: "))
                    if amount % 50 != 0:
                        print("Amount must be a multiple of 50")
                        continue
                    balance = self.controller.deposit(amount)
                    operation = {f"{datetime.now().time()}":
                                 f"deposit {amount}"}
                    self.history.append(operation)
                    print("New balance: {}".format(balance))
                case "2":
                    amount = int(input(
                        "Enter the amount to withdraw: "
                        ))
                    if amount % 50 != 0:
                        print("Amount must be a multiple of 50")
                        continue
                    success, balance = self.controller.withdraw(amount)
                    if success:
                        operation = {f"{datetime.now().time()}":
                                     f"withdraw {amount}"}
                        self.history.append(operation)
                        print("New balance: {}".format(balance))
                    else:
                        print("Insufficient funds")
                case "3":
                    break
                case "4":
                    print(*self.history)
                case _:
                    print("Invalid choice")

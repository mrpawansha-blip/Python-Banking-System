"""
Python Banking System
Module 03: Object-Oriented Python

Demonstrates:
- Classes, objects, constructors and methods
- Encapsulation using private attributes
- Inheritance and polymorphism
- Abstraction using an abstract base class
- Account creation, deposit, withdrawal and transaction history
"""

from abc import ABC, abstractmethod
from datetime import datetime


class BankAccount(ABC):
    """Abstract base class for bank accounts."""

    def __init__(self, account_number, account_holder, opening_balance=0.0):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.account_number = str(account_number)
        self.account_holder = account_holder
        self.__balance = float(opening_balance)  # Encapsulated attribute
        self._transactions = []
        if opening_balance:
            self._record("Opening balance", opening_balance)

    @property
    def balance(self):
        """Read-only access to account balance."""
        return self.__balance

    def _record(self, transaction_type, amount):
        self._transactions.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "amount": round(float(amount), 2),
            "balance": round(self.__balance, 2)
        })

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount
        self._record("Deposit", amount)
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.__balance:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount
        self._record("Withdrawal", amount)
        return self.__balance

    def transaction_history(self):
        return list(self._transactions)

    @abstractmethod
    def account_type(self):
        """Return the account type."""
        pass

    def display_details(self):
        print(f"Account number : {self.account_number}")
        print(f"Account holder : {self.account_holder}")
        print(f"Account type   : {self.account_type()}")
        print(f"Balance        : Rs. {self.balance:.2f}")


class SavingsAccount(BankAccount):
    """Savings account with a minimum balance rule."""

    def account_type(self):
        return "Savings"

    def withdraw(self, amount):
        minimum_balance = 500.0
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if self.balance - amount < minimum_balance:
            raise ValueError("Savings account must maintain Rs. 500 minimum balance.")
        return super().withdraw(amount)


class CurrentAccount(BankAccount):
    """Current account; uses the base withdrawal rule."""

    def account_type(self):
        return "Current"


class BankingSystem:
    """Manages bank accounts and user operations."""

    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter new account number: ").strip()
        if not account_number:
            print("Account number cannot be empty.")
            return
        if account_number in self.accounts:
            print("Account number already exists.")
            return

        name = input("Enter account holder name: ").strip()
        if not name:
            print("Account holder name cannot be empty.")
            return

        account_kind = input("Account type (S for Savings / C for Current): ").strip().upper()
        if account_kind not in ("S", "C"):
            print("Please choose S or C.")
            return

        try:
            opening_balance = float(input("Opening balance: Rs. "))
            account_class = SavingsAccount if account_kind == "S" else CurrentAccount
            self.accounts[account_number] = account_class(
                account_number, name, opening_balance
            )
            print("Account created successfully.")
        except ValueError as error:
            print(f"Could not create account: {error}")

    def find_account(self):
        account_number = input("Enter account number: ").strip()
        account = self.accounts.get(account_number)
        if account is None:
            print("Account not found.")
        return account

    def deposit_money(self):
        account = self.find_account()
        if account:
            try:
                amount = float(input("Enter deposit amount: Rs. "))
                account.deposit(amount)
                print(f"Deposit successful. New balance: Rs. {account.balance:.2f}")
            except ValueError as error:
                print(f"Transaction failed: {error}")

    def withdraw_money(self):
        account = self.find_account()
        if account:
            try:
                amount = float(input("Enter withdrawal amount: Rs. "))
                account.withdraw(amount)
                print(f"Withdrawal successful. New balance: Rs. {account.balance:.2f}")
            except ValueError as error:
                print(f"Transaction failed: {error}")

    def show_balance(self):
        account = self.find_account()
        if account:
            account.display_details()

    def show_history(self):
        account = self.find_account()
        if account:
            history = account.transaction_history()
            if not history:
                print("No transactions recorded yet.")
                return
            print("\nDATE/TIME             TYPE          AMOUNT       BALANCE")
            print("-" * 66)
            for item in history:
                print(
                    f"{item['time']:<21} {item['type']:<13} "
                    f"Rs.{item['amount']:<10.2f} Rs.{item['balance']:.2f}"
                )

    def run(self):
        while True:
            print("\n========== PYTHON BANKING SYSTEM ==========")
            print("1. Create account")
            print("2. Deposit money")
            print("3. Withdraw money")
            print("4. Check account details / balance")
            print("5. View transaction history")
            print("6. Exit")
            choice = input("Select an option (1-6): ").strip()

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit_money()
            elif choice == "3":
                self.withdraw_money()
            elif choice == "4":
                self.show_balance()
            elif choice == "5":
                self.show_history()
            elif choice == "6":
                print("Thank you for using Python Banking System.")
                break
            else:
                print("Invalid choice. Please select 1 to 6.")


if __name__ == "__main__":
    BankingSystem().run()

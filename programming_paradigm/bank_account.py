class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount to the account."""
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw a specified amount from the account if sufficient funds are available."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")

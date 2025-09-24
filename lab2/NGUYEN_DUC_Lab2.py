

class BankAccount:
    def __init__(self, new_name, checking_balance, savings_balance):
        self.customer_name = str(new_name)
        self.checking_balance = float(checking_balance)
        self.savings_balance = float(savings_balance)

    # def print_card_info(self):
    #     print("Card Holder: ", self.customer_name)
    #     print("Current Checking Balance: ", self.checking_balance)
    #     print("Current Savings Balance: ", self.savings_balance)

    def deposit_checking(self, amount):
        if amount > 0:
            self.checking_balance = self.checking_balance + amount
            # self.print_card_info()
        else:
            return ValueError
        
    def deposit_saving(self, amount):
        if amount > 0:
            self.savings_balance = self.savings_balance + amount
            # self.print_card_info()
        else:
            return ValueError
        
    def withdraw_checking(self, amount):
        if amount > 0 :
            if (self.checking_balance - amount) >= 0:
                self.checking_balance = self.checking_balance - amount
                # self.print_card_info()
            else:
                return ValueError
        else:
            return ValueError
        
    def withdraw_savings(self, amount):
        if amount > 0 :
            if (self.savings_balance - amount) >= 0:
                self.savings_balance = self.savings_balance - amount
                # self.print_card_info()
            else:
                return ValueError
        else:
            return ValueError
    
    def transfer_to_savings(self, amount):
        if amount > 0:
            if self.checking_balance - amount >= 0:
                self.savings_balance = self.savings_balance + amount
                self.checking_balance = self.checking_balance - amount
                # self.print_card_info()
            else:
                return ValueError
        else:
            return ValueError
        
def main():
# Create a new bank account
    account = BankAccount("Mickey", 500.00, 1000.00)
# Set values
    account.checking_balance = 500
    account.savings_balance = 500
# Do some transactions
    account.withdraw_savings(100)
    account.withdraw_checking(100)
    account.transfer_to_savings(300)
# Print results
    print(account.customer_name)
    print(f"${account.checking_balance:.2f}")
    print(f"${account.savings_balance:.2f}") 


main()
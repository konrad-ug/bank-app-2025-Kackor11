# mala sciaga:
# python3 -m coverage run --source=src -m pytest
# python3 -m coverage report

class Account:
    def __init__(self):
        self.balance = 0.00
        self.transaction_history = []
        
    def transfer_in(self, amount):
        if isinstance(amount, float):
            self.balance += amount
            self.update_transfer_history(amount, 0)
            return True
        return False
                        
    def transfer_out(self, amount):
        if isinstance(amount, float) and self.balance >= amount:
            self.balance -= amount
            self.update_transfer_history(-amount, 0)
            return True
        return False
            
    def express_transfer(self, amount):
        from src.customer_account import Customer_Account
        if isinstance(self, Customer_Account):
            fee = 1.00
        else:
            fee = 5.00
        
        if self.balance >= amount:
            self.balance = self.balance - amount - fee
            self.update_transfer_history(-amount, -fee)
            return True
        return False
    
    def update_transfer_history(self, amount_value, fee_value):
        self.transaction_history.append(amount_value)
        if fee_value != 0:
            self.transaction_history.append(fee_value)
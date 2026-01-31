# mala sciaga:
# python3 -m coverage run --source=src -m pytest
# python3 -m coverage report
from datetime import datetime

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

    def send_history_via_email(self, email_address):
        from src.smtp.smtp import SMTPClient
        from src.customer_account import Customer_Account
        from src.firm_account import Firm_Account
        
        date_str = datetime.now().strftime("%Y-%m-%d")
        subject = f"Account Transfer History {date_str}"
        
        if isinstance(self, Customer_Account):
            msg_content = f"Personal account history: {self.transaction_history}"
        elif isinstance(self, Firm_Account):
             msg_content = f"Company account history: {self.transaction_history}"
        else:
             msg_content = f"Account history: {self.transaction_history}"

        return SMTPClient.send(subject, msg_content, email_address)
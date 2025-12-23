from src.account import Account

class Firm_Account(Account):
    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.nip = nip if len(nip) == 10 else "INVALID"
        self.balance = 0.00
        self.transaction_history = []
        
    def take_loan(self, amount):
        if self.balance > amount * 2 and -1775 in self.transaction_history:
            self.balance += amount
            return True
        return False
        

        
        
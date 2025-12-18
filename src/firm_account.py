from src.account import Account

class Firm_Account(Account):
    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.nip = nip if len(nip) == 10 else "INVALID"
        self.balance = 0.00
        self.transaction_history = []
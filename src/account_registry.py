from src.customer_account import Customer_Account

class Account_Registry:
    def __init__(self):
        self.accounts = []
        
    def add_account(self, account: Customer_Account):
        if isinstance(account, Customer_Account) and account.is_pesel_valid(account.pesel):
            existing_acc = self.search_by_pesel(account.pesel)
            if existing_acc is None:
                self.accounts.append(account)
                return True
            return False
        return False
    
    def search_by_pesel(self, given_pesel):
        for person in self.accounts:
            if person.pesel == given_pesel:
                return person
        return None
        
    def return_all_accounts(self):
        return self.accounts
    
    def return_registry_length(self):
        return len(self.accounts)
        
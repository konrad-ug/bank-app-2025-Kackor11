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
                       
    def transfer_out(self, amount):
        if isinstance(amount, float) and self.balance >= amount:
            self.balance -= amount
        self.update_transfer_history(-amount, 0)
            
    def express_transfer(self, amount):
        if isinstance(self, Customer_Account):
            fee = 1.00
        else:
            fee = 5.00
        
        new_balance = self.balance - amount - fee
        self.balance = new_balance if (self.balance - amount) >= 0 else self.balance
        
        self.update_transfer_history(-amount, -fee)
    
    def update_transfer_history(self, amount_value, fee_value):
        self.transaction_history.append(amount_value)
        if fee_value != 0:
            self.transaction_history.append(fee_value)
        


class Customer_Account(Account):
    def __init__(self, first_name, last_name, pesel, promo_code):
        self.first_name = first_name
        self.last_name = last_name
        self.given_promo_code = promo_code
        self.balance = 0.00
        self.transaction_history = []
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"
        
        if self.is_code_given_and_valid(promo_code) and self.is_person_young_enough(pesel):
            self.balance = 50.00
    
    def is_pesel_valid(self, pesel):
        if isinstance(pesel, str) and len(pesel) == 11:
            return True
        return False
    
    def is_code_given_and_valid(self, given_promo_code):
        if given_promo_code != None:
            if len(given_promo_code) == 8 and given_promo_code[:5] == "PROM_":
                return True
            return False
        
    def is_person_young_enough(self, pesel):
        if not self.is_pesel_valid(pesel):
            return False
        
        year = int(pesel[:2])
        month = int(pesel[2:4])
        if 1 <= month <= 12:
            return year > 60
        return True
    
class Firm_Account(Account):
    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.nip = nip if len(nip) == 10 else "INVALID"
        self.balance = 0.00
        self.transaction_history = []

        
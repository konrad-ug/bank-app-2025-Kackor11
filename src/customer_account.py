from src.account import Account

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

    def submit_for_loan(self, amount):
        if len(self.transaction_history) < 5:
            return False
        
        last_three_positive = all(t > 0 for t in self.transaction_history[-3:])
        
        sum_last_five_greater_then_amount = sum(self.transaction_history[-5:]) > amount
        
        if sum_last_five_greater_then_amount or last_three_positive:
            self.balance += amount
            return True
        
        return False
            
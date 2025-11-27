class Account:
    def __init__(self, first_name, last_name, pesel, promo_code):
        self.first_name = first_name
        self.last_name = last_name
        self.given_promo_code = promo_code
        self.balance = 0.0
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"
        
        if self.is_code_given_and_valid(promo_code) and self.is_person_young_enough(pesel):
            self.balance = 50.0
    
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
        

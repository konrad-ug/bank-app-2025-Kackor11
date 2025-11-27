from src.account import Account


class TestAccount:
    def test_account_creation_with_valid_promo_code(self):
        account = Account("John", "Doe", "12345678910", "PROM_XYZ")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 50.0
        assert account.pesel == "12345678910"
        
    def test_account_creation_without_valid_promo_code(self):
        account = Account("John", "Doe", "12345678910", "PROM_XYZB")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        assert account.pesel == "12345678910"
        
    def test_pesel_too_short(self):
        account = Account("Jane", "Doe", "12345", "PROM_XYZ")
        assert account.pesel == "Invalid"
        
    def test_pesel_too_long(self):
        account = Account("Jane", "Doe", "1234556660543458", "PROM_XYZ")
        assert account.pesel == "Invalid"
        
    def test_pesel_not_given(self):
        account = Account("Jane", "Doe", None, "PROM_XYZ")
        assert account.pesel == "Invalid"
        
    def test_promo_code_not_given(self):
        account = Account("Jane", "Doe", "12345678910", None)
        assert account.balance == 0.0
    
    def test_promo_code_given_valid(self):
        account = Account("Jane", "Doe", "12345678910", "PROM_XYZ")
        assert account.balance == 50.0
        
    def test_promo_code_given_invalid_1(self):
        account = Account("Jane", "Doe", "12345678910", "PRO_XYZ")
        assert account.balance == 0.0
        
    def test_person_born_after_1960_and_promo_valid(self):
        account = Account("Jane", "Doe","850515PPP6K", "PROM_XYZ")
        assert account.balance == 50.0
        
    def test_person_born_before_1960_and_promo_valid(self):
        account = Account("Jane", "Doe", "58092104246", "PROM_XYZ")
        assert account.balance == 0.0
        
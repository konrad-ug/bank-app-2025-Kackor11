from src.account import Customer_Account, Firm_Account, Account

class Test_Account:
    def test_base_account_if_valid(self):
        account = Account()
        assert account.balance == 0.00

class Test_Firm_Account:
    def test_firm_account_creation_with_valid_nip(self):
        account = Firm_Account("Valve", "1234567890")
        assert account.company_name == "Valve"
        assert account.nip == "1234567890"
        
    def test_firm_account_creation_with_invalid_nip(self):
        account = Firm_Account("Valve", "123456789")
        assert account.company_name == "Valve"
        assert account.nip == "INVALID"

        
class Test_Firm_Transfer:
    def test_firm_account_express_transfer_enough_money(self):
        account = Firm_Account("Valve", "1234567890")
        account.balance += 200.00
        account.express_transfer(190.00)
        assert account.balance == 5.00
        
    def test_firm_account_express_transfer_not_enough_money(self):
        account = Firm_Account("Valve", "1234567890")
        account.balance += 200.00
        account.express_transfer(210.00)
        assert account.balance == 200.00 
    
    def test_firm_account_express_transfer_equal_money(self):
        account = Firm_Account("Valve", "1234567890")
        account.balance += 200.00
        account.express_transfer(200.00)
        assert account.balance == -5.00

    def test_transfer_out_Firm_Account_went_through_enough_money(self):
        account = Firm_Account("Valve", "1234567890")
        account.balance += 200.00
        account.transfer_out(150.00)
        assert account.balance == 50.00
        
    def test_transfer_out_Firm_Account_did_not_go_through_not_enough_money(self):
        account = Firm_Account("Valve", "1234567890")
        account.balance += 200.00
        account.transfer_out(260.00)
        assert account.balance == 200.00
        
    def test_Firm_Account_transfer_in(self):
        account = Firm_Account("Valve", "1234567890")
        account.transfer_in(100.00)
        assert account.balance == 100.00
        
    def test_Firm_Account_transfer_in_invalid_type(self):
        account = Firm_Account("Valve", "1234567890")
        account.transfer_in("abc")
        assert account.balance == 0.00
        

class Test_Customer_Account:
    def test_account_creation_with_valid_promo_code(self):
        account = Customer_Account("John", "Doe", "12345678910", "PROM_XYZ")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 50.00
        assert account.pesel == "12345678910"
        
    def test_account_creation_without_valid_promo_code(self):
        account = Customer_Account("John", "Doe", "12345678910", "PROM_XYZB")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.00
        assert account.pesel == "12345678910"
        
    def test_pesel_too_short(self):
        account = Customer_Account("Jane", "Doe", "12345", "PROM_XYZ")
        assert account.pesel == "Invalid"
        
    def test_pesel_too_long(self):
        account = Customer_Account("Jane", "Doe", "1234556660543458", "PROM_XYZ")
        assert account.pesel == "Invalid"
        
    def test_pesel_not_given(self):
        account = Customer_Account("Jane", "Doe", None, "PROM_XYZ")
        assert account.pesel == "Invalid"
        
    def test_promo_code_not_given(self):
        account = Customer_Account("Jane", "Doe", "12345678910", None)
        assert account.balance == 0.00
    
    def test_promo_code_given_valid(self):
        account = Customer_Account("Jane", "Doe", "12345678910", "PROM_XYZ")
        assert account.balance == 50.00
        
    def test_promo_code_given_invalid_1(self):
        account = Customer_Account("Jane", "Doe", "12345678910", "PRO_XYZ")
        assert account.balance == 0.00
        
    def test_person_born_after_1960_and_promo_valid(self):
        account = Customer_Account("Jane", "Doe","850515PPP6K", "PROM_XYZ")
        assert account.balance == 50.00
        
    def test_person_born_before_1960_and_promo_valid(self):
        account = Customer_Account("Jane", "Doe", "58092104246", "PROM_XYZ")
        assert account.balance == 0.00
        
    def test_person_born_after_2000_and_promo_valid(self):
        account = Customer_Account("Jane", "Doe", "01251587623", "PROM_XYZ")
        assert account.balance == 50.00

        
class Test_Customer_Transfer:
    def test_customer_account_express_transfer_enough_money(self):
        account = Customer_Account("Jane", "Doe", "01251587623", None)
        account.balance += 200.00
        account.express_transfer(190.00)
        assert account.balance == 9.00
        
    def test_customer_account_express_transfer_not_enough_money(self):
        account = Customer_Account("Jane", "Doe", "01251587623", None)
        account.balance += 200.00
        account.express_transfer(210.00)
        assert account.balance == 200.00
    
    def test_customer_account_express_transfer_equal_money(self):
        account = Customer_Account("Jane", "Doe", "01251587623", None)
        account.balance += 200.00
        account.express_transfer(200.00)
        assert account.balance == -1.00
    
    def test_transfer_Customer_Account_went_through_enough_money(self):
        account = Customer_Account("Jane", "Doe", "01251587623", "PROM_XYZ")
        account.balance += 200.00
        account.transfer_out(150.00)
        assert account.balance == 100.00
        
    def test_transfer_Customer_Account_did_not_go_through_not_enough_money(self):
        account = Customer_Account("Jane", "Doe", "01251587623", "PROM_XYZ")
        account.balance += 200.00
        account.transfer_out(260.00)
        assert account.balance == 250.00
        
    def test_Customer_Account_transfer_in(self):
        account = Customer_Account("Jane", "Doe", "01251587623", "PROM_XYZ")
        account.transfer_in(100.00)
        assert account.balance == 150.00
        
    def test_Customer_Account_transfer_in_invalid_type(self):
        account = Customer_Account("Jane", "Doe", "01251587623", "PROM_XYZ")
        account.transfer_in("abc")
        assert account.balance == 50.00

       
class Test_Account_transaction_history:
    # CUSTOMER ACCOUNT TESTS
    def test_customer_account_history_valid_express_transfer(self):
        account = Customer_Account("Jane", "Doe", "01251587623", None)
        account.balance += 200.00
        account.express_transfer(190.00)
        assert account.transaction_history == [-190.00, -1.00]
        
    def test_customer_account_history_valid_transfer_in(self):
        account = Customer_Account("Jane", "Doe", "01251587623", None)
        account.balance == 0.00
        account.transfer_in(200.00)
        account.transfer_in(150.00)
        assert account.transaction_history == [200.00, 150.00]
        
    def test_customer_account_history_valid_transfer_out(self):
        account = Customer_Account("Jane", "Doe", "01251587623", None)
        account.balance == 1000.00
        account.transfer_out(200.00)
        account.transfer_out(150.00)
        assert account.transaction_history == [-200.00, -150.00]
    
    def test_customer_account_history_multiple_diffrent_transfers(self):
        account = Customer_Account("Jane", "Doe", "01251587623", None)
        account.balance == 100.00
        account.transfer_in(200.00)
        account.transfer_out(150.00)
        account.express_transfer(50.00)
        assert account.transaction_history == [200.00, -150.00, -50.00, -1.00]
    
    # FIRM ACCOUNT TESTS
    def test_firm_account_history_valid_express_transfer(self):
        account = Firm_Account("Valve", "1234567890")
        account.balance += 200.00
        account.express_transfer(190.00)
        assert account.transaction_history == [-190.00, -5.00]
        
    def test_firm_account_history_valid_transfer_in(self):
        account = Firm_Account("Valve", "1234567890")
        account.balance == 0.00
        account.transfer_in(200.00)
        account.transfer_in(150.00)
        assert account.transaction_history == [200.00, 150.00]
        
    def test_firm_account_history_valid_transfer_out(self):
        account = Firm_Account("Valve", "1234567890")
        account.balance == 1000.00
        account.transfer_out(200.00)
        account.transfer_out(150.00)
        assert account.transaction_history == [-200.00, -150.00]
    
    def test_firm_account_history_multiple_diffrent_transfers(self):
        account = Firm_Account("Valve", "1234567890")
        account.balance == 100.00
        account.transfer_in(200.00)
        account.transfer_out(150.00)
        account.express_transfer(50.00)
        assert account.transaction_history == [200.00, -150.00, -50.00, -5.00]
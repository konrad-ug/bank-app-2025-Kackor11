from src.customer_account import Customer_Account

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

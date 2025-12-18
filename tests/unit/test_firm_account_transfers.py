from src.firm_account import Firm_Account
        
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
        

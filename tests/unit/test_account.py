from src.account import Account
from src.customer_account import Customer_Account
from src.firm_account import Firm_Account

class Test_Account:
    def test_base_account_if_valid(self):
        account = Account()
        assert account.balance == 0.00

class Test_Customer_Account_transaction_history:
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
    
class Test_Firm_Account_transaction_history:
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
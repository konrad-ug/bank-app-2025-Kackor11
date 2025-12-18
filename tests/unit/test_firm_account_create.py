from src.firm_account import Firm_Account

class Test_Firm_Account:
    def test_firm_account_creation_with_valid_nip(self):
        account = Firm_Account("Valve", "1234567890")
        assert account.company_name == "Valve"
        assert account.nip == "1234567890"
        
    def test_firm_account_creation_with_invalid_nip(self):
        account = Firm_Account("Valve", "123456789")
        assert account.company_name == "Valve"
        assert account.nip == "INVALID"
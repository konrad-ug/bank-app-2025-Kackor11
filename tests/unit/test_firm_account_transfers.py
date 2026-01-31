import pytest
from src.firm_account import Firm_Account
from unittest.mock import patch

@pytest.fixture
def account():
    with patch.object(Firm_Account, 'verify_nip_in_gov', return_value=True):
        return Firm_Account("Valve", "1234567890")
     
class Test_Firm_express_Transfer:
    @pytest.mark.parametrize("start_balance, transfer_value, end_balance", [
        [200.00, 190.00, 5.00],
        [200.00, 210.00, 200.00],
        [200.00, 200.00, -5.00]
    ])
    
    def test_firm_express_transfer(self, account, start_balance, transfer_value, end_balance):
        account.balance = start_balance
        account.express_transfer(transfer_value)
        assert account.balance == end_balance

class Test_Firm_Transfer_In:
    @pytest.mark.parametrize("transfer_value, end_balance", [
        [100.00, 100.00],
        ["abc", 0.00]
    ])
    
    def test_firm_in_transfer(self, account, transfer_value, end_balance):
        account.transfer_in(transfer_value)
        assert account.balance == end_balance

class Test_Firm_Transfer_Out:
    @pytest.mark.parametrize("start_balance, transfer_value, end_balance", [
       [200.00, 150.00, 50.00],
        [200.00, 260.00, 200.00]
    ])
    
    def test_firm_out_transfer(self, account, start_balance, transfer_value, end_balance):
        account.balance = start_balance
        account.transfer_out(transfer_value)
        assert account.balance == end_balance
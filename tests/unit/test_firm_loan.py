import pytest
from src.firm_account import Firm_Account
from unittest.mock import patch

@pytest.fixture
def account():
    with patch.object(Firm_Account, 'verify_nip_in_gov', return_value=True):
        return Firm_Account("Valve", "1234567890")

class Test_Firm_For_Loan:
    
    @pytest.mark.parametrize("history, current_balance, amount, expected_loan_result, expected_final_result", [
        # enough money, zus appears
        ([2000, -1775, 100], 2200, 1000, True, 3200),
        # enough money, zus does not appear
        ([2000, 100], 2200, 1000, False, 2200),
        # not enough money, zus appears
        ([2000, 100, -1775], 2200, 2000, False, 2200),
        # not enough money, zus doesnt appear
        ([2000, 100], 2200, 2000, False, 2200)
    ])
    
    def test_submit_for_loan(self, account, history, current_balance, amount, expected_loan_result, expected_final_result):
        account.transaction_history = history
        account.balance = current_balance
        result = account.take_loan(amount)
        assert result == expected_loan_result
        assert account.balance == expected_final_result
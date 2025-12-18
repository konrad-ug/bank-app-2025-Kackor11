import pytest
from src.customer_account import Customer_Account

@pytest.fixture
def account():
    return Customer_Account("Jane", "Doe", "01251587623", None)

class Test_Customer_For_Loan:
    
    @pytest.mark.parametrize("history, current_balance, amount, expected_loan_result, expected_final_balance", [
        # test_customer_loan_history_not_long_enough
        ([100.00, 200.00], 300.00, 500.00, False, 300.00),
        # test_customer_loan_last_three_transactions_are_in
        ([-25, 100.00, 200.00, 400.00, 100.00], 675.00, 500.00, True, 1175.00),
        # test_customer_loan_last_five_transactions_greater_then_loan_amount
        ([-25, 100.00, 200.00, 400.00, -100], 575.00, 500.00, True, 1075.00),
        # test_customer_loan_last_five_transactions_lower_then_loan_amount
        ([-25, 100.00, 200.00, 400.00, -400], 575.00, 500.00, False, 575.00)
    ])
    
    def test_submit_for_loan(self, account, history, current_balance, amount, expected_loan_result, expected_final_balance):
        account.transaction_history = history
        account.balance = current_balance
        result = account.submit_for_loan(amount)
        assert result == expected_loan_result
        assert account.balance == expected_final_balance
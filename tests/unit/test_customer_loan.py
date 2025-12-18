from src.customer_account import Customer_Account

class Test_Customer_For_Loan:
    def test_customer_loan_history_not_long_enough(self):
        account = Customer_Account("Jane", "Doe", "01251587623", None)
        account.transaction_history = [100.00, 200.00]
        account.balance = 300.00
        loan = account.submit_for_loan(500)
        assert loan == False
        assert account.balance == 300.00

    def test_customer_loan_last_three_transactions_are_in(self):
        account = Customer_Account("Jane", "Doe", "01251587623", None)
        account.transaction_history = [-25, 100.00, 200.00, 400.00, 100.00]
        account.balance = 675.00
        loan = account.submit_for_loan(500)
        assert loan == True
        assert account.balance == 1175.00
    
    def test_customer_loan_last_five_transactions_greater_then_loan_amount(self):
        account = Customer_Account("Jane", "Doe", "01251587623", None)
        account.transaction_history = [-25, 100.00, 200.00, 400.00, -100]
        account.balance = 575.00
        loan = account.submit_for_loan(500)
        assert loan == True
        assert account.balance == 1075.00
    
    def test_customer_loan_last_five_transactions_lower_then_loan_amount(self):
        account = Customer_Account("Jane", "Doe", "01251587623", None)
        account.transaction_history = [-25, 100.00, 200.00, 400.00, -400]
        account.balance = 575.00
        loan = account.submit_for_loan(500)
        assert loan == False
        assert account.balance == 575.00

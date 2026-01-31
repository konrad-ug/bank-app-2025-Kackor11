import pytest
from src.account import Account
from src.customer_account import Customer_Account
from src.firm_account import Firm_Account
from src.smtp.smtp import SMTPClient
from unittest.mock import patch
from datetime import datetime

class Test_Mail_Sending:
    
    def test_send_history_customer_account_success(self, mocker):
        mock_smtp = mocker.patch("src.smtp.smtp.SMTPClient.send", return_value=True)
        
        account = Customer_Account("Jan", "Kowalski", "12345678901", None)
        account.balance = 100.0
        account.transaction_history = [100.0, -1.0, 500.0] 
        email = "jan@test.com"
        
        result = account.send_history_via_email(email)
        
        assert result is True
        mock_smtp.assert_called_once()
        
        args, _ = mock_smtp.call_args
        subject, text, recipient = args
        
        today = datetime.now().strftime("%Y-%m-%d")
        assert subject == f"Account Transfer History {today}"
        assert text == "Personal account history: [100.0, -1.0, 500.0]"
        assert recipient == email

    def test_send_history_firm_account_success(self, mocker):
        mock_smtp = mocker.patch("src.smtp.smtp.SMTPClient.send", return_value=True)
        
        with patch.object(Firm_Account, 'verify_nip_in_gov', return_value=True):
            account = Firm_Account("Valve", "1234567890")
            
        account.transaction_history = [5000.0, -1000.0, 500.0]
        email = "ceo@valve.com"
        
        result = account.send_history_via_email(email)
        
        assert result is True
        
        args, _ = mock_smtp.call_args
        subject, text, recipient = args
        
        today = datetime.now().strftime("%Y-%m-%d")
        assert subject == f"Account Transfer History {today}"
        assert text == "Company account history: [5000.0, -1000.0, 500.0]"
        assert recipient == email

    def test_send_history_failure(self, mocker):
        mock_smtp = mocker.patch("src.smtp.smtp.SMTPClient.send", return_value=False)
        account = Customer_Account("Jan", "Kowalski", "12345678901", None)
        
        result = account.send_history_via_email("bad@email.com")
        
        assert result is False
        mock_smtp.assert_called_once()

    def test_send_history_base_account(self, mocker):
        mock_smtp = mocker.patch("src.smtp.smtp.SMTPClient.send", return_value=True)
        account = Account()
        account.transaction_history = [10.0]
        
        result = account.send_history_via_email("base@test.com")
        
        assert result is True
        args, _ = mock_smtp.call_args
        _, text, _ = args
        assert text == "Account history: [10.0]"

    def test_smtp_client_real_implementation(self):
        result = SMTPClient.send("Subject", "Body", "email@test.com")
        assert result is False
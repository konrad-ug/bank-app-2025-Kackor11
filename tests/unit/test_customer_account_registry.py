import pytest
from src.customer_account import Customer_Account
from src.account_registry import Account_Registry
from src.firm_account import Firm_Account

@pytest.fixture
def account_registry():
    pass
    
class Test_Account_Registry_contains:
    def test_every_account_is_customer_account(self):
        account_registry = Account_Registry()
        account_registry.accounts = [
        Customer_Account("Jane", "Doe", "12345678910", None),
        Customer_Account("John", "Dawidson", "12365478910", None),
        Customer_Account("Joanna", "D'arc", "12345678019", None)
    ]
        result = all(isinstance(account, Customer_Account) for account in account_registry.accounts)
        assert result == True
        
    def test_not_every_account_is_customer_account(self):
        account_registry = Account_Registry()
        account_registry.accounts = [
        Firm_Account("Valve", "1234567890"),
        Customer_Account("John", "Dawidson", "12365478910", None),
        Customer_Account("Joanna", "D'arc", "12345678019", None)
    ]
        result = all(isinstance(account, Customer_Account) for account in account_registry.accounts)
        assert result == False
           
@pytest.fixture
def account_registry():
    account_registry = Account_Registry()
    account_registry.accounts = [
            Customer_Account("Jane", "Doe", "12345678911", None),
            Customer_Account("John", "Dawidson", "12365478910", None),
            Customer_Account("Joanna", "D'arc", "12345678019", None)
        ]
    return account_registry

class Test_Adding_To_Account_Registry:
    
    @pytest.mark.parametrize("person, expected_result", [
        [Customer_Account("Person1_name", "Person1_surname", "12345678910", None), True],
        [Customer_Account("Person2_name", "Person2_surname", "12347890", None), False],
        [Customer_Account("Person3_name", "Person3_surname", "12345678911", None), False],
        [Firm_Account("Valve", "1234567890"), False]
    ])
    
    def test_account_we_add_is_customer_account(self, account_registry, person, expected_result):
        result = account_registry.add_account(person)
        assert result == expected_result

from src.customer_account import Customer_Account
from src.account_registry import Account_Registry

class Test_Account_Registry_Return_All:
    def test_return_all_accounts_when_registry_is_empty(self):
        registry = Account_Registry()
        result = registry.return_all_accounts()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_return_all_accounts_returns_added_accounts(self):
        registry = Account_Registry()
        account1 = Customer_Account("Jan", "Testowy", "99112233445", None)
        account2 = Customer_Account("Anna", "Testowa", "99112233446", None)
        
        registry.add_account(account1)
        registry.add_account(account2)
        
        all_accounts = registry.return_all_accounts()
        
        assert len(all_accounts) == 2
        assert account1 in all_accounts
        assert account2 in all_accounts
        assert all_accounts == registry.accounts 
        
class Test_Account_Registry_length:
    def test_registry_length_is_zero(self):
        registry = Account_Registry()
        assert registry.return_registry_length() == 0

    def test_registry_length_increases_when_accounts_added(self):
        registry = Account_Registry()
        account1 = Customer_Account("Jan", "Kowalski", "99999999999", None)
        account2 = Customer_Account("Anna", "Nowak", "88888888888", None)
        registry.add_account(account1)
        assert registry.return_registry_length() == 1
        registry.add_account(account2)
        assert registry.return_registry_length() == 2

    def test_registry_length_does_not_count_duplicates(self):
        registry = Account_Registry()
        account = Customer_Account("Jan", "Kowalski", "99999999999", None)
        registry.add_account(account)
        registry.add_account(account)
        assert registry.return_registry_length() == 1
import pytest
from unittest.mock import MagicMock, patch
from src.mongo_accounts_repository import MongoAccountsRepository
from src.customer_account import Customer_Account
from src.firm_account import Firm_Account

class TestMongoRepository:
    @pytest.fixture
    def mock_repo(self, mocker):
        mocker.patch("src.mongo_accounts_repository.MongoClient")
        repo = MongoAccountsRepository()
        repo.collection = MagicMock()
        return repo

    def test_save_all_customer_account(self, mock_repo):
        account = Customer_Account("Jan", "Kowalski", "12345678901", None)
        mock_repo.save_all([account])
        
        mock_repo.collection.delete_many.assert_called_with({})
        mock_repo.collection.update_one.assert_called()
        
        args, _ = mock_repo.collection.update_one.call_args
        filter_dict = args[0]
        assert "pesel" in filter_dict

    def test_save_all_firm_account(self, mock_repo):
        with patch.object(Firm_Account, 'verify_nip_in_gov', return_value=True):
            firm = Firm_Account("FirmaX", "1234567890")
        
        mock_repo.save_all([firm])
        
        args, _ = mock_repo.collection.update_one.call_args
        filter_dict = args[0]
        assert "nip" in filter_dict
        assert filter_dict["nip"] == "1234567890"

    def test_load_all_returns_objects(self, mock_repo):
        fake_db_data = [
            {
                "type": "customer",
                "name": "Adam",
                "surname": "Nowak",
                "pesel": "99999999999",
                "balance": 100.0,
                "transaction_history": [100.0]
            },
            {
                "type": "firm",
                "company_name": "SoftWareHouse",
                "nip": "1234567890",
                "balance": 5000.0,
                "transaction_history": []
            }
        ]
        
        mock_repo.collection.find.return_value = fake_db_data
        
        loaded_accounts = mock_repo.load_all()
        
        assert len(loaded_accounts) == 2
        
        assert isinstance(loaded_accounts[0], Customer_Account)
        assert loaded_accounts[0].first_name == "Adam"
        
        assert isinstance(loaded_accounts[1], Firm_Account)
        assert loaded_accounts[1].company_name == "SoftWareHouse"
        assert loaded_accounts[1].nip == "1234567890"
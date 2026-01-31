import pytest
import requests
from src.firm_account import Firm_Account
from unittest.mock import patch

class Test_Firm_Account:    
    
    def test_firm_account_creation_with_valid_nip_mocked(self, mocker):
        mock_get = mocker.patch("src.firm_account.requests.get")
        
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": {
                "subject": {
                    "statusVat": "Czynny",
                    "name": "Valve",
                    "nip": "1234567890"
                }
            }
        }
        mock_get.return_value = mock_response

        account = Firm_Account("Valve", "1234567890")
        
        assert account.company_name == "Valve"
        assert account.nip == "1234567890"
        mock_get.assert_called_once()
        
    def test_firm_account_creation_with_invalid_len_nip(self, mocker):
        mocker.patch("src.firm_account.requests.get") 
        
        account = Firm_Account("Valve", "123456789")
        assert account.company_name == "Valve"
        assert account.nip == "INVALID"

    def test_firm_account_creation_api_returns_not_active(self, mocker):
        mock_get = mocker.patch("src.firm_account.requests.get")
        
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": {
                "subject": {
                    "statusVat": "Zwolniony"
                }
            }
        }
        mock_get.return_value = mock_response

        with pytest.raises(ValueError, match="Company not registered!!"):
            Firm_Account("Valve", "1234567890")

    def test_firm_account_creation_api_connection_error(self, mocker):
        mock_get = mocker.patch("src.firm_account.requests.get")
        mock_get.side_effect = requests.exceptions.RequestException("Connection error")
        with pytest.raises(ValueError, match="Company not registered!!"):
            Firm_Account("Valve", "1234567890")
            
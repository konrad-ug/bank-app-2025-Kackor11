import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/accounts"

class TestAPIAccount:
    def test_create_and_get_account(self):
        
        pesel = "12345678901"
        requests.delete(f"{BASE_URL}/{pesel}")
        
        test_account = {
            "name": "Jane",
            "surname": "Doe",
            "pesel": pesel
        }
        response = requests.post(BASE_URL, json=test_account)
        assert response.status_code == 201
        
        response = requests.get(f"{BASE_URL}/12345678901")
        assert response.status_code == 200
        
        data = response.json()
        assert data["name"] == "Jane"
        assert data["surname"] == "Doe"
        assert data["pesel"] == "12345678901"
        
    def test_account_not_found(self):
        response = requests.get(f"{BASE_URL}/01132423420")
        assert response.status_code == 404
        
    def test_update_account(self):
        pesel = "33333333333"
        requests.post(BASE_URL, json={"name": "John", "surname": "Wick", "pesel": pesel})
        
        new_data = {"surname": "Steward"}
        response = requests.patch(f"{BASE_URL}/{pesel}", json=new_data)
        assert response.status_code == 200
        
        response = requests.get(f"{BASE_URL}/{pesel}")
        assert response.json()["surname"] == "Steward"
        assert response.json()["name"] == "John"
        
    def test_delete_account(self):
        pesel = "88888888888"
        requests.post(BASE_URL, json={"name": "Jack", "surname": " Sparrow", "pesel": pesel})
        
        response = requests.delete(f"{BASE_URL}/{pesel}")
        assert response.status_code == 200
        
        response = requests.get(f"{BASE_URL}/{pesel}")
        assert response.status_code == 404
        
    def test_create_account_with_existing_pesel(self):
            pesel = "99799799701"
            account_data = {
                "name": "Unique", 
                "surname": "Person", 
                "pesel": pesel
            }
            requests.delete(f"{BASE_URL}/{pesel}")
            
            response = requests.post(BASE_URL, json=account_data)
            assert response.status_code == 201
            
            response = requests.post(BASE_URL, json=account_data)
            assert response.status_code == 409
            assert response.json()["message"] == "Account with this pesel already exists"
            
            requests.delete(f"{BASE_URL}/{pesel}")

    def setup_method(self):
        self.pesel = "55555555555"
        requests.delete(f"{BASE_URL}/{self.pesel}")
        requests.post(BASE_URL, json={
            "name": "Rich", 
            "surname": "Richie", 
            "pesel": self.pesel
        })

    def teardown_method(self):
        requests.delete(f"{BASE_URL}/{self.pesel}")

    def test_transfer_incoming(self):
        body = {"amount": 100.0, "type": "incoming"}
        response = requests.post(f"{BASE_URL}/{self.pesel}/transfer", json=body)
        
        assert response.status_code == 200
        assert response.json()["message"] == "Transfer accepted"
        
        acc_response = requests.get(f"{BASE_URL}/{self.pesel}")
        assert acc_response.json()["balance"] == 100.0

    def test_transfer_outgoing_success(self):
        requests.post(f"{BASE_URL}/{self.pesel}/transfer", json={"amount": 500.0, "type": "incoming"})
        
        body = {"amount": 200.0, "type": "outgoing"}
        response = requests.post(f"{BASE_URL}/{self.pesel}/transfer", json=body)
        
        assert response.status_code == 200
        
        acc_response = requests.get(f"{BASE_URL}/{self.pesel}")
        assert acc_response.json()["balance"] == 300.0

    def test_transfer_outgoing_failure_insufficient_funds(self):
        body = {"amount": 100.0, "type": "outgoing"}
        response = requests.post(f"{BASE_URL}/{self.pesel}/transfer", json=body)
        
        assert response.status_code == 422
        
    def test_transfer_account_not_found(self):
        response = requests.post(f"{BASE_URL}/00000000000/transfer", json={"amount": 100.0, "type": "incoming"})
        assert response.status_code == 404

    def test_transfer_invalid_type(self):
        body = {"amount": 100.0, "type": "hacker_attack"}
        response = requests.post(f"{BASE_URL}/{self.pesel}/transfer", json=body)
        
        assert response.status_code == 400
import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/accounts"

class TestAPIAccount:
    def test_create_and_get_account(self):
        test_account = {
            "name": "Jane",
            "surname": "Doe",
            "pesel": "12345678901"
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
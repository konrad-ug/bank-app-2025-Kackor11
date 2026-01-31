import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/accounts"

class TestPerformance:
    def test_perf_create_delete_account(self):
        """
        Test który używając API stworzy, a później usunie konto. Powtórzy to 100 razy. Test ma sprawdzić czy otrzymanie responsu w każdym przypadku będzie krótsze niż 0.5s
        """
        pesel = "99999999999"
        
        for i in range(100):
            requests.delete(f"{BASE_URL}/{pesel}", timeout=0.5)
            
            payload = {
                "name": "Perf",
                "surname": "Tester",
                "pesel": pesel
            }
            response_create = requests.post(BASE_URL, json=payload, timeout=0.5)
            assert response_create.status_code == 201
            
            response_delete = requests.delete(f"{BASE_URL}/{pesel}", timeout=0.5)
            assert response_delete.status_code == 200

    def test_perf_transfers(self):
        """
        Test który używając API stworzy konto i wywoła zaksięgowanie 100 przelewów przychodzących. Odpowiedź w każdym requescie powinna być krótsza niż 0.5s. Test powinien sprawdzić również ostateczne saldo
        """
        pesel = "88888888888"
        requests.delete(f"{BASE_URL}/{pesel}")
        
        payload = {
            "name": "Transfer",
            "surname": "Master",
            "pesel": pesel
        }
        requests.post(BASE_URL, json=payload)
        
        transfer_count = 100
        transfer_amount = 10.0
        
        for i in range(transfer_count):
            transfer_payload = {
                "amount": transfer_amount,
                "type": "incoming"
            }
            response = requests.post(f"{BASE_URL}/{pesel}/transfer", json=transfer_payload, timeout=0.5)
            assert response.status_code == 200
            
        response_get = requests.get(f"{BASE_URL}/{pesel}")
        assert response_get.status_code == 200
        data = response_get.json()
        
        expected_balance = transfer_count * transfer_amount
        assert data["balance"] == expected_balance
        
        requests.delete(f"{BASE_URL}/{pesel}")
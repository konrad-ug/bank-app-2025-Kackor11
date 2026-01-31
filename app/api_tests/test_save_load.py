import requests

BASE_URL = "http://127.0.0.1:5000/api/accounts"

class TestAPISaveLoad:
    def setup_method(self):
        requests.post(f"{BASE_URL}/load")
        
    def test_save_and_load_flow(self):
        pesel = "55555555555"
        requests.delete(f"{BASE_URL}/{pesel}")
        
        requests.post(BASE_URL, json={
            "name": "Persist", 
            "surname": "Data", 
            "pesel": pesel
        })
        
        response_save = requests.post(f"{BASE_URL}/save")
        assert response_save.status_code == 200
        
        requests.delete(f"{BASE_URL}/{pesel}")
        
        response_check = requests.get(f"{BASE_URL}/{pesel}")
        assert response_check.status_code == 404
        
        response_load = requests.post(f"{BASE_URL}/load")
        assert response_load.status_code == 200
        
        response_check_after = requests.get(f"{BASE_URL}/{pesel}")
        assert response_check_after.status_code == 200
        data = response_check_after.json()
        assert data["name"] == "Persist"